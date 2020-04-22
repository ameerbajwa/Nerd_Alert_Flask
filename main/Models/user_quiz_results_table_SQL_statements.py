
select_user_quiz_results = "SELECT * FROM user_quiz_results WHERE user_id=%s AND quiz_id=%s;"

select_quiz_iteration = "SELECT iteration FROM user_quiz_results WHERE quiz_id=%s ORDER BY iteration DESC LIMIT 1;"

insert_user_quiz_results = "INSERT INTO user_quiz_results (user_id, quiz_id, iteration, score, date_created) " \
                           "VALUES (%s,%s,%s,%s,%s);"
