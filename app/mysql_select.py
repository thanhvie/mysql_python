import mysql.connector
from utilities.common import get_env_var

env_var = get_env_var()


def get_select():

    mydb = mysql.connector.connect(
        host=env_var[0],
        user=env_var[1],
        password=env_var[2],
        database=env_var[3]
    )

    mycursor = mydb.cursor()

    # select all items in table
    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    # select columns

    mycursor.execute("SELECT name, address FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    # fetchone

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchone()

    print(myresult)

    mydb.close()
