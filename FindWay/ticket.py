# -*- coding: utf-8 -*-
"""
:authors: Dima Chepushtanov
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2024 Ymka
"""

from .config import language, ApiUrl as url, headers as head
import requests as req
import json


class Tickets():
    def __init__(self) -> None:
        pass

    def showAllTickets(self, transport):
        """Возврат билетов на транспорт

        Транспорт указывается в строгом формате:
            Самолет -> "avia"\n
            Поезд   -> "train"\n
            Автобус -> "bus"\n

        Ошибки:
            Любой ввод неверных данных или данных не в нужном формате
            приведут к ошибке.
        """

        try:
            answer = req.get(f"{url}/{transport}/{language}")
            return {"status": answer.status_code,
                    "title": answer.json()}
        except Exception as e:
            return {"status": 404,
                    "title": f"Ошибка запроса: {e}"}

    def showFilterTicket(self, transport, **kwargs):
        """Функция поиска билетов по заданным параметрам"""
        try:
            payload = kwargs['params']
            answer = req.post(f"{url}/{transport}", json=payload, headers=head)
            return {"status": answer.status_code,
                    "title": answer.json()}

        except Exception as e:
            return {"status": 404,
                    "title": f"Ошибка запроса: {e}"}

    def createNewTicket(self, transport, **kwargs):
        """Создание нового маршрута движения"""
        try:
            payload = kwargs['params']
            answer = req.put(f"{url}/{transport}", json=payload, headers=head)
            return {"status": answer.status_code,
                    "title": answer.json()}

        except Exception as e:
            return {"status": 404,
                    "title": f"Ошибка запроса: {e}"}

    def updateOldTicket(self, transport, id, **kwargs):
        """Изменение данных по id"""

    def createAdaptiveWay(self):
        """Динамический подбор пути из точки А в точку Б
            По заданным критериям: 
                1) Без пересадок
                2) До двух пересадок
                3) Самый быстрый маршрут
                4) Самый дешевый маршрут
                5) Разный вид транспорта
                6) Возможность ездить с животными
        """


if __name__ == "__main__":
    tt = Tickets()
    print(tt.createNewTicket("train", params={
  "en": {
    "end": "string",
    "end-date": "2023-09-20",
    "end-time": "15:30",
    "price": "120",
    "start": "string",
    "start-date": "2023-09-20",
    "start-time": "15:30"
  },
  "ru": {
    "end": "string",
    "end-date": "2023-09-20",
    "end-time": "15:30",
    "price": "120",
    "start": "string",
    "start-date": "2023-09-20",
    "start-time": "15:30"
  }
}))