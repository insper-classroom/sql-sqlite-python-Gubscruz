import sqlite3

conn = sqlite3.connect('database_alunos.db')
cursor = conn.cursor()

# Deleta a tabela "Estudantes" se ela já existir
cursor.execute("DROP TABLE IF EXISTS Estudantes")

# Recria a tabela "Estudantes"
cursor.execute("""
CREATE TABLE Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoIngresso INTEGER
);
""")
# Inserção dos registros
estudantes = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022),
]

cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, AnoIngresso)
VALUES (?, ?, ?);
""", estudantes)

conn.commit()

# Seleção e impressão de todos os estudantes
cursor.execute('SELECT * FROM Estudantes')
print("Todos os estudantes:")
for registro in cursor.fetchall():
    print(registro)

# Filtrar e mostrar os estudantes que ingressaram entre 2019 e 2020
cursor.execute('SELECT * FROM Estudantes WHERE AnoIngresso BETWEEN 2019 AND 2020')
print("\nEstudantes que ingressaram entre 2019 e 2020:")
for registro in cursor.fetchall():
    print(registro)

# Atualizar o "Ano de Ingresso" de Ana Silva, por exemplo
cursor.execute('UPDATE Estudantes SET AnoIngresso = ? WHERE Nome = ?', (2023, 'Ana Silva'))
conn.commit()

# Seleção e impressão de todos os estudantes novamente

cursor.execute('DELETE FROM Estudantes WHERE ID = ?', ('4',))
conn.commit()
cursor.execute('SELECT * FROM Estudantes')
print("\nTodos os estudantes (após atualização):")
for registro in cursor.fetchall():
    print(registro)

cursor.execute('SELECT * FROM Estudantes WHERE Curso = ? AND Anoingresso >= ?', ('Computação', 2019))
conn.commit()
print("\nEstudantes de CComputação pos 2019:")
for registro in cursor.fetchall():
    print(registro)

cursor.execute('UPDATE Estudantes SET AnoIngresso = ? WHERE Curso = ?', (2018, 'Computação'))
conn.commit()
cursor.execute('SELECT * FROM Estudantes')
print("\nEstudantes de CComputação atualizados:")
for registro in cursor.fetchall():
    print(registro)

conn.close()
