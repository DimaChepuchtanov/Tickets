# -*- coding: utf-8 -*-
"""
:authors: Dima Chepushtanov
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2024 Ymka
"""

import psycopg2 as pg

connect = pg.connect(database="Ticker", user="postgres", password="1q2w3e4r")

