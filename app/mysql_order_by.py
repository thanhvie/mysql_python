import mysql.connector
from utilities.common import get_env_var

env_var = get_env_var()


def get_order_by():

    mydb = mysql.connector.connect(
        host=env_var[0],
        user=env_var[1],
        password=env_var[2],
        database=env_var[3]
    )

    mycursor = mydb.cursor()

    # Sort the result alphabetically by name

    sql = "SELECT * FROM customers ORDER BY name"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    # Sort the result reverse alphabetically by name

    sql = "SELECT * FROM customers ORDER BY name DESC"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mydb.close()
