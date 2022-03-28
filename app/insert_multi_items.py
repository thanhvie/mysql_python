import mysql.connector
from utilities.common import get_env_var

env_var = get_env_var()


def insert_multi_items():

    mydb = mysql.connector.connect(
        host=env_var[0],
        user=env_var[1],
        password=env_var[2],
        database=env_var[3]
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = [
        ('Peter', 'Lowstreet 4'),
        ('Amy', 'Apple st 652'),
        ('Hannah', 'Mountain 21'),
        ('Michael', 'Valley 345'),
        ('Sandy', 'Ocean blvd 2'),
        ('Betty', 'Green Grass 1'),
        ('Richard', 'Sky st 331'),
        ('Susan', 'One way 98'),
        ('Vicky', 'Yellow Garden 2'),
        ('Ben', 'Park Lane 38'),
        ('William', 'Central st 954'),
        ('Chuck', 'Main Road 989'),
        ('Viola', 'Sideway 1633')
    ]

    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")

    # insert items into users table

    sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
    val = [
        ('John', '154'),
        ('Peter', '154'),
        ('Amy', '155'),
        ('Hannah', ''),
        ('Michael', '')
    ]

    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")

    # insert items into products table

    sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
    val = [
        ('154', 'Chocolate Heaven'),
        ('155', 'Tasty Lemons'),
        ('156', 'Vanilla Dreams')
    ]

    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")

    mydb.close()
