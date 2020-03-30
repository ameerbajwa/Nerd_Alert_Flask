
select_user_id_question_id = "SELECT * FROM user_question_results WHERE user_id=%s AND question_id=%s;"

insert_user_question_results = "INSERT INTO user_question_results " \
                               "(user_id, quiz_id, question_id, user_answer, correct_answer) " \
                               "VALUES (%s,%s,%s,%s,%s);"
