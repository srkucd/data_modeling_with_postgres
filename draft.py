import pandas as pd
import psycopg2
from sql_queries import *

# df = pd.read_json('data/log_data/2018/11/2018-11-01-events.json' ,lines=True)
conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
cur = conn.cursor()
# # cur.execute()
# print(df['action'])
# # print(type(df['title'][0]))

# df = pd.read_json('data/log_data/2018/11/2018-11-01-events.json', lines=True, convert_dates=['ts'])
df2 = pd.read_json('data/song_data/A/A/A/TRAAAAW128F429D538.json', lines=True)
# print(df)
# df = df[df['page']=='NextSong']
# t = pd.to_datetime(df['ts'], unit='ms')

song_columns = ['song_id', 'title', 'artist_id', 'year', 'duration']
song_data = []
for each in song_columns:
    song_data.append(df2[each][0])

for each in song_data:
    print(type(each))