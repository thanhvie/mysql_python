import mysql.connector
from utilities.common import get_env_var


def create_database():

    env_var = get_env_var()

    mysql_connection = mysql.connector.connect(
        host=env_var[0],
        user=env_var[1],
        password=env_var[2]
    )

    my_cursor = mysql_connection.cursor()

    database_name = env_var[3]
    sql_query = "CREATE DATABASE " + database_name
    my_cursor.execute(sql_query)

    my_cursor.execute("SHOW DATABASES")

    for x in my_cursor:
        print(x)

    mysql_connection.close()
