import mysql.connector as connector
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from model.user import User

hostname = 'mysql.padawans.dev' 
username = 'padawans' 
password = 'OTE2020' 
database = 'padawans' 

connection = connector.connect(
    host = hostname
    ,user = username
    ,passwd = password
    ,db = database
)
def list_all(cursor, table_name):
    sql_command = f'SELECT * from {table_name}'
    cursor.execute(sql_command)
    list_lines = cursor.fetchall()
    return list_lines
        

def list_by_id(cursor, table_name, id):
    sql_command = f'SELECT * from {table_name} where id = {id}'
    cursor.execute(sql_command)
    result = cursor.fetchone()
    return result

def create(cursor, sql_command):
    cursor.execute(sql_command)
    connection.commit()

def update(cursor,sql_command):
    cursor.execute(sql_command)
    connection.commit()

def delete(cursor, table_name, id):
    sql_command = f'DELETE FROM {table_name} where id = {id};'
    cursor.execute(sql_command)
    connection.commit()

u = User('ana_delay@olist.com','delay_russia',123215)

sql_command_insert = f'''INSERT INTO users
                    VALUES
                    (
                        0
                        ,'{u.email}'
                        ,'{u.password}'
                    )
                    ;'''

sql_command_update = f'''UPDATE users 
                    set
                    mail = '{u.email}'
                    ,password = '{u.password}'
                    where id = {u.id}; '''

cursor = connection.cursor()

# delete(cursor, 'users', 2)
update(cursor, sql_command_update)
result = list_all(cursor, 'users')
print(result)
# result = list_by_id(cursor, 'users',2)
# print(result)
connection.close()
