from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("hiking.sqlite")

db.execute("""
    CREATE TABLE IF NOT EXISTS User(
        id integer primary key autoincrement,
        name text,
        age integer
    );
""")

db.pretty_print("""
    SELECT * 
    FROM User;
""")

# db.print_tables(verbose=True)
