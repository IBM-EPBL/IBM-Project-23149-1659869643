from flask import Flask,render_template
app= Flask(__name__)
@app.route("/")
def Home():
    return render_template('Home.html')
@app.route("/about")
def About():
    return render_template('about.html')
@app.route("/signup")
def signup():
    return render_template('signup.html')
@app.route("/signin")
def signin():
    return render_template('signin.html')