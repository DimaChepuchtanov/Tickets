
from flask import render_template, Flask
import connexion

import requests as rq
app = Flask(__name__)


@app.route("/web/main", methods=['GET', 'POST'])
def start():
    data = {"user": "man",
            "userName": "Иванов Иван Иванович",
            "includes": "main.html"}
    return render_template("base.html", **data)


@app.route("/web/main/post/<int:page>", methods=['GET', 'POST'])
def mainPost(page):
    info = rq.post(f"http://127.0.0.1:8080/api/post/show/{page}").json()
    data = {"user": "man",
            "includes": "post.html",
            "page": page,
            "url": info['status']['images'][0],
            "content": ["Во-первых, мы предлагаем широкий выбор транспортных средств. Независимо от того, нужен ли вам билет на поезд, самолет, автобус или другой вид транспорта, у нас вы всегда найдете подходящий вариант. Мы понимаем, что каждый клиент уникален и может иметь свои предпочтения, поэтому стараемся предложить максимальную гибкость в выборе.",
                        "Во-вторых, мы гарантируем удобство и надежность. Наша система бронирования и оплаты билетов работает без сбоев, а наши партнеры по транспорту имеют безупречную репутацию. Мы ценим ваше время и комфорт, поэтому стремимся предоставить лучший сервис.",
                        "В-третьих, мы предлагаем конкурентные цены. Мы следим за рыночной ситуацией и стараемся предложить нашим клиентам самые выгодные тарифы. Мы уверены, что качественный сервис не обязательно должен быть дорогим, и поэтому работаем над тем, чтобы наши цены были доступны для всех.",
                        "Наконец, мы ценим каждого клиента и стремимся предоставить ему индивидуальный подход. Наша команда профессионалов готова помочь вам с выбором билетов, ответить на все вопросы и решить любые возникшие проблемы. Мы гордимся своим отношением к клиентам и стремимся делать все возможное, чтобы оправдать ваше доверие.",
                        "Таким образом, если вы задаетесь вопросом 'почему именно мы?', ответ прост - мы предлагаем удобство, надежность, выгодные цены и индивидуальный подход. Мы верим, что выбор билетов на транспорт должен быть легким и приятным, и готовы сделать все возможное, чтобы сделать ваше путешествие комфортным и беззаботным."]
            }
    return render_template("base.html", **data)


@app.route("/web/profile/<UserName>", methods=['GET', 'POST'])
def profile(UserName: str):
    
    profile_user = rq.get(f"http://127.0.0.1:8080/api/user/{UserName}").json()
    profile = profile_user['status']
    posts = []

    for i in profile['post']:
        postInfo = rq.post(f"http://127.0.0.1:8080/api/post/show/{int(i)}").json()
        posts.append({"id": postInfo['status']['id'],
                      "title": postInfo['status']['title'],
                      "discribe": postInfo['status']['discribe'],
                      "images": postInfo['status']['images']})
        
    data = {"user": "man",
            "includes": "profile.html",
            "userId": profile['FIO'],
            "postList": posts,
            "userName": profile['FIO'],
            "profile": [f"Пользователь: {profile['FIO']}", f"Возраст: {profile['age']}", f"Пол: {profile['sex']}"]
            }
    return render_template("base.html", **data)


@app.route("/web/profile/token/<UserName>", methods=['GET', 'POST'])
def token(UserName: str):
    profile_user = rq.get(f"http://127.0.0.1:8080/api/user/{UserName}").json()
    profile = profile_user['status']

    active_token = []
    token = rq.get(f"http://127.0.0.1:8080/api/token/check/{profile['ID']}").json()
    if token['status'] == "Пользователь не найден":
        active_token = [None, "create"]
    elif token['status'] == "Токен просрочен":
        text = rq.get(f"http://127.0.0.1:8080/api/token/show/{profile['ID']}").json()
        active_token = [text['status'], "update"]
    else:
        text = rq.get(f"http://127.0.0.1:8080/api/token/show/{profile['ID']}").json()
        active_token = [text['status'], "None"]

    data = {"user": "man",
            "includes": "token.html",
            "token": active_token,
            "idUser": profile['ID'],
            "profile": [f"Пользователь: {profile['FIO']}", f"Возраст: {profile['age']}", f"Пол: {profile['sex']}"]
            }
    return render_template("base.html", **data)


@app.route("/web/ticket", methods=['GET', 'POST'])
def ticket():

        
    data = {"user": "man",
            "includes": "BuyTiket.html",
            }
    return render_template("base.html", **data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)