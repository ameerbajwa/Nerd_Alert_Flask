from Models import SQL_queries_to_database

create_tables = 1

if create_tables == 1:
    SQL_queries_to_database.create_nerd_alert_tables()

