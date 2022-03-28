import mysql.connector
from utilities.common import get_env_var

env_var = get_env_var()


def get_update():

    mydb = mysql.connector.connect(
        host=env_var[0],
        user=env_var[1],
        password=env_var[2],
        database=env_var[3]
    )

    mycursor = mydb.cursor()

    # Overwrite the address column from "Valley 345" to "Canyon 123"

    sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    # Prevent SQL Injection

    sql = "UPDATE customers SET address = %s WHERE address = %s"
    val = ("Valley 345", "Canyon 123")

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    mydb.close()
