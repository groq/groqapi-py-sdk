import os
import requests
import sys
import grpc
from datetime import datetime

sys.path.append(os.path.join(sys.path[0], "protogen"))
from public.llmcloud.requestmanager.v1 import (
    requestmanager_pb2,
    requestmanager_pb2_grpc,
)

from public.llmcloud.modelmanager.v1 import (
    modelmanager_pb2,
    modelmanager_pb2_grpc,
)

class GroqGrpcConnection:
    _grpc_channel = None
    _auth_token = ""
    _auth_expiry_time = ""
    def _get_groq_key(self, renew=False):
        groq_access_key = os.environ.get("GROQ_SECRET_ACCESS_KEY")
        if self._auth_token != "" and renew is False:
            return self._auth_token

        if groq_access_key is None:
            print("Auth Token Error: Please set env variable GROQ_SECRET_ACCESS_KEY with the unique secret")
            sys.exit(1)

        Headers = {
            "Authorization": "Bearer " + groq_access_key,
        }
        AUTH_URL = "https://api.groq.com/v1/auth/get_token"
        auth_resp = requests.post(url=AUTH_URL, headers=Headers)
        self._auth_token = auth_resp.json()['access_token']
        self._auth_expiry_time = auth_resp.json()['expiry']

    def _is_past_expiry(self):
        return datetime.now() >= datetime.strptime(self._auth_expiry_time, '%Y-%m-%dT%H:%M:%SZ')

    def _open_grpc_channel(self) -> grpc.secure_channel:
        if self._auth_token != "":
            if self._is_past_expiry():
                print("Renewing auth token")
                self._get_groq_key(renew=True)
            else:
                print("Reusing auth token")
        else:
            print("Getting auth token")
            self._get_groq_key(renew=True)

        credentials = grpc.ssl_channel_credentials()
        call_credentials = grpc.access_token_call_credentials(self._auth_token)
        credentials = grpc.composite_channel_credentials(credentials, call_credentials)

        API_URL = "api.groq.com:443"
        query_channel = grpc.secure_channel(API_URL, credentials)
        return query_channel

    def __init__(self):
        self._grpc_channel = self._open_grpc_channel()

    def __del__(self):
        if self._grpc_channel is not None:
            self._grpc_channel.close()

    def get_grpc_channel(self):
        if self._grpc_channel is not None:
            if self._is_past_expiry():
                self._grpc_channel.close()
                self._auth_token = ""
                self._auth_expiry_time = ""
                self._grpc_channel = self._open_grpc_channel()
        else:
            self._grpc_channel = self._open_grpc_channel()

        return self._grpc_channel

grpc_connection = GroqGrpcConnection()

class Models:
    def __init__(self):
        global grpc_connection
        self._query_channel = grpc_connection.get_grpc_channel()
        self._stub = modelmanager_pb2_grpc.ModelManagerServiceStub(self._query_channel)

    def list_models(self):
        request = modelmanager_pb2.ListModelsRequest()
        resp = self._stub.ListModels(request)
        return resp

class ChatCompletion:
    def __init__(self, model):
        global grpc_connection
        self._query_channel = grpc_connection.get_grpc_channel()
        self._stub = requestmanager_pb2_grpc.RequestManagerServiceStub(self._query_channel)
        self._model = model
        self._system_prompt = "Give useful and accurate answers."
        self._lastmessages = []

    def __del__(self):
        self._lastmessages = []

    def __enter__(self):
        global grpc_connection
        self._query_channel = grpc_connection.get_grpc_channel()
        return self

    def __exit__(self, *args: object) -> None:
        self._lastmessages = []
        return None

    def _update_history(self, user_prompt, response):
        self._lastmessages.append({"user_prompt" : user_prompt, "last_resp" : response})

    def send_chat(
        self,
        user_prompt = "Write multiple paragraphs",
        seed=1234,
        max_tokens=2048,
        temperature=0.7,
        top_p=0.3,
        top_k=40,
    ):
        # Generate request
        request = requestmanager_pb2.GetTextCompletionRequest()
        request.user_prompt = user_prompt

        for msg in self._lastmessages:
            req = request.history.add()
            req.user_prompt = msg["user_prompt"]
            req.assistant_response = msg["last_resp"]

        request.model_id = self._model
        request.system_prompt = self._system_prompt
        request.seed = seed
        request.max_tokens = max_tokens
        request.temperature = temperature
        request.top_p = top_p
        request.top_k = top_k

        try:
            resp = self._stub.GetTextCompletion(request)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
                print('Invalid Args. Please check model name and other params')
            elif e.code() == grpc.StatusCode.UNAVAILABLE:
                print(f"grpc error: {e.details()}. Requested model maybe currently offline.")
            else:
                raise e
            return "", "", {}

        # Save last messages
        self._update_history(user_prompt, resp.content)

        return resp.content, resp.request_id, resp.stats

class Completion:
    def __init__(self):
        global grpc_connection
        self._query_channel = grpc_connection.get_grpc_channel()
        self._stub = requestmanager_pb2_grpc.RequestManagerServiceStub(self._query_channel)

    def __del__(self):
        return

    def __enter__(self):
        global grpc_connection
        self._query_channel = grpc_connection.get_grpc_channel()
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def send_prompt(
        self,
        model,
        user_prompt = "Write multiple paragraphs",
        system_prompt="Give useful and accurate answers.",
        seed=1234,
        max_tokens=2048,
        temperature=0.7,
        top_p=0.3,
        top_k=40,
    ):
        # Generate request
        request = requestmanager_pb2.GetTextCompletionRequest()
        request.user_prompt = user_prompt
        request.model_id = model
        request.system_prompt = system_prompt
        request.seed = seed
        request.max_tokens = max_tokens
        request.temperature = temperature
        request.top_p = top_p
        request.top_k = top_k

        try:
            resp = self._stub.GetTextCompletion(request)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
                print('Invalid Args. Please check model name and other params')
            elif e.code() == grpc.StatusCode.UNAVAILABLE:
                print(f"grpc error: {e.details()}. Requested model maybe currently offline.")
            else:
                raise e
            return "", "", {}
        
        return resp.content, resp.request_id, resp.stats
