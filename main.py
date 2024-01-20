# -*- coding: utf-8 -*-
"""
:authors: Dima Chepushtanov
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2024 Ymka
"""

import requests
import re
import json
from pprint import pprint
import vk_api
from typing import Any, Callable, List, Optional, Union


class Ticker():
    def __init__(self) -> None:
        pass

    """Блок работы с профилем """
    def __chekAplpa(self, text: str) -> bool:
        """Проверка текста на наличие чисел"""

        number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for i in text:
            if i in number:
                return True

        return False

    def profile_info(self, FIO: str) -> dict:
        """Возврат информации о пользователе

            FIO: строка содержащая Фамилию Имя и Отчество
                !Данные должны быть в строгом порядке, иначе данные будут в неверном формате отображены
        """

        if self.__chekAplpa(FIO):
            return {"status_code": "400",
                    "title": "Ошибка данных",
                    "detail": "Ошибка введенных данных. Обнаружены цифры"}

        try:
            reuqest = requests.get(f"http://127.0.0.1:8000/api/user/{FIO}")
        except:
            return {"status_code": "500",
                    "title": "Ошибка сервера",
                    "detail": "Сервер отверг запрос. Нет подключения"}

        status = reuqest.status_code
        detail = reuqest.json()

        if status == 404:
            return {
                "status_code": status,
                "title": "Пользователь не найден",
                "detail": f"Пользователь {FIO} был не найден в базе"  
            }
        else:
            return {
                "status_code": status,
                "title": "Пользователь найден",
                "detail": detail  
            }

    def link_profile(self, FIO: str) -> str:
        """Возвращает ссылку на профиль сайта пользователя""" 
        pass

    def history_buy(self, FIO: str) -> dict:
        """Возвращает список купленных билетов пользователя"""

        if self.__chekAplpa(FIO):
            return {"status_code": "400",
                    "title": "Ошибка данных",
                    "detail": "Ошибка введенных данных. Обнаружены цифры"}

        try:
            reuqest = requests.get(f"http://127.0.0.1:8000/api/user/{FIO}")
        except Exception as e:
            return {"status_code": "500",
                    "title": "Ошибка сервера",
                    "detail": "Сервер отверг запрос. Нет подключения"}

        status = reuqest.status_code
        detail = reuqest.json()

        if status == 404:
            return {
                "status_code": status,
                "title": "Пользователь не найден",
                "detail": f"Пользователь {FIO} был не найден в базе"  
            }
        else:
            return {
                "status_code": status,
                "title": "Пользователь найден",
                "detail": detail['storyBuy']
            }

    def edit_profile(self, FIO: str, edit: dict) -> bool:
        """Изменяет данные профиля"""

        pass

    def create_profile(self, FIO: str) -> bool:
        """Создание профиля пользователя"""

        if self.__chekAplpa(FIO):
            return {"status_code": "400",
                    "title": "Ошибка данных",
                    "detail": "Ошибка введенных данных. Обнаружены цифры"}

        try:
            reuqest = requests.post(f"http://127.0.0.1:8000/api/user",
                                    data=json.dumps({"FIO": FIO}),
                                    headers={'Content-Type': 'application/json'})
        except:
            return {"status_code": "500",
                    "title": "Ошибка сервера",
                    "detail": "Сервер отверг запрос. Нет подключения"}

        status = reuqest.status_code
        detail = reuqest.json()

        if status == 404:
            return {
                "status_code": status,
                "title": "Пользователь не создан",
                "detail": f"Пользователь {FIO} не был создан"
            }
        else:
            return {
                "status_code": status,
                "title": "Пользователь создан",
                "detail": detail
            }

    def find_profile(self) -> dict:
        """Возвращает весь список пользователей"""
        try:
            reuqest = requests.get(f"http://127.0.0.1:8000/api/user")
        except:
            return {"status_code": "500",
                    "title": "Ошибка сервера",
                    "detail": "Сервер отверг запрос. Нет подключения"}

        status = reuqest.status_code
        detail = reuqest.json()

        return {
                "status_code": status,
                "title": "Список пользователей",
                "detail": detail
            }


if __name__ == "__main__":
    tiket = Ticker()
    # print(tiket.profile_info("Иванов Иван Иванович"))
    pprint(tiket.find_profile())