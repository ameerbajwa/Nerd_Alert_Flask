
select_all_quizzes = "SELECT * FROM quiz;"

select_quiz_by_quiz_name = "SELECT * FROM quiz WHERE quiz_name=%s;"

select_quiz_by_createdBy = "SELECT * FROM quiz WHERE createdBy=%s;"

select_quiz_by_quiz_type = "SELECT * FROM quiz WHERE type_of_quiz=%s;"

select_quiz_by_id = "SELECT * FROM quiz WHERE quiz_id=%s;"

insert_new_quiz = "INSERT INTO quiz (" \
                  " quiz_id, " \
                  " quiz_name, " \
                  " source, " \
                  " title_of_source," \
                  " createdBy, " \
                  " createdBy_user_id, " \
                  " date_created, " \
                  " active) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"

select_quiz_id = "SELECT quiz_id FROM quiz ORDER BY date_created DESC LIMIT 1"
