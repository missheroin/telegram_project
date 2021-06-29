import sqlite3

def writenote(all):
    a = all.split('-')
    zg = a[1]
    op = a[-1]
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    result = cur.execute("""INSERT INTO notes (zagolovok, opisanie)
                         VALUES (?, ?)""", (zg, op)).fetchall()
    con.commit()
    for elem in result:
        print(elem)
    con.close()
    print(zg, op)
