# Building and installation

1. To build run:
`python setup.py sdist bdist_wheel`

2. Install built pip wheel:
`pip3 install dist/groq_llm_api-0.5.0-py3-none-any.whl`

3. Set the secret access key as an env variable:
`export GROQ_SECRET_ACCESS_KEY="<secret key>"`

4. Run following examples


# Examples:

Code:
```
#!/usr/bin/env python3

from groq.llmcloud import Models

# List all Models first
modelmanager = Models()
print("Listing supported models")
print(modelmanager.list_models())
```

Output:
```
Getting auth token
Listing supported models
models {
  id: "llama2-70b-2048"
  details {
    family: "Llama"
    version: "2"
    size: "70B"
    sequence_length: 2048
    tag: "2023090300"
    name: "Llama 2"
  }
  meta {
    created: 1693721698
  }
}
models {
  id: "llama2-7b-2048"
  details {
    family: "Llama"
    version: "2"
    size: "7B"
    sequence_length: 2048
    tag: "2023090301"
    name: "Llama 2"
  }
  meta {
    created: 1693721698
  }
}
models {
  id: "codellama-34b"
  details {
    family: "Llama"
    version: "2"
    size: "34B"
    sequence_length: 16384
    tag: "20230100300"
    name: "Code Llama"
  }
  meta {
    created: 1693767886
  }
}
models {
  id: "jais-13b-chat"
  details {
    family: "Jais"
    version: "1"
    size: "13B"
    sequence_length: 2048
    tag: "20230100300"
    name: "Jais Chat"
  }
  meta {
    created: 1693767886
  }
}
models {
  id: "falcon-40b"
  details {
    family: "Falcon"
    version: "1"
    size: "40B"
    sequence_length: 2048
    tag: "20230100300"
    name: "Falcon"
  }
  meta {
    created: 1693767886
  }
}
```

ChatCompletion example:

Code:
```
#!/usr/bin/env python3

from groq.llmcloud import ChatCompletion

with ChatCompletion("llama2-70b-2048") as chat:
  prompt = "Who won the world series in 2020?"
  response, id, stats =  chat.send_chat(prompt)
  print(f"Question : {prompt}\nResponse : {response}\n")
  prompt = "The Los Angeles Dodgers won the World Series in 2020."
  response, id, stats =  chat.send_chat(prompt)
  print(f"Question : {prompt}\nResponse : {response}\n")
  prompt = "Where was it played?"
  response, id, stats =  chat.send_chat(prompt)
  print(f"Question : {prompt}\nResponse : {response}\n")
```
Output:
```
Question : Who won the world series in 2020?
Response : The Los Angeles Dodgers won the World Series in 2020. They defeated the Tampa Bay Rays in the Fall Classic, winning the series 4 games to 2.

Question : The Los Angeles Dodgers won the World Series in 2020.
Response : That's correct! The Los Angeles Dodgers won the World Series in 2020, defeating the Tampa Bay Rays in the Fall Classic. Well done!

Question : Where was it played?
Response : The 2020 World Series was played at Globe Life Field in Arlington, Texas. It was the first time that the World Series was played at this stadium, which was opened in 2020. The Dodgers and Rays played six games at Globe Life Field, with the Dodgers winning four of them.
```

Completion example:
```
#!/usr/bin/env python3

from groq.llmcloud import Completion

with Completion() as completion:
  prompt = "What are transformers in machine learning"
  response, id, stats = completion.send_prompt("llama2-70b-2048", user_prompt=prompt)
  if response != "":
      print(f"\nPrompt: {prompt}\n")
      print(f"Request ID: {id}")
      print(f"Output:\n {response}\n")
      print(f"Stats:\n {stats}\n")

```
Output:
```
Prompt: What are transformers in machine learning

Request ID: 2XUQlIAUbWKN9wxfUwcBoHl0qVr
Output:
 In machine learning, transformers are a type of neural network architecture that is commonly used for natural language processing tasks such as language translation, language modeling, and text classification. Transformers were introduced in a paper by Vaswani et al. in 2017 and have since become widely used in the field.

The key innovation of transformers is the self-attention mechanism, which allows the model to attend to different parts of the input sequence simultaneously and weigh their importance. This is in contrast to traditional recurrent neural networks (RNNs), which process the input sequence one element at a time and have recurrence connections that allow them to capture long-range dependencies.

Transformers consist of an encoder and a decoder. The encoder takes in a sequence of tokens (e.g. words or characters) and outputs a sequence of vectors, called "keys," "values," and "queries." The decoder then takes these vectors as input and outputs a sequence of tokens. During training, the model is trained to minimize the difference between the predicted tokens and the actual tokens in the target sequence.

One of the key advantages of transformers is their ability to parallelize computation across input sequences. This allows them to handle long input sequences efficiently and makes them well-suited for tasks such as machine translation, where the input and output sequences can be quite long.

Transformers have been used to achieve state-of-the-art results on a number of natural language processing tasks, including machine translation, language modeling, and text classification. They have also been used for other sequence-to-sequence tasks such as image captioning and speech recognition.

Stats:
 time_generated: 0.950264345
tokens_generated: 352
time_processed: 0.026768545
tokens_processed: 35
```

Model offline example:

Code:
```
#!/usr/bin/env python3

from groq.llmcloud import Completion

compl = Completion()
prompt = "What are transformers in machine learning"
response, id, stats = compl.send_prompt("codellama-34b", user_prompt=prompt)
```
Output:
```
grpc error: upstream request timeout. Requested model maybe currently offline.
```
