import sqlite3
import datetime


def writeevent(all):
    a = all.split('-')
    d = a[1].split('.')
    dt = str(datetime.date(2021, int(d[1]), int(d[0])))
    print(dt)
    t = a[2].split(':')
    tm = str(datetime.time(int(t[0]), int(t[-1]), 00))
    print(tm)
    zg = a[3]
    op = a[4]
    td = a[-1].split(':')
    tdn = str(datetime.time(int(td[0]), int(td[-1]), 00))
    print(zg, op, tdn)
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    result = cur.execute(
        """INSERT INTO events (data, time, zagolovok, opisanie, notify) 
        VALUES (?, ?, ?, ?, ?)""", (dt, tm, zg, op, tdn)).fetchall()
    con.commit()
    for elem in result:
        print(elem)
    con.close()
