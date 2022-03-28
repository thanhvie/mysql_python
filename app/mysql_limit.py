import mysql.connector
from utilities.common import get_env_var

env_var = get_env_var()


def get_limit():

    mydb = mysql.connector.connect(
        host=env_var[0],
        user=env_var[1],
        password=env_var[2],
        database=env_var[3]
    )

    mycursor = mydb.cursor()

    # Select the 5 first records in the "customers" table

    mycursor.execute("SELECT * FROM customers LIMIT 5")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    # Start from position 3, and return 5 records

    mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mydb.close()
