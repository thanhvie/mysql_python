from app.create_database import create_database
from app.create_table import create_table
from app.insert_multi_items import insert_multi_items
from app.mysql_delete import delete_items
from app.mysql_drop_table import drop_table
from app.mysql_join import join_items
from app.mysql_limit import get_limit
from app.mysql_order_by import get_order_by
from app.mysql_select import get_select
from app.mysql_update import get_update
from app.mysql_where import get_where

if __name__ == '__main__':
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
