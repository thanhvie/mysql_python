import mysql.connector
from utilities.common import get_env_var

env_var = get_env_var()


def delete_items():

    mydb = mysql.connector.connect(
        host=env_var[0],
        user=env_var[1],
        password=env_var[2],
        database=env_var[3]
    )

    mycursor = mydb.cursor()

    # Delete any record where the address is "Mountain 21"

    sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

    # Prevent SQL Injection
    sql = "DELETE FROM customers WHERE address = %s"
    adr = ("Yellow Garden 2", )

    mycursor.execute(sql, adr)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

    mydb.close()
