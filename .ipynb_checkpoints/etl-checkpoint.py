import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    This function is used to select data from song related json files
    Arguments:
        cur: cursor of the database needs import data
        filepath:directory of folder containing files
        
    Returns:
    
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_columns = ['song_id', 'title', 'artist_id', 'year', 'duration']
    song_data = df[song_columns].values[0].tolist()
#     song_data = []
#     for each in song_columns:
#         song_data.append(df[each][0])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_columns = ['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']
    artist_data = df[artist_columns].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    This function is used to select data from log related json files
    
    Arguments:
        cur: cursor of the database needs import data
        filepath:directory of folder containing files
        
    Returns:
    
    """
    # open log file
    df = pd.read_json(filepath, lines=True, convert_dates=['ts'])

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    #There is a duplicate, is that normal?
    time_data = [[each, each.hour, each.day, each.week, each.month, each.year, each.dayofweek] for each in t]
    column_labels = ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']
    time_df = pd.DataFrame(time_data, columns=column_labels).drop_duplicates()

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_id = df['userId'].tolist()
    first_name = df['firstName'].tolist()
    last_name = df['lastName'].tolist()
    gender = df['gender'].tolist()
    level = df['level'].tolist()

    user_df = pd.DataFrame({'user_id':user_id,
                     'first_name':first_name,
                     'last_name':last_name,
                     'gender': gender,
                     'level': level}).drop_duplicates()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = [row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent]
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    will process each data file in a give filepath using func
    """

    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()