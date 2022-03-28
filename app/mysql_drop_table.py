import mysql.connector
from utilities.common import get_env_var

env_var = get_env_var()


def drop_table():

    mydb = mysql.connector.connect(
        host=env_var[0],
        user=env_var[1],
        password=env_var[2],
        database=env_var[3]
    )

    mycursor = mydb.cursor()

    sql = "DROP TABLE IF EXISTS customers"

    mycursor.execute(sql)

    mydb.close()
