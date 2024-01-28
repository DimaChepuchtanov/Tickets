# Модуль API для билетов
#
# Разделы для билетов РЖД, самолет и автобус
#

from flask import abort
from datetime import datetime
from pprint import pprint
from database import connect as cn

cursor = cn.cursor()
"""Данные по Авиабилетам"""

marshrut_air = {
    0: {
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

        "ru": {
            "start": "Пермь (Савино)",
            "end": "Москва (Домодедово)",
            "start-date": "19.09.2023",
            "start-time": "15:40:00",
            "end-date": "20.09.2023",
            "end-time": "03:40:00",
            "price": "2500 рублей"
        }   
        },
    1: {
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
}

marshrut_train = {}

marshrut_bus = {}


def all_marshurts_avia(language):
    """Функция получения всех маршрутов авиа

        Список абсолютно всех билетов
    """
    tickets = {}

    if language == "en":
        cursor.execute("SELECT * FROM ticketairen")
        answer = cursor.fetchall()

        for i in answer:
            tickets[i[0]] = {"Start": i[1],
                             "End": i[2],
                             "Start-Date": i[3].isoformat(),
                             "End-Date": i[4].isoformat(),
                             "Start-Time": i[5].isoformat(),
                             "End-Time": i[6].isoformat(),
                             "Price": i[7]}

        answer = tickets.values()
    else:
        cursor.execute("SELECT * FROM ticketairru")
        answer = cursor.fetchall()

        for i in answer:
            tickets[i[0]] = {"Start": i[1],
                             "End": i[2],
                             "Start-Date": i[3].isoformat(),
                             "End-Date": i[4].isoformat(),
                             "Start-Time": i[5].isoformat(),
                             "End-Time": i[6].isoformat(),
                             "Price": i[7]}
        
        answer = tickets.values()

    return list(answer)


def all_marshutrs_train():
    """Функция получения всех маршрутов ЖД"""

    return list(marshrut_train.values())


def all_marshurts_bus():
    """Функция получения всех маршрутов автобусов"""

    return list(marshrut_bus.values())


def insert_marshrut_avia(newMarshrut):
    """Функция добаления нового маршрута авиа"""


    cursor.execute(f"""SELECT id
                      FROM ticketairen
                      WHERE start = '{newMarshrut['en']['start']}' AND 
                            "end" = '{newMarshrut['en']['end']}' AND
                            "startDate" = '{datetime.strptime(newMarshrut['en']['start-date'], '%Y-%m-%d').date()}' AND
                            "endDate" = '{datetime.strptime(newMarshrut['en']['end-date'], '%Y-%m-%d').date()}' AND
                            "price" = '{newMarshrut['en']['price']}'""")
    answer_en = cursor.fetchall()

    cursor.execute(f"""SELECT id
                      FROM ticketairru
                      WHERE start = '{newMarshrut['ru']['start']}' AND 
                            "end" = '{newMarshrut['ru']['end']}' AND
                            "startDate" = '{datetime.strptime(newMarshrut['ru']['start-date'], '%Y-%m-%d').date()}' AND
                            "endDate" = '{datetime.strptime(newMarshrut['ru']['end-date'], '%Y-%m-%d').date()}' AND
                            "price" = '{newMarshrut['ru']['price']}'""")
    answer_ru = cursor.fetchall()

    if len(answer_en) > 0 and len(answer_ru) > 0:
        abort(400, "Маршрут уже создан")

    if len(answer_ru) == 0 and len(answer_en) > 0:
        try:
            cursor.execute("SELECT MAX(id) FROM ticketairru")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1

            cursor.execute(f"""INSERT INTO ticketairru(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
                                VALUES({id}, '{newMarshrut['ru']['start']}', '{newMarshrut['ru']['end']}',
                                '{datetime.strptime(newMarshrut['ru']['start-date'], '%Y-%m-%d').date()}', '{datetime.strptime(newMarshrut['ru']['end-date'], '%Y-%m-%d').date()}',
                                '{newMarshrut['ru']['start-time']}', '{newMarshrut['ru']['end-time']}',
                                {newMarshrut['ru']['price'].split(",")[0]})""")

            cn.commit()
            return newMarshrut['ru'], 201
        except Exception as e:
            abort(400, f"Ошибка добавления данных! Ошибка: {e}")
    
    if len(answer_ru) > 0 and len(answer_en) == 0:
        try:
            cursor.execute("SELECT MAX(id) FROM ticketairen")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1

            cursor.execute(f"""INSERT INTO ticketairru(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
                                VALUES({id}, '{newMarshrut['en']['start']}', '{newMarshrut['en']['end']}',
                                '{datetime.strptime(newMarshrut['en']['start-date'], '%Y-%m-%d').date()}', '{datetime.strptime(newMarshrut['en']['end-date'], '%Y-%m-%d').date()}',
                                '{newMarshrut['en']['start-time']}', '{newMarshrut['en']['end-time']}',
                                {newMarshrut['en']['price'].split(",")[0]})""")
            cn.commit()
            return newMarshrut['en'], 201
        except Exception as e:
            abort(400, f"Ошибка добавления данных! Ошибка: {e}")
    else:
        try:
            cursor.execute("SELECT MAX(id) FROM ticketairru")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1
            cursor.execute(f"""INSERT INTO ticketairru(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
                                VALUES({id}, '{newMarshrut['ru']['start']}', '{newMarshrut['ru']['end']}',
                                '{datetime.strptime(newMarshrut['ru']['start-date'], '%Y-%m-%d').date()}', '{datetime.strptime(newMarshrut['ru']['end-date'], '%Y-%m-%d').date()}',
                                '{newMarshrut['ru']['start-time']}', '{newMarshrut['ru']['end-time']}',
                                {newMarshrut['ru']['price'].split(",")[0]})""")

            cursor.execute("SELECT MAX(id) FROM ticketairen")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1
            cursor.execute(f"""INSERT INTO ticketairen(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
                                VALUES({id}, '{newMarshrut['en']['start']}', '{newMarshrut['en']['end']}',
                                '{datetime.strptime(newMarshrut['en']['start-date'], '%Y-%m-%d').date()}', '{datetime.strptime(newMarshrut['en']['end-date'], '%Y-%m-%d').date()}',
                                '{newMarshrut['en']['start-time']}', '{newMarshrut['en']['end-time']}',
                                {newMarshrut['en']['price'].split(",")[0]})""")
            cn.commit()
            return newMarshrut, 201
        except Exception as e:
            abort(400, f"Ошибка добавления данных! Ошибка: {e}")



def insert_marshrut_train(newMarshrut):
    """Функция добаления нового маршрута ЖД"""

    for key, value in marshrut_train.items():
        if value["en"] == newMarshrut['en'] and value['ru'] == newMarshrut['ru']:
            abort(400, "Маршрут уже создан")

    keys = int(list(marshrut_train.keys())[-1]) + 1

    marshrut_train[keys] = {
            "en": newMarshrut['en'],
            "ru": newMarshrut['ru']
        }
    return marshrut_train[keys], 201


def insert_marshrut_bus(newMarshrut):
    """Функция добаления нового маршрута Автобус"""

    for key, value in marshrut_bus.items():
        if value["en"] == newMarshrut['en'] and value['ru'] == newMarshrut['ru']:
            abort(400, "Маршрут уже создан")

    keys = int(list(marshrut_bus.keys())[-1]) + 1

    marshrut_bus[keys] = {
            "en": newMarshrut['en'],
            "ru": newMarshrut['ru']
        }
    return marshrut_bus[keys], 201


def filterTicket_avia(ticket):
    """Функция на тикеты по критерию"""

    language = ["ru", "en"]

    if ticket['language'] not in language:
        abort(
            404, f"Язык {ticket['language']} не найден"
        )

    tickets = []
    for key, value in marshrut_air.items():
        if ticket['start'] == value[ticket['language']]['start'] and ticket['end'] == value[ticket['language']]['end'] and ticket['date'] == value[ticket['language']]['start-date']:
            tickets.append(value[ticket['language']])  

    if len(tickets) > 0:
        return tickets
    else:
        abort(404, "Билетов по заданным параметрам не найдено")


def filterTicket_train(ticket):
    """Функция на тикеты по критерию"""

    language = ["ru", "en"]

    if ticket['language'] not in language:
        abort(
            404, f"Язык {ticket['language']} не найден"
        )

    tickets = []
    for key, value in marshrut_train.items():
        if ticket['start'] == value[ticket['language']]['start'] and ticket['end'] == value[ticket['language']]['end'] and ticket['date'] == value[ticket['language']]['start-date']:
            tickets.append(value[ticket['language']])  

    if len(tickets) > 0:
        return tickets
    else:
        abort(404, "Билетов по заданным параметрам не найдено")


def filterTicket_bus(ticket):
    """Функция на тикеты по критерию"""

    language = ["ru", "en"]

    if ticket['language'] not in language:
        abort(
            404, f"Язык {ticket['language']} не найден"
        )

    tickets = []
    for key, value in marshrut_bus.items():
        if ticket['start'] == value[ticket['language']]['start'] and ticket['end'] == value[ticket['language']]['end'] and ticket['date'] == value[ticket['language']]['start-date']:
            tickets.append(value[ticket['language']])  

    if len(tickets) > 0:
        return tickets
    else:
        abort(404, "Билетов по заданным параметрам не найдено")


def update_way_avia(idWay, idWa):
    """Обновлнение маршрута"""

    if idWay not in marshrut_air:
        abort(404, "Билет не найден")

    marshrut_air[idWay] = {"en": idWa['en'], "ru": idWa['ru']}
    return marshrut_air[idWay]


def update_way_train(idWay, idWa):
    """Обновлнение маршрута"""

    if idWay not in marshrut_train:
        abort(404, "Билет не найден")

    marshrut_train[idWay] = {"en": idWa['en'], "ru": idWa['ru']}
    return marshrut_train[idWay]


def update_way_bus(idWay, idWa):
    """Обновлнение маршрута"""

    if idWay not in marshrut_bus:
        abort(404, "Билет не найден")

    marshrut_bus[idWay] = {"en": idWa['en'], "ru": idWa['ru']}
    return marshrut_bus[idWay]