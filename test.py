
import sqlite3

connection = sqlite3.connect('diary.db')

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
print('Ce trebuie să facem?')

while True:
    x = input('Castor> ')
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
        cursor.execute('select * from progress;')
        y = cursor.fetchall()

        if len(y) == 0:
            print('Datele inca nu au fost adaugate')
        else:
            for i in y:
                print('id={} {} - {}'.format(i[0], i[1], i[2]))

    elif x[:3] == 'add':
        # add m 10
        scode = x[4]
        subject = None
        if scode == 'm':
            subject = 'Matematica'
        elif scode == 'g':
            subject = 'Geografia'
        elif scode == 'i':
            subject = 'Informatica'
        else:
            print('Disciplina nu a fost adaugata')
            continue

        if len(x) == 8:
            grade = x[6] + x[7]
        else:
            grade = x[6]
        
        if int(grade) > 10: 
            print('Nota nu trebuie să fie mai mare decât 10.')
        else:
            cursor.execute('insert into progress(subject, grade) values (?, ?)', (subject, grade))
            connection.commit()

        print('ok')
    
   
connection.close()
print('La revedere! Vă aștept din nou!')
