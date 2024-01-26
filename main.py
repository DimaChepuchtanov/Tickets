
from flask import render_template, Flask
import connexion

import requests
app = Flask(__name__)


@app.route("/web/main", methods=['GET', 'POST'])
def start():
    data = {"user": "None",
            "includes": "main.html"}
    return render_template("base.html", **data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)