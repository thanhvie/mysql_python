import mysql.connector
from utilities.common import get_env_var

env_var = get_env_var()


def get_where():

    mydb = mysql.connector.connect(
        host=env_var[0],
        user=env_var[1],
        password=env_var[2],
        database=env_var[3]
    )

    mycursor = mydb.cursor()

    # Select record(s) where the address is "Park Lane 38"

    sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    # Select records where the address contains the word "way":

    sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    # Escape query values by using the placeholder %s method

    sql = "SELECT * FROM customers WHERE address = %s"
    adr = ("Yellow Garden 2", )

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mydb.close()
