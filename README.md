# freesound-oauth2-python-flask
A simple web app based on flask and python to download original sound files from freesound.org using oauth2 authorization

Code optimised from [kemitche's repository](https://gist.github.com/kemitche/9749639).


## Setup

1. Install dependencies from requirements.txt. Ideally create a [virtualenv](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) and install the requirements

2. Apply for your freesound API key from [here](http://freesound.org/apiv2/apply/) and update it in the code

3. [IMPORTANT] Set your "callback_url" as http://localhost:5000/freesound_callback

4. Open terminal and navigate to your working directory and run the code.

  In Mac

      $ export FLASK_APP=freesound_oauth2.py
      $ flask run

  In Windows

      $ export FLASK_APP=freesound_oauth2.py
      $ python -m flask run
 
 5. Open your web browser with url http://localhost:5000 and authorise your app.
 
_________________________
 
 Find flask documentation [here](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application)
   
