from  flask import Flask

app = Flask(__name__)

from productos import productos

@app.route("/")
def entrada():
    pass

if __name__ == "__main__":
    app.run(debug=True)

