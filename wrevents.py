import sqlite3


def printevents():
    a = []
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    result = cur.execute("""SELECT data, time, zagolovok FROM events""").fetchall()
    print(result)
    for i in range(len(result)):
        a.append(str(result[i])[2:-1])
    a = str(a)
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.replace("'", "")
    a = a.replace(",", "\n")
    a = a.replace(" ", "")
    return a
    con.close()
