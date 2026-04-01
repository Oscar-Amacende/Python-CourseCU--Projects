#Explicamos las rutas
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return jsonify(message="Hello world")

# Otra ruta distinta
@app.route('/hello')
def hello_world():
    return 'Hola jessiii'

@app.route("/health", methods=["GET", "POST"])
def health():
    if request.method == "GET" : return jsonify(status="OK", method="GET"), 200
    if request.method == "GET" : return jsonify(status="OK", method="POST"), 200

@app.route("/ejemplo")
def ejemplo():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
