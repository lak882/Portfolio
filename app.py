from flask import Flask, render_template
import os
import csv

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"]

@app.route("/", methods=["GET"])
def index():
    """Let user search different runs"""
    images = os.listdir(os.path.join(app.static_folder, "art"))
    images = sorted(images)
    return render_template("index.html", images=images)
