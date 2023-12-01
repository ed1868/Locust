# import openai
from flask import Flask, render_template, request
# from dotenv import dotenv_values
import json
import time
# config = dotenv_values('.env');
# openai.api_key = config["OPENAI_API_KEY"]


app = Flask(__name__,
    template_folder='templates',
    # static_url_path='', 
    # static_folder='static'
)

@app.route("/")
def index():
    return "HELLOOOOOO"


@app.route("/slow")
def slow_route():
    time.sleep(5)  # Wait for 5 seconds before proceeding
    return "This is a slow response"





if __name__ == "__main__":
    app.run(debug=True)
