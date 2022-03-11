from flask import Flask
from flask import jsonify
from Tokenizer import tokens

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/localidades/<query>")
def busca_localidades(query):
    return jsonify({'localidades': tokens.get(query)})

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")