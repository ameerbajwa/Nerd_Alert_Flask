
create_users_table = "CREATE TABLE users (" \
                     "  user_id INT NOT NULL PRIMARY KEY," \
                     "  username VARCHAR(300) NOT NULL UNIQUE," \
                     "  password VARCHAR(300) NOT NULL," \
                     "  email VARCHAR(300) NOT NULL," \
                     "  date_created DATETIME NOT NULL," \
                     "  last_login DATETIME NOT NULL," \
                     "  admin INT NOT NULL," \
                     "  creator INT NOT NULL" \
                     ");"

create_quiz_table = "CREATE TABLE quiz (" \
                    "   quiz_id INT NOT NULL PRIMARY KEY," \
                    "   quiz_name VARCHAR(500) NOT NULL," \
                    "   quiz_description VARCHAR(500)," \
                    "   source VARCHAR(100) NOT NULL," \
                    "   title_of_source VARCHAR(500) NOT NULL," \
                    "   createdBy VARCHAR(300) NOT NULL," \
                    "   createdBy_user_id INT NOT NULL," \
                    "   date_created datetime NOT NULL," \
                    "   status INT NOT NULL" \
                    ");"

create_quiz_question_table = "CREATE TABLE quiz_questions (" \
                             "  question_id INT NOT NULL PRIMARY KEY," \
                             "  quiz_id INT NOT NULL," \
                             "  question VARCHAR(500) NOT NULL," \
                             "  choice_A VARCHAR(500)," \
                             "  choice_B VARCHAR(500)," \
                             "  choice_C VARCHAR(500)," \
                             "  choice_D VARCHAR(500)," \
                             "  correct_answer VARCHAR(10) NOT NULL," \
                             "  date_created DATETIME NOT NULL," \
                             "  FOREIGN KEY (quiz_id) REFERENCES quiz(quiz_id) ON DELETE CASCADE" \
                             ");"

create_user_quiz_results = "CREATE TABLE user_quiz_results (" \
                           "    user_id INT NOT NULL," \
                           "    quiz_id INT NOT NULL," \
                           "    iteration INT NOT NULL," \
                           "    score INT NOT NULL," \
                           "    date_created DATETIME NOT NULL," \
                           "    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE," \
                           "    FOREIGN KEY (quiz_id) REFERENCES quiz(quiz_id) ON DELETE CASCADE" \
                           ");"

create_user_question_results = "CREATE TABLE user_question_results (" \
                               "    user_id INT NOT NULL," \
                               "    quiz_id INT NOT NULL," \
                               "    question_id INT NOT NULL," \
                               "    quiz_iteration INT NOT NULL," \
                               "    user_answer VARCHAR(10) NOT NULL," \
                               "    correct_answer VARCHAR(10) NOT NULL," \
                               "    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE," \
                               "    FOREIGN KEY (quiz_id) REFERENCES quiz(quiz_id) ON DELETE CASCADE," \
                               "    FOREIGN KEY (question_id) REFERENCES quiz_questions(question_id) ON DELETE CASCADE" \
                               ");"
