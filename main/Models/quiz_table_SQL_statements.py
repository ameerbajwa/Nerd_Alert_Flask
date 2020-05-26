
select_all_quizzes = "SELECT * FROM quiz WHERE createdBy_user_id!=%s;"
select_quiz_by_quiz_name = "SELECT * FROM quiz WHERE quiz_name=%s AND createdBy_user_id!=%s;"
select_quiz_by_createdBy = "SELECT * FROM quiz WHERE createdBy=%s AND createdBy_user_id!=%s;"
select_quiz_by_source = "SELECT * FROM quiz WHERE source=%s AND createdBy_user_id!=%s;"

select_users_quizzes = "SELECT * FROM quiz WHERE createdBy_user_id=%s;"
select_users_quiz_by_quiz_name = "SELECT * FROM quiz WHERE quiz_name=%s AND createdBy_user_id=%s;"
select_users_quiz_by_createdBy = "SELECT * FROM quiz WHERE createdBy=%s AND createdBy_user_id=%s;"
select_users_quiz_by_source = "SELECT * FROM quiz WHERE source=%s AND createdBy_user_id=%s;"

select_quiz_by_id = "SELECT * FROM quiz WHERE quiz_id=%s;"

update_quiz = "UPDATE quiz SET " \
              " quiz_name=%s, " \
              " quiz_description=%s, " \
              " source=%s, " \
              " title_of_source=%s " \
              "WHERE quiz_id=%s;"

insert_new_quiz = "INSERT INTO quiz (" \
                  " quiz_id, " \
                  " quiz_name, " \
                  " quiz_description, " \
                  " source, " \
                  " title_of_source," \
                  " createdBy, " \
                  " createdBy_user_id, " \
                  " date_created, " \
                  " status) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"

select_quiz_id = "SELECT quiz_id FROM quiz ORDER BY date_created DESC LIMIT 1;"

delete_quiz = "UPDATE quiz SET status = 0 WHERE quiz_id=%s;"
