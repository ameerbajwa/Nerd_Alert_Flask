from .. import connection
from .create_tables import create_users_table, create_quiz_table, create_quiz_question_table, create_user_quiz_results, create_user_question_results

connection_to_database = connection.connect_to_mysql_database()

create_tables_array = [create_users_table, create_quiz_table, create_quiz_question_table, create_user_quiz_results, create_user_question_results]

for table in create_tables_array:
    with connection_to_database.cursor() as cursor:
        cursor.execute(table)

connection_to_database.commit()
connection_to_database.close()
