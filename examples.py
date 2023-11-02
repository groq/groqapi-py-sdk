#!/usr/bin/env python3

from groq.llmcloud import Completion
from groq.llmcloud import ChatCompletion
from groq.llmcloud import Models

if __name__ == "__main__":
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

    compl = Completion()
    prompt = "What are transformers in machine learning"
    response, id, stats = compl.send_prompt("llama2-70b-4096", user_prompt=prompt)
    if response != "":
        print(f"\nPrompt: {prompt}\n")
        print(f"Request ID: {id}")
        print(f"Output:\n {response}\n")
        print(f"Stats:\n {stats}\n")

