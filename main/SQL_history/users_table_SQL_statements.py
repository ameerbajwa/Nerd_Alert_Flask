
select_user_by_username = "SELECT * FROM users WHERE username=%s;"

select_user_by_user_id = "SELECT * FROM users WHERE user_id=%s;"

register_new_user = "INSERT INTO users (user_id, username, password, email, date_created, last_login) " \
                    "VALUES (%s,%s,%s,%s,%s,%s);"


