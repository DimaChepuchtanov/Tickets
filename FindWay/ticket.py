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
    def __init__(self, url) -> None:
        self.url = url

    def filterMarshrut(self, data):
        """Функция поиска маршрута
        
        Пример входных данных:
        data = {
                "date": "2024-02-01",
                "end": "Москва",
                "language": "ru",
                "start": "Пермь"
            }
        """
        try:
            answer = req.post("http://127.0.0.1:8080/api/way/{wayes}", json=data)
            return {"status": answer.json()}

        except Exception as e:
            return {"status": f"Ошибка запроса: {e}"}
    
