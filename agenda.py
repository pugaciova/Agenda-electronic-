# help – lista de comenzi
# Folosim print ca să afișăm lista de comenzi

# show - arată lista de note
# cursor.execute('select * from progress;')

# add [cod materie] [nota] - adaugă înregistrare
#   1. verificăm codul disciplinei
#   2. facem insert cu valori de la utiliz.
# Codurile materiilor:
# m - Matematică
# g - Geometrie
# i - Informatică

# update [id] [nota nouă] - actualizează nota
# cursor.execute('update......')

# del [id] - șterge înregistrare
# cursor.execute('delete......')

# exit - ieșire
# Folosim break 

# Biblioteca cu ajutorul căreia putem lucra cu baza de date SQLite
import sqlite3
# Ne conectăm la baza de date. Dacă fișierul lipsește, acesta va fi creat automat.
connection = sqlite3.connect('diary.db')
# Creăm un cursor. Prin acesta putem executa comenzi SQL.
cursor = connection.cursor()

sql = '''
create table if not exists progress
(
id integer primary key autoincrement,
subject text,
grade integer
);
'''
cursor.execute(sql)
connection.commit()

print('Salut de la Castor!')
print('Ce vreți să faceți?')

while True:
    x = input('Castor>')
    if x == 'exit':
        break
    if x == 'help':
        print("help – lista de comenzi")
        print("show - arată lista de note")
        print("add [cod materie] [nota] - adaugă înregistrare")
        print("Codurile materiilor:")
        print("m - Matematică")
        print("g - Geometrie")
        print("i - Informatică")
        print("update [id] [nota nouă] - actualizează nota")
        print("del [id] - șterge înregistrare")
        print("exit - ieșire")

    elif x == 'show':
        cursor.execute('Select * from progress')
        y = cursor.fetchall()
        # y = [[1,'m',10], [2,'m',9]....]

        if len(y) == 0:
            print('Datele încă nu sunt!')
        else:
            for i in y: # i1 =[1,'m',10], i2 =[2,'m',9]....
                print('id ={} {} - {}'.format(i[0],i[1],i[2]))

    elif x[0:3] == 'add':
        scode = x[4]
        subject = None
        if scode == 'm':
            subject = 'Matematica'
        elif scode == 'g':
            subject = 'Geografia'
        elif scode == 'i':
            subject = 'Informatica'
        else:
            print('Disciplina încă nu este în lista')
            continue 
        
        if len(x) == 8:
            grade = x[6] + x[7] # '1' + '0' = '10'
        else:
            grade = x[6]
        
        cursor.execute('insert into progress(subject,grade) values (?,?)',(subject,grade))
        connection.commit()
        print('ok')

connection.close()