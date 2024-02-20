# Модуль API для билетов
#
# Разделы для билетов РЖД, самолет и автобус
#

from flask import abort
from datetime import datetime
from pprint import pprint
from database import connect as cn
from random import randint, choice
from pprint import pprint

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


def selectWay(table, start, end, before, way=None):
    before.append(start)

    if end == start:
        return before

    cursor.execute(f"""SELECT "end" FROM ticketairen WHERE start = '{start}'""")
    answer = cursor.fetchall()

    listCity = set([x[0] for x in answer])
    for i in before:
        if i in listCity:
            listCity.remove(i)


    for i in listCity:
        return selectWay(table, i, end, before)



def createMarschrut(wayes):
    """Функция создания маршрута"""

    print(wayes)
    Way = []

    start = "Moscow"
    end = "Izevsk"

    if wayes['language'] == "en":
            cursor.execute(f"""SELECT "end" FROM ticketairen WHERE start = '{wayes['start']}'""")
            answer = cursor.fetchall()

            listAnswer = set([x[0] for x in answer])
            listAnswer.remove(end)

            for way in listAnswer:
                Way.append(selectWay("ticketairen", way, wayes['end'], [wayes['start']]))
    return dateTime(Way,"airandbus")


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


def all_marshutrs_train(language):
    """Функция получения всех маршрутов ЖД"""

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


