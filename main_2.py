import sqlite3
from db_utils import *


conn = sqlite3.connect('database_alunos.db')
cursor = conn.cursor()

create_table(cursor, "Estudantes", "ID INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT NOT NULL, Curso TEXT NOT NULL, AnoIngresso INTEGER")

estudantes = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022),
]
insert(cursor, "Estudantes", "Nome, Curso, AnoIngresso", "?, ?, ?", estudantes)
conn.commit()


registros = select_all(cursor, "Estudantes")
print("Todos os estudantes:")
for registro in registros:
    print(registro)


cursor.execute('SELECT * FROM Estudantes WHERE AnoIngresso BETWEEN 2019 AND 2020')
print("\nEstudantes que ingressaram entre 2019 e 2020:")
for registro in cursor.fetchall():
    print(registro)


update(cursor, "Estudantes", "AnoIngresso", "Nome", (2023, 'Ana Silva'))

delete(cursor, "Estudantes", 4)


registros = select_all(cursor, "Estudantes")
print("\nTodos os estudantes (após atualização):")
for registro in registros:
    print(registro)


cursor.execute('SELECT * FROM Estudantes WHERE Curso = ? AND Anoingresso >= ?', ('Computação', 2019))
print("\nEstudantes de Computação pós 2019:")
for registro in cursor.fetchall():
    print(registro)

update(cursor, "Estudantes", "AnoIngresso", "Curso", (2018, 'Computação'))


registros = select_all(cursor, "Estudantes")
print("\nEstudantes de Computação atualizados:")
for registro in registros:
    print(registro)


conn.close()
