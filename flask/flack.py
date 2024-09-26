from flask import Flask,render_template
app = Flask(__name__)
# Define a route for a home page 
@app.route("/")
def home():
    return "Home, Flask!"

@app.route("/about")
def about():
    return "About, Flask!"

@app.route("/login")
def contect():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
    
@app.errorhandler(404)
def not_found(e):
    return "404 Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)