#!/usr/bin/env python3

import os

from groq.llmcloud import Completion
from groq.llmcloud import ChatCompletion
from groq.llmcloud import Models

if __name__ == "__main__":
    # Set env var GROQ_SECRET_ACCESS_KEY with the access, or you can also set it below
    # os.environ["GROQ_SECRET_ACCESS_KEY"] = ''

    # List all Models first
    modelmanager = Models()
    print("Listing supported models")
    print(modelmanager.list_models())

    with ChatCompletion("llama2-70b-4096") as chat:
        prompt = "Who won the world series in 2020?"
        response, id, stats =  chat.send_chat(prompt)
        print(f"Question : {prompt}\nResponse : {response}\n")
        prompt = "The Los Angeles Dodgers won the World Series in 2020."
        response, id, stats =  chat.send_chat(prompt)
        print(f"Question : {prompt}\nResponse : {response}\n")
        prompt = "Where was it played?"
        response, id, stats =  chat.send_chat(prompt)
        print(f"Question : {prompt}\nResponse : {response}\n")

    with ChatCompletion("llama2-70b-4096") as chat:
        prompt = "Who won the world series in 2020?"
        response =  chat.send_chat(prompt, streaming=True)
        print(f"Question : {prompt}\nResponse :\n")
        output = ""
        for resp in response:
            output += resp.content
        print(output)
        prompt = "The Los Angeles Dodgers won the World Series in 2020."
        response =  chat.send_chat(prompt, streaming=True)
        print(f"Question : {prompt}\nResponse :\n")
        output = ""
        for resp in response:
            output += resp.content
        print(output)
        prompt = "Where was it played?"
        response =  chat.send_chat(prompt, streaming=True)
        print(f"Question : {prompt}\nResponse :\n")
        output = ""
        for resp in response:
            output += resp.content
        print(output)

    compl = Completion()
    prompt = "What are transformers in machine learning"
    response, id, stats = compl.send_prompt("llama2-70b-4096", user_prompt=prompt)
    if response != "":
        print(f"\nPrompt: {prompt}\n")
        print(f"Request ID: {id}")
        print(f"Output:\n {response}\n")
        print(f"Stats:\n {stats}\n")

    # Streaming Completion example
    compl = Completion()
    prompt = "What are transformers in machine learning"
    response = compl.send_prompt("llama2-70b-4096", user_prompt=prompt, streaming=True)
    print(f"\nPrompt: {prompt}\nStream Output:\n")
    output = ""
    for resp in response:
        output += resp.content
    print(output)
