# -*- coding: utf-8 -*-
"""
:authors: Dima Chepushtanov
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2024 Ymka 1q2w3e4r
"""

from .ticket import Tickets
from .user import User
import typing


class Main(Tickets, User):
    def __init__(self, url):
        self.url = url

def auth(url: str, token: str) -> str:
    """Авторизация библиотеки FindWayLib
    Авторизация происходит через получение авторизационного url
    на который будет в последствие отправляться запрос. 
    Доступ один на 24 часа. Совместо с url будет токен
    """

    auth_token = "1"
    auth_url = "http://127.0.0.1:8000/api"

    if auth_token == token and auth_url == url:
        return Main(url)
    elif auth_token == token and auth_url != url:
        return "Ошибка коннекта"




__author__ = 'Dima Chepushtanov'
__version__ = '2.5.34'
__email__ = 'dachepushtanov@edu.hse.ru'

