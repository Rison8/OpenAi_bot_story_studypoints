
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
import json

import os
import openai

openai.api_key = "YOUR_API_GOES_HERE" #generate an API from OpenAI and put it inside the quotes


app = Flask(__name__, template_folder='.')

#home
@app.route("/")
def home():
    return render_template("index.html") #make sure you have an index.html file in the same place as this code

@app.route('/horrorstory/', methods =['GET','POST'])
def handle_request():
    topic_starter = str("Topic: "+request.args.get('input'))
    ai_input = 'Three-Sentence Horror Story:\n'
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=ai_input+topic_starter,
    temperature=0.8,
    max_tokens=350,
    top_p=1,
    frequency_penalty=0.7,
    presence_penalty=0.5
    )
    output_text = response['choices'][0]['text']
    output_text = output_text.strip('\n')
    output_simple_text = "Short Horror Story: " + output_text
    #data_set = {'User Input': topic_starter , 'Three-Sentence Horror Story': output_text}
    #json_dump = json.dumps(data_set)
    return f"{output_simple_text}"

@app.route('/sarcastic_marv/', methods =['GET','POST'])
def marv_request():
  marv_starter = str(request.args.get('input'))
  ai_input ='Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n'
  response = openai.Completion.create(
  model="text-davinci-002",
  prompt=ai_input+marv_starter,
  temperature=0.5,
  max_tokens=300,
  top_p=0.3,
  frequency_penalty=0.5,
  presence_penalty=0
  )
  marv_text = response['choices'][0]['text']
  marv_text = marv_text.strip('\n')
  marv_text_simple = "Marv: " + marv_text
  return f"{marv_text_simple}"


@app.route('/study_notes/', methods =['GET','POST'])
def sn_request():
  sn_starter = str(request.args.get('input'))
  ai_input ='What are 5 key points I should know when studying\n'
  response = openai.Completion.create(
  model="text-davinci-002",
  prompt=ai_input+sn_starter,
  temperature=0.3,
  max_tokens=200,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )
  sn_text = response['choices'][0]['text']
  sn_text = sn_text.strip('\n')
  sn_text_simple = "5 key points: " + sn_text
  return f"{sn_text_simple}"

@app.route('/jeff/', methods =['GET','POST'])
def jeff_request():
  jeff_starter = str(request.args.get('input'))
  #start_sequence = "\nJeff:"
  #restart_sequence = "\nYou: "
  response = openai.Completion.create(
  model="text-davinci-002",
  prompt=jeff_starter,
  temperature=0.5,
  max_tokens=90,
  top_p=1,
  frequency_penalty=0.7,
  presence_penalty=0.5
  )
  jeff_text = response['choices'][0]['text']
  jeff_text = jeff_text.strip('\n')
  jeff_text_simple = "Jeff cares: " + jeff_text
  return f"{jeff_text_simple}"

@app.route('/random_horrorstory/', methods =['GET','POST'])
def horrorstory_extended_request():
    ai_input = 'multiple sentence horror story random prompt:\n'
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=ai_input,
    temperature=0.7,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0.3,
    presence_penalty=0.2
    )
    output_text = response['choices'][0]['text']
    output_text = output_text.strip('\n')
    data_set = {'Horror Story': "Random Horror Story: " + output_text}
    json_dump = json.dumps(data_set)
    #convert string to  object
    json_object = json.loads(json_dump)
    return json_object["Horror Story"]

@app.route('/random_song_genre/', methods =['GET','POST'])
def random_song_genre_request():
  req_genre = str(request.args.get('input'))
  ai_input = 'Random song request by ' + req_genre + '\n'
  response = openai.Completion.create(
  model="text-davinci-002",
  prompt=ai_input,
  temperature=0.7,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.9,
  presence_penalty=0.9
  )
  rsgr_text = response['choices'][0]['text']
  rsgr_text = rsgr_text.strip('\n')
  rsgr_text_simple = "Random Song: " + rsgr_text
  return f"{rsgr_text_simple}"


from werkzeug.exceptions import HTTPException

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    return "Sorry - this application is currently offline pending approval for more credits from OpenAI. Therefore Horry Story, chat with Jeff, chat with Marv and random song genre generators are all offline"
    # render_template("500_generic.html", e=e), 500

