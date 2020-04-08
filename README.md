# Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
This database is used for save songs and users' data from json file that is not cleaned and converted to correct format.

It can be used for search each song's information such as time and artist, and the data based on user's record.

It will help data analyst in Sparkify to make some marketing strategy, and the data can also used for recommender system.

For example, an user click like on a song, we can recommend other songs written by the same artist.

# State and justify your database schema design and ETL pipeline.

## Schema

### Fact tables

#### Songplays

Records in log data associated with song plays i.e. records with `page` set to
`NextSong`.

|   Column    |            Type             | 
| ----------- | --------------------------- | 
| songplay_id | integer                     | 
| start_time  | timestamp without time zone |
| user_id     | integer                     |
| level       | character varying           |
| song_id     | character varying(18)       |
| artist_id   | character varying(18)       |
| session_id  | integer                     |
| location    | character varying           |
| user_agent  | character varying           |

Primary key: songplay_id

### Dimension tables

#### Users

Users in the app.

|   Column   |       Type        | 
| ---------- | ----------------- |
| user_id    | integer           |
| first_name | character varying |
| last_name  | character varying |
| gender     | character(1)      |
| level      | character varying |

Primary key: user_id

#### Songs

Songs in music database.

|  Column   |         Type          |
| --------- | --------------------- |
| song_id   | character varying(18) |
| title     | character varying     |
| artist_id | character varying(18) |
| year      | integer               |
| duration  | double precision      |

Primary key: song_id

#### Artists

Artists in music database.

|  Column   |         Type          |
| --------- | --------------------- |
| artist_id | character varying(18) |
| name      | character varying     |
| location  | character varying     |
| latitude  | double precision      |
| longitude | double precision      |

Primary key: artist_id

#### Time

Timestamps of records in songplays broken down into specific units.

|   Column   |            Type             | 
| ---------- | --------------------------- | 
| start_time | timestamp without time zone | 
| hour       | integer                     | 
| day        | integer                     | 
| week       | integer                     | 
| month      | integer                     | 
| year       | integer                     | 
| weekday    | integer                     | 


During this program, I understand some of very important knowledge:

\* The step of RDBMS based on python.

\* My code can be clearer. For example, when I am going to create a list based on an old list, I don't have to create an empty list, sometimes I can use loop within the list, it makes my code more elegant.