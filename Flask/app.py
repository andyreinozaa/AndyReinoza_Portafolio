from Flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.get("/")
def home():
        return render_template("home.html")

@app.get("/projetos")
def projetos():
        return render_template("projects.html")
    
@app.get("/sobre-me")
def sobre_me():
    return render_template("about-me.html")