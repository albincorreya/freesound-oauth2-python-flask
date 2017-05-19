# freesound-oauth2-python-flask
A simple web app based on flask and python to download original sound files from freesound.org using oauth2 authorization

Code optimised from [kemitche's repository](https://gist.github.com/kemitche/9749639).


# Setup

1. Apply for your freesound API key from [here](http://freesound.org/apiv2/apply/) and to the code

2. [IMPORTANT] Set your "callback_url" as http://localhost:5000/freesound_callback

3. Open terminal and navigate to your working directory and run the code.

  In Mac

      $ export FLASK_APP=freesound_oauth2.py
      $ flask run

  In Windows

      $ export FLASK_APP=freesound_oauth2.py
      $ python -m flask run
 
 4. Open your web browser with url http://localhost:5000 and authorise your app.
 
_________________________
 
 Find flask documentation [here](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application)
   
