import mysql.connector


def create_database(host: str, username: str, password: str, database_name: str):

    dataBase = mysql.connector.connect(
        host=host,
        user=username,
        passwd=password
    )
    cursor_Obj = dataBase.cursor()
    cursor_Obj.execute(f"CREATE DATABASE {database_name}")

    print('All done!!!')


if __name__ == '__main__':

    host = 'localhost'
    username = 'root'
    password = 'root'
    db_name = 'CRM_db'

    create_database(host, username, password, db_name)
