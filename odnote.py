import sqlite3


def noteone(all):
    b = all.split('-')
    param = b[-1]
    a = []
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    result = cur.execute("""SELECT zagolovok, opisanie FROM notes WHERE zagolovok = ?""", (param)).fetchall()
    print(result)
    for i in range(len(result)):
        a.append(str(result[i])[2:-3])
    a = str(a)
    a = a.replace("[","")
    a = a.replace("]", "")
    a = a.replace("'", "")
    a = a.replace(",", "\n")
    a = a.replace(" ", "")
    return a
    con.close()
