# -*- coding: utf-8 -*-
"""
:authors: Dima Chepushtanov
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2024 Ymka
"""

from typing import Optional
import requests as rq
import secrets


"""
Status Table:
    Error = Любая ошибка
    Active = Активный сеанс
    ////

"""


class Main():
    def __init__(self):
        from .ticket import Tickets
        from .user import User

        self.user = User("http://127.0.0.1:8080/api")
        self.ticket = Tickets()


def auth(id: Optional[int] = None, token: Optional[str] = None) -> str:
    """Авторизация библиотеки FindWayLib

    Работа библиотеки происходит с авторизационными данными\n
    ::params
        * token -> ключ авторизации
        * user -> ID пользователя
    """

    if id is None and token is None:
        return {"status": "Error",
                "detail": "Не указаны пользовательские данные и данные токена"}

    if id is None or token is None:
        return {"status": "Error",
                "detail": "Не указан один из необходимых данных"}

    check = rq.get(f"http://127.0.0.1:8080/api/token/check/{id}").json()
    if check['Status'] == "Not Found":
        return {"status": "Error",
                "detail": "Указанный пользователь не найден"}
    elif check['Status'] == "Expired":
        return {"status": "Error",
                "detail": """Активный токен пользователя устарел.
                             Обновите токен на сайте"""}  # УКАЗАТЬ ССЫЛКУ

    else:
        check = rq.get(f"http://127.0.0.1:8080/api/token/showToken/{id}").json()
        if secrets.compare_digest(token, check['Status']):
            return Main()
        else:
            return {"status": "Error",
                    "detail": "Указаный токен не найден"}


__author__ = 'Dima Chepushtanov'
__version__ = '2.5.34'
__email__ = 'dachepushtanov@edu.hse.ru'

