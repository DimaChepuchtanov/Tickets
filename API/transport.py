# Модуль API для билетов
#
# Разделы для билетов РЖД, самолет и автобус
#

from flask import abort
from datetime import datetime

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



def all_marshurts_avia():
    """Функция получения всех маршрутов авиа"""

    return list(marshrut_air.values())


def all_marshutrs_train():
    """Функция получения всех маршрутов ЖД"""

    return list(marshrut_train.values())


def all_marshurts_bus():
    """Функция получения всех маршрутов автобусов"""

    return list(marshrut_bus.values())


def insert_marshrut_avia(newMarshrut):
    """Функция добаления нового маршрута авиа"""

    for key, value in marshrut_air.items():
        if value["en"] == newMarshrut['en'] and value['ru'] == newMarshrut['ru']:
            abort(400, "Маршрут уже создан")

    keys = int(list(marshrut_air.keys())[-1]) + 1

    marshrut_air[keys] = {
            "en": newMarshrut['en'],
            "ru": newMarshrut['ru']
        }
    return marshrut_air[keys], 201


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