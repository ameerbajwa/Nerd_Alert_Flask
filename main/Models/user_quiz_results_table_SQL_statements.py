
select_user_quiz_results = "SELECT * FROM user_quiz_results WHERE user_id=%s AND quiz_id=%s;"

insert_user_quiz_results = "INSERT INTO user_quiz_results (user_id, quiz_id, iteration, score, date_created) " \
                           "VALUES (%s,%s,%s,%s,%s);"
