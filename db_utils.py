def delete(cursor, table_name, id):
    cursor.execute(f'DELETE FROM {table_name} WHERE ID = ?', (id,))
    
def update(cursor, table_name, parameter1, parameter2, values):
    cursor.execute(f'UPDATE {table_name} SET {parameter1} = ? WHERE {parameter2} = ?', values)

def create_table(cursor, table_name, columns):
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    cursor.execute(f'CREATE TABLE {table_name} ({columns})')

def insert(cursor, table_name, columns, values, data):
    cursor.executemany(f'INSERT INTO {table_name} ({columns}) VALUES ({values})', data)

def select_all(cursor, table_name):
    cursor.execute(f'SELECT * FROM {table_name}')
    return cursor.fetchall()
