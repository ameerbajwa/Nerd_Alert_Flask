from .connection import connect_to_mysql_database
from .create_tables_SQL_statements import create_users_table, create_quiz_table, create_quiz_question_table, create_user_quiz_results, create_user_question_results


def create_Nerd_Alert_tables():
    connection_to_database = connect_to_mysql_database()

    create_tables_array = [create_users_table, create_quiz_table, create_quiz_question_table, create_user_quiz_results, create_user_question_results]

    for table in create_tables_array:
        with connection_to_database.cursor() as cursor:
            cursor.execute(table)
            connection_to_database.commit()
            print ("Executed `CREATE TABLE` command")

    connection_to_database.close()
