
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

select_quiz_questions_for_quiz = "SELECT * FROM quiz_questions " \
                                 "WHERE quiz_id=%s " \
                                 "AND question_id NOT IN (SELECT question_id FROM user_question_results WHERE user_id=%s)" \
                                 "ORDER BY date_created" \
                                 "LIMIT 10;"

select_quiz_questions_for_editing = "SELECT * FROM quiz_questions " \
                                    "WHERE quiz_id=%s" \
                                    "ORDER BY date_created DESC;"

select_quiz_question = "SELECT * FROM quiz_questions WHERE question_id=%s;"

update_quiz_question =  "UPDATE quiz_questions SET " \
                        " question=%s, " \
                        " choice_A=%s, " \
                        " choice_B=%s, " \
                        " choice_C=%s, " \
                        " choice_D=%s, " \
                        " correct_answer=%s, " \
                        " date_created=%s" \
                        "WHERE question_id=%s;"

select_quiz_questions_by_ids = "SELECT * FROM quiz_questions WHERE question_id=%s;"

select_count_quiz_questions = "SELECT COUNT(*) FROM quiz_questions " \
                              "WHERE quiz_id=%s;"

delete_quiz_question = "DELETE FROM quiz_questions WHERE question_id=%s;"
