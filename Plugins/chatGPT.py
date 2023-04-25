import random
import openai
import os
from dotenv import load_dotenv
load_dotenv()

# OpenAI Initialization
openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_KEY")


def new_chat(prompt):
    chatResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt="\nHuman: " + prompt + "\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return chatResponse['choices'][0]['text']


def write_paper(prompt):
    chatResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt="\nHuman: " + prompt + "\nAI:",
        temperature=0.9,
        max_tokens=5000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    number = random.randrange(1, 100)
    file_name = "paper" + str(number)
    file_path = "./Assistant Files/" + file_name + ".txt"
    f = open("./Assistant Files/" + file_name + ".txt", "w+")
    f.write(chatResponse['choices'][0]['text'])
    f.close()
    osCommandString = "notepad.exe " + file_path + ""
    os.system(osCommandString)


def summarize(prompt):
    chatResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt="Summarize this text:\n\n " + prompt,
        temperature=0.5,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    return chatResponse['choices'][0]['text']


def getJoke(prompt):
    chatResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    return chatResponse['choices'][0]['text']
