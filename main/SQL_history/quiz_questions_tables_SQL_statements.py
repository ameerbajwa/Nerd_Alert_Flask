
insert_quiz_question = "INSERT INTO quiz_questions " \
                        "(" \
                       "    question_id, " \
                       "    quiz_id, question, " \
                       "    choice_A, " \
                       "    choice_B, " \
                       "    choice_C, " \
                       "    choice_D, " \
                       "    correct_answer, " \
                       "    date_created" \
                       ") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
