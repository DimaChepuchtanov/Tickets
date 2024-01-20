# -*- coding: utf-8 -*-
"""
:authors: Dima Chepushtanov
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2024 Ymka
"""

import psycopg2


def create_connetion():
    """Функция поключения к базе"""

    connect = psycopg2.connect(dbname="Ticker", user="postgres", password="1q2w3e4r")
    
    return connect

if __name__ == "__main__":
    print(create_connetion())