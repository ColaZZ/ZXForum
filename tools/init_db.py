from peewee import MySQLDatabase

from apps.users.models import User

# from ZxForm.settings import database
database = MySQLDatabase(
    "zxforum", host="127.0.0.1", port=3306, user="root", password="root"
)


def init():
    # 生成表
    database.create_tables([User])


if __name__ == "__main__":
    init()