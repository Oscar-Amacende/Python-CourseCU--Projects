from flask import Flask,request, jsonify
import requests

app = Flask(__name__)

#ruta 1
@app.route("/")
def get_author():
    res = requests.get("https://openlibrary.org/search/authors.JSON?q=Michael Crichton")
    if res.status_code == 200:
        return jsonify(res.json())
    elif res.status_code == 404:
        return jsonify({"message" : "Something went wrong!"}), 404
    else :
        return jsonify({"message" : "Server error!"}), 500

#ruta 2
@app.route("/1")
def hola():
    return "<b> My first flask aplication in action </b>"


def fetch_from_database(query):
    url = f"https://openlibrary.org/search.json?q={query}"
    res = requests.get(url)

    if res.status_code == 200:
        return res.json()
    return {"error": "No se pudo obtener información"}

#ruta 3

#Simulamos la peticion del DB
def fetch_from_database(query):
    url = f"https://openlibrary.org/search.json?q={query}"
    res = requests.get(url)

    if res.status_code == 200:
        return res.json()
    return {"error": "No se pudo obtener información"}


@app.route("/2")
def search_response():
    query = request.args.get("q")

    if not query:
        return jsonify({"error_message" : "Input parameter missing"}), 422
    
    #
    resource = fetch_from_database(query)

    if resource:
        return jsonify({"message" : resource})
    else :
        return jsonify({"error_message": "Resource not found"}), 404

@app.route("/3")
def jsonify_decorator(function):
    def modifyOutput():
        return {"output":function()}
    return modifyOutput
@jsonify_decorator
def hello():
    return "Hello world"
@jsonify_decorator
def add():
    num1 = input("Enter a number: ")
    num2 = input("Enter another  number: ")
    return int(num1)+int(num2)

print(hello())
print(add())
if __name__ == '__main__':
    app.run(debug=True)

##Error handling 
# 1xx Request received
# 2xx Succesful
# 3xx proper and redirected
# 4xx client error
# 5xx server error
