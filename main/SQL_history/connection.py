import pymysql


def connect_to_mysql_database():
    connection_to_database = pymysql.connect(
                                user='root',
                                password='Tennis07',
                                host='localhost',
                                database='nerd_alert',
                                cursorclass=pymysql.cursors.DictCursor
                             )
    return connection_to_database