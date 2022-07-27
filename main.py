import os

from flask import Flask, render_template, request
import smtplib
import requests


OWN_EMAIL = "TImjes007@gmail.com"
OWN_PASSWORD = os.environ.get("PORTIFOLIO")
app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html")


@app.route("/contact")
def contact():
    title = "Contact me"
    return render_template("contact.html", title=title)







if __name__ == "__main__":
    app.run(debug=True)