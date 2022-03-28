# mysql_python
This project demonstrate the integration of python and mysql which includes these actions:
- Create a new database
- Create a new table
- Insert items
- Delete items
- Update items
- Get items with select, from, where, limit, order by
- Drop table
- Join two tables
# requirements

This project using mysql docker image so please install docker if you don't have docker yet.
It is not required but a mysql server ide is helpful to interact with mysql server. I'm using Mysql Workbench.

### mysql server: https://hub.docker.com/_/mysql

### mysql server ide: https://dev.mysql.com/downloads/workbench/

## How to Run:

- Run `app.py`
- There is a list of functions as below:
```python
    create_database()
    create_table()
    insert_multi_items()
    delete_items()
    get_select()
    get_where()
    get_order_by()
    get_limit()
    get_update()
    join_items()
    drop_table()
```

## Security:

- All sensitive data is stored in `.env` file. They will be updated by users at setup time.