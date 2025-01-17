
# select_user_question_results = "SELECT * " \
#                                "FROM user_question_results " \
#                                "JOIN quiz_questions " \
#                                "ON user_question_results.question_id = quiz_questions.question_id " \
#                                "WHERE user_question_results.user_id=%s AND quiz_questions.quiz_id=%s " \
#                                "AND user_question_results.quiz_iteration=%s;"

select_user_question_results = "SELECT * " \
                               "FROM user_question_results " \
                               "WHERE user_id=%s AND quiz_id=%s AND quiz_iteration=%s;"

insert_user_question_results = "INSERT INTO user_question_results " \
                               "(user_question_results_id, user_id, quiz_id, question_id, quiz_iteration, " \
                               "user_answer, correct_answer) " \
                               "VALUES (%s,%s,%s,%s,%s,%s,%s);"
