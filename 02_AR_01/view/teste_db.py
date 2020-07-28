import mysql.connector as connector

def list_all(cursor, command):
    cursor.execute(sql_command)
    all_users = cursor.fetchall()
    for id, mail, password in all_users:
        print(id ,mail ,password)

def list_by_id(cursor, command):
    cursor.execute(sql_command)
    user = cursor.fetchone()
    print(user[0] ,user[1] ,user[2])  

def create(cursor, command, model):
    pass

def update(cursor, command, model):
    pass

def delete(cursor, command):
    pass

hostname = 'mysql.padawans.dev' 
username = 'padawans' 
password = 'OTE2020' 
database = 'padawans' 
sql_command = 'SELECT id, mail, password from users'

connection = connector.connect(
    host = hostname
    ,user = username
    ,passwd = password
    ,db = database
)

cursor = connection.cursor()
create(cursor, sql_command)
list_all(cursor, sql_command)


connection.close()
