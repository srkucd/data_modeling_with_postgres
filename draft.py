import pandas as pd

df = pd.read_json('data/log_data/2018/11/2018-11-01-events.json' ,lines=True)
# conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
# cur = conn.cursor()
# cur.execute()
print(df['action'])
# print(type(df['title'][0]))