# -*- coding: utf-8 -*-
"""
:authors: Dima Chepushtanov
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2024 Ymka
"""

import psycopg2 as pg
import datetime, calendar

connect = pg.connect(database="Ticker", user="postgres", password="1q2w3e4r")


if __name__ == "__main__":
    cursor = connect.cursor()
    
    num_days = calendar.monthrange(2024, 2)[1]
    days = [datetime.date(2024, 2, day) for day in range(1, num_days+1)]
    
    times = ["01:00", "05:00", "10:00", "12:00", "16:00", "18:00", "21:00", "23:00"]

    starten = ['Perm', 'Tagil', 'Moscow', 'Ekaterinburg', 'Izevsk', 'Vladivostok', 'Tumen', 'Krasnoyarsk']
    startru = ['Пермь', 'Нижний Тагил', 'Москва', 'Екатеринбург', 'Ижевск', 'Владивосток', 'Тюмень', 'Красноярск']
    table = "tickettrani"
    
    for day in days:
        for start in starten:
            for end in starten:
                if start == end:
                    continue

                for time in times:
                    cursor.execute(f"SELECT MAX(id) FROM {table}en")
                    id = cursor.fetchone()
                    id = 0 if id[0] == None else id[0] + 1

                    cursor.execute(f"""INSERT INTO {table}en(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
                                        VALUES({id}, '{start}', '{end}',
                                        '{day}', '{day + datetime.timedelta(days=1)}',
                                        '{time}', '02:00', '3000')""")
                    connect.commit()
        for start in startru:
            for end in startru:
                if start == end:
                    continue

                for time in times:
                    cursor.execute(f"SELECT MAX(id) FROM {table}ru")
                    id = cursor.fetchone()
                    id = 0 if id[0] == None else id[0] + 1

                    cursor.execute(f"""INSERT INTO {table}ru(id, start, "end", "startDate", "endDate", "startTime", "endTime", price)
                                        VALUES({id}, '{start}', '{end}',
                                        '{day}', '{day + datetime.timedelta(days=1)}',
                                        '{time}', '02:00', '3000')""")
                    connect.commit()

