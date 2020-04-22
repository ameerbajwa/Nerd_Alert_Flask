
select_user_by_username = "SELECT * FROM users WHERE username=%s;"

select_user_by_user_id = "SELECT * FROM users WHERE user_id=%s;"

register_new_user = "INSERT INTO users (user_id, username, password, email, date_created, last_login, admin, creator) " \
                    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"

select_user_id = "SELECT user_id FROM users ORDER BY date_created DESC LIMIT 1;"
