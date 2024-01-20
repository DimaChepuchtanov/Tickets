# people.py
from flask import abort
from datetime import datetime


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
                ]
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
    print(person)

    for key, value in user.items():
        if value["FIO"] == person['FIO']:
            abort(400, "Пользователь уже создан")

    keys = int(list(user.keys())[-1]) + 1

    user[f"{keys}"] = {
            "FIO": person['FIO'],
            "storyBuy": []
        }
    return user[f"{keys}"], 201



def read_all():
    return list(user.values())
