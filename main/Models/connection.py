import pymysql
import config


def connect_to_mysql_database():

    connection_to_database = pymysql.connect(
                                user=config.MYSQL_DATABASE_USERNAME,
                                password=config.MYSQL_DATABASE_PASSWORD,
                                host=config.MYSQL_DATABASE_HOST,
                                database=config.MYSQL_DATABASE_NAME,
                                cursorclass=pymysql.cursors.DictCursor
                             )
    return connection_to_database
