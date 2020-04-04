import pandas as pd

# df = pd.read_json('data/log_data/2018/11/2018-11-01-events.json' ,lines=True)
# # conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
# # cur = conn.cursor()
# # cur.execute()
# print(df['action'])
# # print(type(df['title'][0]))

df = pd.read_json('data/log_data/2018/11/2018-11-01-events.json', lines=True, convert_dates=['ts'])
# print(df)
df = df[df['page']=='NextSong']
# t = pd.to_datetime(df['ts'], unit='ms')
# print(t)
# print(df)
# print(type(t))
# print(t[2].dayofweek)
user_id = df['userId'].tolist()
first_name = df['firstName'].tolist()
last_name = df['lastName'].tolist()
gender = df['gender'].tolist()
level = df['level'].tolist()

user_df = pd.DataFrame({'user_id':user_id,
                     'first_name':first_name,
                     'last_name':last_name,
                     'gender': gender,
                     'level': level})
print(temp)
# print(user_id)
# print(type(user_id))