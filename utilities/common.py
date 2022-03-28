import os
from os.path import join
from dotenv import load_dotenv

base_dir = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = join(base_dir, '.env')
load_dotenv(dotenv_path)


def get_env_var():
    host = os.environ.get("HOST")
    user = os.environ.get('MYSQL_USER')
    password = os.environ.get('PASSWORD')
    database = os.environ.get('DATABASE')
    return host, user, password, database