def all_marshurts_bus(language):
    """Функция получения всех маршрутов автобусов"""

    tickets = {}

    if language == "en":
        cursor.execute("SELECT * FROM ticketbusen")
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
        cursor.execute("SELECT * FROM ticketbusru")
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

    cursor.execute(f"""SELECT id
                      FROM tickettranien
                      WHERE start = '{newMarshrut['en']['start']}' AND 
                            "end" = '{newMarshrut['en']['end']}' AND
                            "startDate" = '{datetime.strptime(newMarshrut['en']['start-date'], '%Y-%m-%d').date()}' AND
                            "endDate" = '{datetime.strptime(newMarshrut['en']['end-date'], '%Y-%m-%d').date()}' AND
                            "price" = '{newMarshrut['en']['price']}'""")
    answer_en = cursor.fetchall()

    cursor.execute(f"""SELECT id
                      FROM tickettraniru
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
            cursor.execute("SELECT MAX(id) FROM tickettraniru")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1

            cursor.execute(f"""INSERT INTO tickettraniru(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
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
            cursor.execute("SELECT MAX(id) FROM tickettranien")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1

            cursor.execute(f"""INSERT INTO tickettraniru(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
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
            cursor.execute("SELECT MAX(id) FROM tickettraniru")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1
            cursor.execute(f"""INSERT INTO tickettraniru(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
                                VALUES({id}, '{newMarshrut['ru']['start']}', '{newMarshrut['ru']['end']}',
                                '{datetime.strptime(newMarshrut['ru']['start-date'], '%Y-%m-%d').date()}', '{datetime.strptime(newMarshrut['ru']['end-date'], '%Y-%m-%d').date()}',
                                '{newMarshrut['ru']['start-time']}', '{newMarshrut['ru']['end-time']}',
                                {newMarshrut['ru']['price'].split(",")[0]})""")

            cursor.execute("SELECT MAX(id) FROM tickettranien")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1
            cursor.execute(f"""INSERT INTO tickettranien(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
                                VALUES({id}, '{newMarshrut['en']['start']}', '{newMarshrut['en']['end']}',
                                '{datetime.strptime(newMarshrut['en']['start-date'], '%Y-%m-%d').date()}', '{datetime.strptime(newMarshrut['en']['end-date'], '%Y-%m-%d').date()}',
                                '{newMarshrut['en']['start-time']}', '{newMarshrut['en']['end-time']}',
                                {newMarshrut['en']['price'].split(",")[0]})""")
            cn.commit()
            return newMarshrut, 201
        except Exception as e:
            abort(400, f"Ошибка добавления данных! Ошибка: {e}")


def insert_marshrut_bus(newMarshrut):
    """Функция добаления нового маршрута Автобус"""

    cursor.execute(f"""SELECT id
                      FROM ticketbusen
                      WHERE start = '{newMarshrut['en']['start']}' AND 
                            "end" = '{newMarshrut['en']['end']}' AND
                            "startDate" = '{datetime.strptime(newMarshrut['en']['start-date'], '%Y-%m-%d').date()}' AND
                            "endDate" = '{datetime.strptime(newMarshrut['en']['end-date'], '%Y-%m-%d').date()}' AND
                            "price" = '{newMarshrut['en']['price']}'""")
    answer_en = cursor.fetchall()

    cursor.execute(f"""SELECT id
                      FROM ticketbusru
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
            cursor.execute("SELECT MAX(id) FROM ticketbusru")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1

            cursor.execute(f"""INSERT INTO ticketbusru(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
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
            cursor.execute("SELECT MAX(id) FROM ticketbusen")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1

            cursor.execute(f"""INSERT INTO ticketbusru(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
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
            cursor.execute("SELECT MAX(id) FROM ticketbusru")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1
            cursor.execute(f"""INSERT INTO ticketbusru(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
                                VALUES({id}, '{newMarshrut['ru']['start']}', '{newMarshrut['ru']['end']}',
                                '{datetime.strptime(newMarshrut['ru']['start-date'], '%Y-%m-%d').date()}', '{datetime.strptime(newMarshrut['ru']['end-date'], '%Y-%m-%d').date()}',
                                '{newMarshrut['ru']['start-time']}', '{newMarshrut['ru']['end-time']}',
                                {newMarshrut['ru']['price'].split(",")[0]})""")

            cursor.execute("SELECT MAX(id) FROM ticketbusen")
            id = cursor.fetchone()
            id = 0 if id[0] == None else id[0] + 1
            cursor.execute(f"""INSERT INTO ticketbusen(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
                                VALUES({id}, '{newMarshrut['en']['start']}', '{newMarshrut['en']['end']}',
                                '{datetime.strptime(newMarshrut['en']['start-date'], '%Y-%m-%d').date()}', '{datetime.strptime(newMarshrut['en']['end-date'], '%Y-%m-%d').date()}',
                                '{newMarshrut['en']['start-time']}', '{newMarshrut['en']['end-time']}',
                                {newMarshrut['en']['price'].split(",")[0]})""")
            cn.commit()
            return newMarshrut, 201
        except Exception as e:
            abort(400, f"Ошибка добавления данных! Ошибка: {e}")


def filterTicket_avia(ticket):
    """Функция на тикеты по критерию"""

    if ticket['language'] not in ['ru', 'en']:
        abort(
            404, f"Язык {ticket['language']} не найден"
        )

    tickets = {}
    answer = []
    
    try:
        cursor.execute(f"""SELECT * FROM ticketair{ticket['language']} WHERE 'startDate' = '{ticket['date']}' AND 'end' = '{ticket['end']}' AND 'start' = '{ticket['start']}'""") 
        
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

    except Exception as e:
        abort(404, f"Ошибка запроса, повторите запрос позднее. Ошибка: {e}")
    if len(answer) > 0:
        return answer
    else:
        abort(404, "Билетов по заданным параметрам не найдено")


def filterTicket_train(ticket):
    """Функция на тикеты по критерию"""

    if ticket['language'] not in ['ru', 'en']:
        abort(
            404, f"Язык {ticket['language']} не найден"
        )

    tickets = {}
    answer = []

    try:
        cursor.execute(f"""SELECT * FROM tickettrani{ticket['language']} WHERE 'startDate' = '{ticket['date']}' AND 'end' = '{ticket['end']}' AND 'start' = '{ticket['start']}'""") 

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

    except Exception as e:
        abort(404, f"Ошибка запроса, повторите запрос позднее. Ошибка: {e}")
    if len(answer) > 0:
        return answer
    else:
        abort(404, "Билетов по заданным параметрам не найдено")


def filterTicket_bus(ticket):
    """Функция на тикеты по критерию"""

    if ticket['language'] not in ['ru', 'en']:
        abort(
            404, f"Язык {ticket['language']} не найден"
        )

    tickets = {}
    answer = []
    
    try:
        cursor.execute(f"""SELECT * FROM ticketbus{ticket['language']} WHERE 'startDate' = '{ticket['date']}' AND 'end' = '{ticket['end']}' AND 'start' = '{ticket['start']}'""") 
        
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

    except Exception as e:
        abort(404, f"Ошибка запроса, повторите запрос позднее. Ошибка: {e}")
    if len(answer) > 0:
        return answer
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


def dateTime(travel: list, transport, language="en"):
    
    way = []

    fly = []
    train = []
    bus = []

    date = "2024-02-22"
    time = "02:00"

    
    if "air" in transport:
        for way in travel:
            for i in range(len(way)-1):
                cursor.execute(f"""SELECT id,"endDate","endTime" FROM ticketair{language} WHERE start = '{way[i]}' AND
                                                                                        "end" = '{way[i+1]}' AND
                                                                                        "startDate" = '{date}' AND
                                                                                        "startTime" > '{time}'""")
                answer = cursor.fetchall()
                for j in answer:
                    fly.append([way[i], way[i+1], j[0]])
                    date = j[1]
    
    date = "2024-02-22"
    if "bus" in transport:
        for way in travel:
            for i in range(len(way)-1):
                cursor.execute(f"""SELECT id,"endDate","endTime" FROM ticketbus{language} WHERE start = '{way[i]}' AND
                                                                                        "end" = '{way[i+1]}' AND
                                                                                        "startDate" = '{date}' AND
                                                                                        "startTime" > '{time}'""")
                answer = cursor.fetchall()
                for j in answer:
                    bus.append([way[i], way[i+1], j[0]])
                    date = j[1]


    if len(bus) == len(fly):
        typecar = ['air', 'bus']
        findWay = [[] for _ in range(len(travel))]

        for j in range(len(findWay)):
                for je in range(len(travel[j])-1):
                    for o in range(len(bus)):
                        if bus[o][0] == travel[j][je] and bus[o][1] == travel[j][je+1]:
                            findWay[j].append({"id":bus[o][2], "start": bus[o][0], "end": bus[o][1], "type": choice(typecar)})
                            bus.pop(o)
                            fly.pop(o)
                            break
        return findWay
        
        


if __name__ == "__main__":
    createMarschrut("en", "air")