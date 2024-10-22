import sqlite3

db = sqlite3.connect('autotwo.db')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS autotwo(
               marka TEXT,
               color TEXT,
               year INTEGER,
               price INTEGER,
               probeg INTEGER,
               sellers_num TEXT,
               photo TEXT
               )
''')


async def add_to_db(marka,color,year,price,probeg,sellers_num,photo):
    cursor.execute('''
INSERT INTO autotwo(marka,color,year,price,probeg,sellers_num,photo)
                   VALUES(?,?,?,?,?,?,?)

''',(marka,color,year,price,probeg,sellers_num,photo))
    db.commit()
    

# add_to_db(marka='Cobalt',color='black',year=2023,price=12000,probeg=56000,sellers_num='+998919277777',
#            photo='AgACAgIAAxkBAAIETWcOPHo-_2rSPaZDDIzqj2Lbfa8DAALY4jEb9DJ4SLJwH6p5Ae7_AQADAgADcwADNgQ')


async def show_autos():
    cursor.execute('SELECT * FROM autotwo')
    return cursor.fetchall()

#print(show_autos())
