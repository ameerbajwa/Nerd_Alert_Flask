
insert_quiz_question = "INSERT INTO quiz_questions " \
                        "(" \
                       "    question_id, " \
                       "    quiz_id, " \
                       "    question, " \
                       "    choice_A, " \
                       "    choice_B, " \
                       "    choice_C, " \
                       "    choice_D, " \
                       "    correct_answer, " \
                       "    date_created" \
                       ") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"

# select_quiz_questions = "SELECT quiz_questions.* " \
#                         "FROM quiz_questions " \
#                         "JOIN user_question_results ON user_question_results.quiz_id = quiz_questions.quiz_id" \
#                         "JOIN users ON users_question_results.user_id = users.user_id" \
#                         "WHERE quiz_questions.quiz_id=%s " \
#                         "   AND quiz_questions.question_id NOT IN (SELECT question_id FROM user_question_results WHERE user_id=%s)"

select_quiz_questions = "SELECT * FROM quiz_questions " \
                        "WHERE quiz_id=%s " \
                        "AND question_id NOT IN (SELECT question_id FROM user_question_results WHERE user_id=%s);"
