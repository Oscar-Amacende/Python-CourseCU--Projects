from flask import Flask, jsonify, request, render_template
from flask import render_template 
import sqlite3

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return jsonify(message="Hello world")

# Otra ruta distinta
@app.route('/hello')
def hello_world():
    return 'Hola jessiii'

posts = []

@app.route("/post")
def show_posts():
    return "Mostrando el post {}".format(len(posts))

@app.route("/health", methods=["GET", "POST"])
def health():
    if request.method == "GET" : return jsonify(status="OK", method="GET"), 200
    if request.method == "POST" : return jsonify(status="OK", method="POST"), 200

@app.route("/ejemplo")
def ejemplo():
    name = request.args.get("name")
    return render_template('index.html',person="Jessica mtz mtz")

#inicializamos la base de datos

def init_db():
    conn = sqlite3.connect("Base.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


@app.route("/login", methods=['POST'])
def login():
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not  password:
        return jsonify({"error" : "Faltan datos"}),400
    
    conn = sqlite3.connect("Base.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
    )

    conn.commit()
    conn.close()

    return jsonify({"message" : f"Usuario {username} guardado"}), 201



# Al arrancar la aplicacion inicializar la base de datos 
if __name__ == '__main__':
    init_db()
    app.run(debug=True)


