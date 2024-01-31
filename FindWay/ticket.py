# -*- coding: utf-8 -*-
"""
:authors: Dima Chepushtanov
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2024 Ymka
"""

from config import language, ApiUrl as url
import requests as req


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
            answer = answer.json()
            return {"status": answer['status'],
                    "title": answer['title']}
        except Exception as e:
            return {"status": 404,
                    "title": f"Ошибка запроса: {e}"}

    def showFilterTicket(self, transport, **params):
        """Функция поиска билетов по заданным параметрам"""


if __name__ == "__main__":
    tt = Tickets()
    tt.showAllTickets("avia")        