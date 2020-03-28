from datetime import datetime

from .connection import connect_to_mysql_database
from .create_tables_SQL_statements import create_users_table, create_quiz_table, create_quiz_question_table, create_user_quiz_results, create_user_question_results
from .users_table_SQL_statements import select_user_by_username, select_user_by_user_id, register_new_user
from .quiz_table_SQL_statements import select_all_quizzes, select_quiz_by_quiz_name, select_quiz_by_createdBy, select_quiz_by_quiz_type


def create_nerd_alert_tables():
    connection_to_database = connect_to_mysql_database()

    create_tables_array = [create_users_table, create_quiz_table, create_quiz_question_table, create_user_quiz_results, create_user_question_results]

    for table in create_tables_array:
        with connection_to_database.cursor() as cursor:
            cursor.execute(table)
            connection_to_database.commit()
            print ("Executed `CREATE TABLE` command")

    connection_to_database.close()


def find_user_by_username(username):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        sql_query = select_user_by_username
        cursor.execute(sql_query, (username,))
        results = cursor.fetchone()

    connection_to_database.close()

    return results


def find_user_by_id(_id):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        sql_query = select_user_by_user_id
        cursor.execute(sql_query, (_id,))
        results = cursor.fetchone()

    connection_to_database.close()

    return results


def create_user(data):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = register_new_user
        cursor.execute(query, (data['id'], data['username'], data['password'], data['email'], str(datetime.now()),
                               str(datetime.now())))

        connection_to_database.commit()

    connection_to_database.close()
    return True


def find_all_quizzes():
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = select_all_quizzes
        cursor.execute(query)
        results = cursor.fetchall()

    connection_to_database.close()

    return results


def find_quiz_by_username(username):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = select_quiz_by_quiz_name
        cursor.execute(query, (username,))
        results = cursor.fetchall()

    connection_to_database.close()

    return results


def find_quiz_by_creator(creatdBy):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = select_quiz_by_createdBy
        cursor.execute(query, (creatdBy,))
        results = cursor.fetchall()

    connection_to_database.close()

    return results


def find_quiz_by_type(type):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = select_quiz_by_quiz_type
        cursor.execute(query, (type,))
        results = cursor.fetchall()

    connection_to_database.close()

    return results
