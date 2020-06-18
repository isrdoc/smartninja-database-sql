from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("hiking.sqlite")

db.execute("""
    CREATE TABLE IF NOT EXISTS User(
        id integer primary key autoincrement,
        name text,
        age integer
    );
""")

to_delete = ["1", "3", "5"]

separator = ", "
str_to_delete = separator.join(to_delete)

db.execute("""
    DELETE FROM User 
    WHERE id IN (""" + str_to_delete + """);
""")

db.pretty_print("SELECT * FROM User")

# db.print_tables(verbose=True)
