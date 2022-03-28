import mysql.connector
from utilities.common import get_env_var

env_var = get_env_var()


def create_table():

    mydb = mysql.connector.connect(
        host=env_var[0],
        user=env_var[1],
        password=env_var[2],
        database=env_var[3]
    )

    # create table
    mycursor = mydb.cursor()

    mycursor.execute(
        "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

    mycursor.execute(
        "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav VARCHAR(255))")

    mycursor.execute(
        "CREATE TABLE products (id VARCHAR(255), name VARCHAR(255))")

    # get list of tables
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)

    mydb.close()
