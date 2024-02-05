# people.py
from flask import abort
from datetime import datetime
from database import connect as cn

cursor = cn.cursor()


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


user = {"0":
        {
            "FIO": "Иванов Иван Иванович",
            "storyBuy":
                [
                    {
                        "id": 1,
                        "en":
                        {
                            "start": "Perm (Savino)",
                            "end": "Moscow (Domodedovo)",
                            "start-date": "19.09.2023",
                            "start-time": "03:40:00 pm",
                            "end-date": "20.09.2023",
                            "end-time": "03:40:00 am",
                            "price": "120 $"
                        },

                        "ru":
                        {
                            "start": "Пермь (Савино)",
                            "end": "Москва (Домодедово)",
                            "start-date": "19.09.2023",
                            "start-time": "15:40:00",
                            "end-date": "20.09.2023",
                            "end-time": "03:40:00",
                            "price": "2500 рублей"
                        }
                    },
                    {
                        "id": 2,
                        "en":
                        {
                            "start": "Perm (Savino)",
                            "end": "Moscow (Domodedovo)",
                            "start-date": "19.09.2023",
                            "start-time": "01:40:00 pm",
                            "end-date": "20.09.2023",
                            "end-time": "03:40:00 am",
                            "price": "120 $"
                        },

                        "ru": {
                            "start": "Пермь (Савино)",
                            "end": "Москва (Домодедово)",
                            "start-date": "19.09.2023",
                            "start-time": "15:40:00",
                            "end-date": "20.09.2023",
                            "end-time": "03:40:00",
                            "price": "2500 рублей"
                        }
                    }
                ],
            "filter": {"language": 'ru',
                       "countTransport": "2",
                       "typeTransport": ["avia", "bus"]}
            }
        }


def update(userInfo, newData):
    if userInfo in user:
        value = user[userInfo]['storyBuy']
        value.append(newData)
        user[userInfo]['storyBuy'] = value
        return user[userInfo]
    else:
        abort(
            404,
            f"Person with last name {userInfo} not found"
        )


def read_one(userInfo):
    """Информация о конкретном пользователе"""

    for key, value in user.items():
        if value['FIO'] == userInfo:
            return value
    else:
        abort(
            404, f"Person with last name {userInfo} not found"
        )


def create(person):
    """Создание нового пользователя"""

    findUser = False
    try:
        cursor.execute(f"SELECT id FROM clients WHERE 'FIO' = '{person['FIO']}'")
        findUser = cursor.fetchone()
    except Exception as e:
        abort(404, f"Ошибка запроса на поиск пользователя. Ошибка {e}")
    
    if findUser is not None:
        abort(404, f"Пользователь уже существует")
    else:
        try:
            cursor.execute(f"SELECT MAX(id) FROM clients")
            findUser = cursor.fetchone()
            cursor.execute(f"INSERT INTO clients VALUES({findUser[0] + 1}, '{person['FIO']}', '[]', '{['languageru', 'counttransport2', 'typetransportbusandtrain']}'")
            cn.commit()
        except Exception as e:
            abort(404, f"Ошибка создания. {e}")
    
    return person['FIO'], 201


def read_all():
    """Возвращает информацию о всех пользователях"""
    tickets = {}

    try:
        cursor.execute("SELECT * FROM clients")
        answer = cursor.fetchall()
        print(answer)
        for i in answer:

            ticketBought = {"aviva": [],
                            "train": [],
                            "bus": [],
                            "error": []}
            try:
                for ticket in i[2]:
                    if "Air" in ticket:
                        ticketBought["aviva"].append(ticket.removeprefix("Air"))
                    elif "Bus" in ticket:
                        ticketBought["bus"].append(ticket.removeprefix("Bus"))
                    elif "Train" in ticket:
                        ticketBought["train"].append(ticket.removeprefix("Train"))
                    else:
                        ticketBought['error'].append(ticket)
            except:
                ticketBought = {}

            try:
                paramFilter = {"language": i[3][0].removeprefix("language"),
                           "countTransport": i[3][1].removeprefix("counttransport"),
                           "typetransport": i[3][2].removeprefix("typetransport").split("and")}
            except:
                paramFilter = {}

            tickets[i[0]] = {"id": i[0],
                             "FIO": i[1],
                             "StoryBuy": ticketBought,
                             "filter": paramFilter
                             }

        return tickets
    except Exception as e:
        abort(404, f"Ошибка запроса. {e}")
    
