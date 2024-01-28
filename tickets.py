# -*- coding: utf-8 -*-
"""
:authors: Dima Chepushtanov
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2024 Ymka
"""

from flask import abort
from datetime import datetime
from database import connect


"""Данные по Авиабилетам"""


ticket_air = {
    "1": {
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
    "2": {
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


def all_airTicket(lanaguage):
    """Функция на все авиа тикеты"""
    return list(ticket_air.values())


def filterTicket(ticket):
    """Функция на тикеты по критерию"""

    language = ["ru", "en"]

    if ticket['language'] not in language:
        abort(
            404, f"Language {ticket['language']} not find // Язык {ticket['language']} не найден"
        )

    tickets = []
    for key, value in ticket_air.items():
        if ticket['start'] == value[ticket['language']]['start'] and ticket['end'] == value[ticket['language']]['end'] and ticket['date'] == value[ticket['language']]['start-date']:
            tickets.append(value[ticket['language']])  

    if len(tickets) > 0:
        return tickets
    else:
        abort(
            404, f"Person with last name not found // Билет не найден"
        )


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM ticketairen")
    
    ticket_air = {}


    
