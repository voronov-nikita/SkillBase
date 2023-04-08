import flask


app = flask.Flask(__name__)

# откроется в самом начале (главная старница)
@app.route("/")
def index():
    return "Hello"

# откроется при переходе по пути /about
@app.route("/about")
def about():
    return "About"


@app.route("/json")
def json_flask():
    data = {
        "name": "Nikita",
        "age": 16,
        "status": True
    }
    return flask.jsonify(data)

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")