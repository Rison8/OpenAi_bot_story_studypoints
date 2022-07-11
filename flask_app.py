
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
import json

import os
import openai

openai.api_key = "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"

app = Flask(__name__)
@app.route('/', methods =['GET','POST'])


def handle_request():
    topic_starter = str("Topic: "+request.args.get('input'))
    ai_input = 'Three-Sentence Horror Story:'
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=topic_starter+ai_input,
    temperature=0.8,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0.7,
    presence_penalty=0.5
    )
    output_text = response['choices'][0]['text']
    output_text = output_text.strip('\n')
    data_set = {'User Input': topic_starter , 'Three-Sentence Horror Story': output_text}
    json_dump = json.dumps(data_set)
    return json_dump
