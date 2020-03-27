
create_users_table = "CREATE TABLE users (" \
                     "  user_id INT NOT NULL PRIMARY KEY," \
                     "  username VARCHAR(300) NOT NULL UNIQUE," \
                     "  password VARCHAR(300) NOT NULL," \
                     "  email VARCHAR(300) NOT NULL," \
                     "  date_created DATETIME NOT NULL," \
                     "  last_login DATETIME NOT NULL" \
                     ");"

create_quiz_table = "CREATE TABLE quiz (" \
                    "   quiz_id INT NOT NULL PRIMARY KEY," \
                    "   quiz_name VARCHAR(500) NOT NULL," \
                    "   type_of_quiz VARCHAR(100) NOT NULL," \
                    "   createdBy VARCHAR(300) NOT NULL UNIQUE," \
                    "   createdBy_user_id INT NOT NULL UNIQUE," \
                    "   date_created datetime NOT NULL," \
                    "   active INT NOT NULL" \
                    ");"

create_quiz_question_table = "CREATE TABLE quiz_questions (" \
                             "  question_id INT NOT NULL PRIMARY KEY," \
                             "  quiz_id INT NOT NULL UNIQUE," \
                             "  " \
                             ");"