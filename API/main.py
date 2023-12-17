
from flask import render_template # Remove: import Flask
import connexion
import tickets, transport, user
import requests
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/", methods=['GET', 'POST'])
def start():
    s = requests.get("http://127.0.0.1:8000/api/user").json()
    return s


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)