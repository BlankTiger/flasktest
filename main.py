from flask import Flask
from markupsafe import escape

app = Flask("flasktest")

with open("index.html") as f:
    INDEX_PAGE = f.read()


@app.route("/")
def index() -> str:
    return INDEX_PAGE


@app.route("/api/hi/<string:name>")
def hello_name(name: str) -> str:
    p_tag = f"<p>Hello, {escape(name)}!</p>"
    return p_tag
