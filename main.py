from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("hiking.sqlite")

db.execute("""
    CREATE TABLE IF NOT EXISTS HikingGroupUser(
        id integer primary key autoincrement,
        UserId integer,
        HikingGroupId integer
    );
""")

db.pretty_print("""
    SELECT
        HikingGroup.Destination AS Destination,
        HikingGroup.Name AS [Group],
        COUNT(*) AS UsersInDestination
    FROM User
    JOIN HikingGroup
    JOIN HikingGroupUser
    USING (UserId, HikingGroupId)
""")


# db.pretty_print("SELECT * FROM HikingGroupUser")

# db.print_tables(verbose=True)
