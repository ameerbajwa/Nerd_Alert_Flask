
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

select_quiz_questions = "SELECT * FROM quiz_questions " \
                        "WHERE quiz_id=%s " \
                        "AND question_id NOT IN (SELECT question_id FROM user_question_results WHERE user_id=%s)" \
                        "ORDER BY RAND()" \
                        "LIMIT 10;"

delete_quiz_question = "DELETE FROM quiz_questions WHERE question_id=%s;"
