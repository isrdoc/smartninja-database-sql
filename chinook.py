from smartninja_sql.sqlite import SQLiteDatabase

chinook = SQLiteDatabase("Chinook_Sqlite.sqlite")

chinook.pretty_print("""
    SELECT
        Album.ArtistId AS Album,
        Artist.ArtistId AS Artist
    FROM Album
    JOIN Artist
    USING (ArtistId)
    WHERE Artist.ArtistId=1;
""")
