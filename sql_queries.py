# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES
# {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL, 
                                                                start_time INT, 
                                                                user_id INT, 
                                                                level INT, 
                                                                song_id INT, 
                                                                artist_id INT, 
                                                                session_id INT, 
                                                                location VARCHAR,
                                                                user_agent VARCHAR,
                                                                PRIMARY KEY(songplay_id))
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(user_id INT, 
                                                            first_name VARCHAR,
                                                            last_name VARCHAR,
                                                            gender VARCHAR,
                                                            level VARCHAR,
                                                            PRIMARY KEY(user_id))
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id INT,
                                                         title VARCHAR,
                                                         artist_id INT,
                                                         year INT,
                                                         duration INT,
                                                         PRIMARY KEY(song_id))
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(artist_id INT, 
                                                             name VARCHAR, 
                                                             location VARCHAR, 
                                                             latitude REAL, 
                                                             longitude REAL,
                                                             PRIMARY KEY(artist_id))
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time TIMESTAMP,
                                                        hour INT,
                                                        day INT,
                                                        week INT,
                                                        month INT,
                                                        year INT,
                                                        weekday VARCHAR)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level)
                        VALUES (%s,%s,%s,%s,%s)
""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration)
                        VALUES (%s,%s,%s,%s,%s)
""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude)
                          VALUES(%s,%s,%s,%s,%s)
""")


time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday)
                        VALUES(%s,%s,%s,%s,%s,%s,%s)
""")

# FIND SONGS

song_select = ("""SELECT song_id, artist_id FROM 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]