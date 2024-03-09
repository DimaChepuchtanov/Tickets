# -*- coding: utf-8 -*-
"""
:authors: Dima Chepushtanov
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2024 Ymka
"""

from .config import language, headers as head
import requests as req
import json


class User():
    def __init__(self, url):
        self.url = url

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

        try:
            reuqest = req.get(f"{self.url}/user/{FIO}").json()
        except Exception as e:
            return {"status": "Error",
                    "detail": "Сервер отверг запрос. Нет подключения"}

        if reuqest['status'] == "User Not Found":
            return {"status": "Error",
                    "detail": "Пользователь не найден"}
        else:
            return {"status": "Successful",
                    "detail": reuqest['status']}

    def link_profile(self, FIO: str) -> str:
        """Возвращает ссылку на профиль сайта пользователя"""

        try:
            reuqest = req.get(f"{self.url}/user/{FIO}").json()
        except Exception as e:
            return {"status": "Error",
                    "detail": "Сервер отверг запрос. Нет подключения"}

        if reuqest['status'] == "User Not Found":
            return {"status": "Error",
                    "detail": "Пользователь не найден"}
        else:
            return {"status": "Successful",
                    "detail": reuqest['status']['link']}
        pass

    def history_buy(self, FIO: str) -> dict:
        """Просмотр купленных билетов
        
        Входные параметры:
            * FIO - имя пользователя
        Выходные параметры: 
            * список строк, где каждая строка = последовательность билетов

        Пример выходной строки:
        ["bus12 air22 train12"]
        """

        try:
            reuqest = req.get(f"{self.url}/user/{FIO}").json()
        except Exception as e:
            return {"status": "Error",
                    "detail": "Сервер отверг запрос. Нет подключения"}

        if reuqest['status'] == "User Not Found":
            return {"status": "Error",
                    "detail": "Пользователь не найден"}
        else:
            return {"status": reuqest['status']['StoryBuy']}

    def edit_profile(self, FIO: str, edit: dict) -> bool:
        """Изменяет данные профиля

        Пользовательское изменение профиля включает в себя:
            * Изменение пола пользователя
            * Изменение возраста пользователя
            * Изменение почты пользователя

        Входные данные:
            * FIO - имя пользователя
            * eidt - словарь с измененными данными
        """

        edit['history'] = ""
        edit['post'] = ""
        try:
            reuqest = req.put(f"{self.url}/user/{FIO}", json=edit).json()
        except:
            return {"status": "Error",
                    "detail": "Сервер отверг запрос. Нет подключения"}
        
        if reuqest['status'] == "Данные не обновлены":
            return {"status": "Error",
                    "detail": "Ошибка сервера, данные не были обновены"}
        elif reuqest['status'] == "User Not Found":
            return {"status": "Error",
                    "detail": "Пользователь не был найден"}
        else:
            return {"status": "Saccessful",
                    "detail": "Пользовательские данные были обновлены"}

    def history_post(self, FIO: str) -> dict:
        """Просмотр истории постов от пользователя

        Входные параметры:
            * FIO - имя пользователя
        Выходные параметры: 
            * список пользовательских постов
        """

        try:
            reuqest = req.get(f"{self.url}/user/{FIO}").json()
        except Exception as e:
            return {"status": "Error",
                    "detail": "Сервер отверг запрос. Нет подключения"}

        if reuqest['status'] == "User Not Found":
            return {"status": "Error",
                    "detail": "Пользователь не найден"}
        else:
            return {"status": reuqest['status']['post']}

    def create_post(self, FIO: str, post: dict) -> dict:
        """Создание поста

        Входные параметры:
            * FIO - имя пользователя
            * post - словарь параметров
        """

        try:
            post = req.post(f"{self.url}/post/create/{FIO}", data=post).json()
        except:
            return {"status": "Error",
                    "detail": "Сервер отверг запрос. Нет подключения"}

        if post['status'] == "Ошибка обновления, проверьте корректность данных и повторите попытку":
            return {"status": "Error",
                    "detail": "Ошибка сервера, повторите попытку"}
        else:
            return {"status": "Пост создан. Данные обновлены"}

    def edit_post(self, id: int, post: dict) -> dict:
        """Создание поста

        Входные параметры:
            * FIO - имя пользователя
            * post - словарь параметров
        """

        try:
            post = req.post(f"{self.url}/post/edit/{id}", data=post).json()
        except:
            return {"status": "Error",
                    "detail": "Сервер отверг запрос. Нет подключения"}

        if post['status'] == "Ошибка обновления, проверьте корректность данных и повторите попытку":
            return {"status": "Error",
                    "detail": "Ошибка сервера, повторите попытку"}
        else:
            return {"status": "Данные обновлены"}
    
    def delete_post(self, id: int) -> dict:
        """Удаление поста

        Входные параметры:
            * FIO - имя пользователя
            * post - словарь параметров
        """

        try:
            post = req.get(f"{self.url}/post/delete/{id}").json()
        except:
            return {"status": "Error",
                    "detail": "Сервер отверг запрос. Нет подключения"}

        if post['status'] == "Ошибка обновления, проверьте корректность данных и повторите попытку":
            return {"status": "Error",
                    "detail": "Ошибка сервера, повторите попытку"}
        else:
            return {"status": "Пост удален"}


if __name__ == "__main__":
    user = User()
    print(user.profile_info("Иванов Иван Иванович"))