import mysql.connector
from utilities.common import get_env_var

env_var = get_env_var()


def join_items():

    mydb = mysql.connector.connect(
        host=env_var[0],
        user=env_var[1],
        password=env_var[2],
        database=env_var[3]
    )

    mycursor = mydb.cursor()

    # Join users and products to see the name of the users favorite product

    sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    INNER JOIN products ON users.fav = products.id"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mydb.close()
