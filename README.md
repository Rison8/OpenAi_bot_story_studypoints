# OpenAi bot story and study points webapp setup
Setting up a webapp for a three sentence ai horror story generated from topic from user

requires free accounts with: Openai.com & pythonanywhere.com

Instructions for setting up your webapp

1. create an account on openai.com (this is primarily for getting an API Key to use later)
2. create an account on www.pythonanywhere.com
2. create a new web app tab (from the dashboard)
3. a sample code called flask_app.py will be automatically created
4. Go to files in the pythonanywhere dashboard, click on the mysite directory, open the code called flask_app.py. Replace the code contents with what I have supplied in the script called flask_app.py in the repository
5. on the line where it says 'openai.api_key = "INSERT-YOUR-API-KEY-HERE', retrieve your openai API key from this location (https://beta.openai.com/account/api-keys) and paste it in inside the double quotes. Save the code.
6. on the pythonanywhere home page, click on files. There is a link on it called 'Open Bash Console here'. Click on it.
7. you will get a linux terminal prompt. type in the following command and hit enter: pip install openai
8. after some time has passed it will have installed the package and dependencies with a successful message. This console is where you go if you want to install other python packages to use in your .py scripts
9. (replace insertpythonanywhereusername with your username you used to create your pythonanywhere account) ->paste into the url the follow: insertpythonanywhereusername.pythonanywhere.com/horrorstory/?input=
10. type in a phrase to generate a three sentence horror story after ?input=then hit enter
11. If everything has gone to plan you should get a horror story output*!
* note there are likely to be a number of fiddly bits that may mean this does not occur the first time and you are presented with a error message screen instead.

Change the folder in the url for either marv or study_notes
