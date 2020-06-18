from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("hiking.sqlite")

db.execute("CREATE TABLE User(name text, age integer);")

db.print_tables()
