from flask import Flask, render_template, request
from comprehensive import *
from inclusiveTermFixer import *
from sentiment import *

app = Flask(__name__)


@app.route('/')
def load_page():
    return render_template('index.html')


@app.route('/processdata', methods=["POST"])
def processData():
    data = request.form.get('getText')
    # function that takes in data and returns suggestions
    return fixTerms(data)

@app.route('/suggestionsdata', methods=["POST"])
def suggestionsData():
    data = request.form.get('getSuggestions')
    return syntax_process(data) #function that returns suggestions

@app.route('/sentimentdata', methods=["POST"])
def sentimentsData():
    data = request.form.get('getSentiments')
    return analyze_sentiment(data) #function that returns sentiment


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
