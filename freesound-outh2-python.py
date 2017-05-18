# A python web server oauth2 authorization for freesound.org

# optimised from kemitche's repository https://gist.github.com/kemitche/9749639

from flask import Flask, abort, request
from uuid import uuid4
import requests
import requests.auth
import urllib


CLIENT_ID = "YOUR CLIENT_ID HERE"
CLIENT_SECRET = "YOUR CLIENT_SECRET HERE"

# AUTHORIZE_URL = "https://www.freesound.org/apiv2/oauth2/authorize/"
# ACCESS_TOKEN_URL = "https://www.freesound.org/apiv2/oauth2/access_token/"
# REDIRECT_URI = "http://localhost:5000/freesound_callback"


def user_agent():
    return "freesound oauth2-sample-web-app"

def base_headers():
    return {"User-Agent": user_agent()}

app = Flask(__name__)
@app.route('/')
def homepage():
    text = '<a href="%s">Authenticate with freesound.org</a>'
    return text % make_authorization_url()

def make_authorization_url():
    # Generate a random string for the state parameter
    # Save it for use later to prevent xsrf attacks
    state = str(uuid4())
    save_created_state(state)
    params = {"client_id": CLIENT_ID,
              "response_type":"code",
              "state": state
              }
    url = "https://www.freesound.org/apiv2/oauth2/authorize/?" + urllib.urlencode(params)
    return url


def save_created_state(state):
    pass
def is_valid_state(state):
    return True

@app.route('/freesound_callback')
def freesound_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    state = request.args.get('state', '')
    if not is_valid_state(state):
        # Uh-oh, this request wasn't started by us!
        abort(403)
    code = request.args.get('code')
    access_token = get_token(code)
    save_access_token(access_token)
    return "Your access token is: %s" % access_token

def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "authorization_code",
                 "code": code
                 }
    headers = base_headers()
    response = requests.post("https://www.freesound.org/apiv2/oauth2/access_token/",
                             auth=client_auth,
                             headers=headers,
                             data=post_data)
    token_json = response.json()
    return token_json["access_token"]
    
    
def get_username(access_token):
    headers = base_headers()
    headers.update({"Authorization": "bearer " + access_token})
    response = requests.get("https://www.freesound.org/apiv2/me/", headers=headers)
    me_json = response.json()
    print me_json['name']
    return me_json['name']

def save_access_token(access_token):
    # save your access_token as a .txt file in your working directory
    doc = open("access_token","w")
    doc.write(access_token)
    doc.close()
    # call the function to download the sound file by providing access token  freesound sound_id as an argument.
    fs_downloader(access_token,"SOUND_ID") # replace SOUND_ID with freesound sound_id you want to download
    return


def fs_downloader(access_token,sound_id):
    download_uri = "https://www.freesound.org/apiv2/sounds/" + sound_id + "/download/"
    filepath = "/freesound_download/" # modify here to save the audio file to an different directory
    headers = base_headers()
    headers.update({"Authorization": "bearer " + access_token})
    response = requests.get(download_uri, headers=headers, stream=True)
    print response.headers
    file_string = response.headers['Content-Disposition']
    filename = str(re.findall(r'"([^"]*)"', file_string)).strip('[]')
    filename = filename[1:-1] #stripping first and last character of the string
    print response.url,"\n\n" 
    # writing audio file to disk 
    with open(filepath+filename, 'wb') as fd:
        for chunk in response.iter_content(response.headers['Content-Length']>100):
            fd.write(chunk)
    print "\n Download completed ......"
    return 


if __name__ == '__main__':
    app.run(debug=True, port=5000)
