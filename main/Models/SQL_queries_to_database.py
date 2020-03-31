from datetime import datetime
from werkzeug.security import generate_password_hash

from .connection import connect_to_mysql_database
from .create_tables_SQL_statements import create_users_table, create_quiz_table, create_quiz_question_table, create_user_quiz_results, create_user_question_results
from .users_table_SQL_statements import select_user_by_username, select_user_by_user_id, register_new_user, select_user_id
from .quiz_table_SQL_statements import select_all_quizzes, select_quiz_by_quiz_name, select_quiz_by_createdBy, select_quiz_by_quiz_type, select_quiz_by_id, insert_new_quiz, select_quiz_id
from .quiz_questions_tables_SQL_statements import insert_quiz_question, select_quiz_questions
from .user_quiz_results_table_SQL_statements import select_user_id_quiz_id, insert_user_quiz_results
from .user_question_results_table_SQL_statements import select_user_id_question_id, insert_user_question_results


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


def find_user_id():
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        sql_query = select_user_id
        cursor.execute(sql_query)
        result = cursor.fetchall()

    connection_to_database.close()

    return result


def create_user(data, user_id):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = register_new_user
        cursor.execute(query, (str(user_id+1), data['username'], generate_password_hash(data['password']), data['email'], str(datetime.now()),
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


def find_quiz_by_id(id):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = select_quiz_by_id
        cursor.execute(query, (id,))
        results = cursor.fetchall()

    connection_to_database.close()

    if len(results) > 0:
        return results
    else:
        return None


def create_quiz(data, quiz_id):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = insert_new_quiz
        cursor.execute(query, (str(quiz_id+1), data['quiz_name'], data['source'], data['title_of_source'],
                               data['createdBy'], str(data['createdBy_user_id']), str(datetime.now()), str(1)))

        connection_to_database.commit()

    connection_to_database.close()
    return True


def find_new_quiz_id():
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = select_quiz_id
        cursor.execute(query)
        result = cursor.fetchall()

    connection_to_database.close()
    return result


def create_quiz_question(data):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = insert_quiz_question
        cursor.execute(query, (str(data['question_id']), str(data['quiz_id']), data['question'], data['choice_A'],
                               data['choice_B'], data['choice_C'], data['choice_D'], data['correct_answer'],
                               str(datetime.now())))

        connection_to_database.commit()

    connection_to_database.close()
    return True


def find_quiz_questions(quiz, user):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = select_quiz_questions
        cursor.execute(query, (quiz, user))
        results = cursor.fetchall()

    connection_to_database.close()
    return results


def find_user_id_quiz_id(user, quiz):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = select_user_id_quiz_id
        cursor.execute(query, (user, quiz))
        results = cursor.fetchall()

    connection_to_database.close()
    return results


def implant_users_quiz_score(data):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = insert_user_quiz_results
        cursor.execute(query, (str(data['user_id']), str(data['quiz_id']), str(data['score']), str(datetime.now())))

        connection_to_database.commit()

    connection_to_database.close()
    return True


def find_user_id_question_id(user, question):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = select_user_id_question_id
        cursor.execute(query, (user, question))
        results = cursor.fetchall()

    connection_to_database.close()
    return results


def implant_users_question_answers(data):
    connection_to_database = connect_to_mysql_database()

    with connection_to_database.cursor() as cursor:
        query = insert_user_question_results
        cursor.execute(query, (str(data['user_id']), str(data['quiz_id']), str(data['question_id']),
                               data['user_answer'], data['correct_answer']))

        connection_to_database.commit()

    connection_to_database.close()
    return True
