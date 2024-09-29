from flask import Flask, redirect, url_for, session, render_template_string ,render_template ,request
from authlib.integrations.flask_client import OAuth
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

app = Flask(__name__)
app.secret_key = "your_flask_secret_key"  # Replace with a strong secret key

oauth = OAuth(app)

# Configure Google OAuth
google = oauth.register(
    name='google',
    client_id='',
    client_secret='',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/auth/callback')
def auth():
    token = google.authorize_access_token()
    user_info = google.get('https://openidconnect.googleapis.com/v1/userinfo')
    user_info_json = user_info.json()

    # Get the email and name from user_info
    email = user_info_json.get('email')
    name = user_info_json.get('name')
    
    # Create a welcome message
    welcome_message = f'Welcome, {name}! Your email is: {email}'

    # Render welcome message
    return render_template('index.html',name=name)

@app.route('/reviews',methods=['GET', 'POST'])
def form():
    if request.method == 'post':
        userName = request.form.get('name')
        message = request.form.get('message')
        display = f'name :{userName} message: {message},'

        print('reviews',display)
        return render_template_string(f'<h1> {display} </h1>')


    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)


