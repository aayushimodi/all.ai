from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def load_page():
    return render_template('index.html')


@app.route('/processdata', methods=["POST"])
def processData():
    data = request.form.get('getText')
    print(data)
    return data
    # modify text
    # return modified_text


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
