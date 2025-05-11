################################# Part 1.1 ########################################
##  Reading Files
# import sqlite3
# import pandas as pd

# with sqlite3.connect('C:\Python\darslar\chinook.db') as conn:
#     df = pd.read_sql_query("SELECT * FROM customers", conn)
#     print(df.head(10))
################################# Part 1.2 ######################################
# import pandas as pd

# df = pd.read_json('C:\Python\darslar\iris.json')

# print("Shape:", df.shape)

# print("Columns:", df.columns.tolist())
################################# Part 1.3 ######################################
# import pandas as pd

# df = pd.read_excel('C:\Python\darslar\\titanic.xlsx')

# print(df.head())
################################# Part 1.4 ######################################
# import pandas as pd

# df = pd.read_csv('C:/Python/darslar/flights.csv')


# df.info()
################################# Part 1.4 ######################################
# import pandas as pd

# df = pd.read_csv('C:\Python\darslar\movie.csv')

# print(df.sample(10))
################################# Part 2.1 ######################################
# import pandas as pd
# df = pd.read_json(r'C:\Python\darslar\iris.json')
# df.columns = df.columns.str.replace(r'([a-z])([A-Z])', r'\1_\2', regex=True).str.lower()
# print(df.columns)
# df_selected = df[['sepal_length', 'sepal_width']]
# print(df_selected)
################################# Part 2.2 ######################################
# import pandas as pd

# df = pd.read_excel(r'C:\Python\darslar\titanic.xlsx')

# print(df.columns)
################################# Part 2.3 ######################################
# import pandas as pd

# df = pd.read_parquet('C:/Python/darslar/flights.htm')

# df_selected = df[['origin', 'dest', 'carrier']]
# print(df_selected)

# unique_dest_count = df['dest'].nunique()
# print(f"Number of unique destinations: {unique_dest_count}")
################################# Part 2.4 ######################################
# import pandas as pd

# df = pd.read_csv('C:/Python/darslar/movie.csv')

# df_filtered = df[df['duration'] > 120]

# df_sorted = df_filtered.sort_values(by='director_facebook_likes', ascending=False)

# print(df_sorted)
################################# Part 3 ######################################
# import pandas as pd

# # JSON faylni o‘qish
# iris_df = pd.read_json(r'C:\Python\darslar\iris.json')

# # Raqamli ustunlar bo‘yicha statistikalar
# print("IRIS Dataset – Mean:")
# print(iris_df.mean(numeric_only=True))

# print("\nMedian:")
# print(iris_df.median(numeric_only=True))

# print("\nStandard Deviation:")
# print(iris_df.std(numeric_only=True))
# # Excel faylni o‘qish
# titanic_df = pd.read_excel(r'C:\Python\darslar\titanic.xlsx')

# # Ustun nomlarini tekshirish (kerak bo‘lishi mumkin)
# # print(titanic_df.columns)

# # Faraz: 'Age' nomli ustun mavjud
# print("TITANIC Dataset – Age stats:")
# print("Min:", titanic_df['Age'].min())
# print("Max:", titanic_df['Age'].max())
# print("Sum:", titanic_df['Age'].sum())

# # CSV faylni o‘qish
# movie_df = pd.read_csv(r'C:\Python\darslar\movie.csv')

# # 1) Eng ko‘p director_facebook_likes to‘plagan rejissor
# likes_sum = movie_df.groupby('director_name')['director_facebook_likes'].sum()
# top_director = likes_sum.idxmax()
# top_likes = likes_sum.max()
# print(f"Most liked director: {top_director} ({top_likes} likes)")

# # 2) Eng uzun 5 ta film va ularning rejissorlari
# top5_movies = movie_df[['movie_title', 'duration', 'director_name']].sort_values(by='duration', ascending=False).head(5)
# print("\nTop 5 longest movies:")
# print(top5_movies)

# # Parquet faylni o‘qish
# flights_df = pd.read_parquet(r'C:\Python\darslar\Flights.parquet')

# # 1) Yo‘q qiymatlarni tekshirish
# print("FLIGHTS Dataset – Missing values by column:")
# print(flights_df.isnull().sum())

# # 2) Bitta raqamli ustundagi yo‘q qiymatlarni o‘rtacha bilan to‘ldirish (masalan: 'air_time')
# if 'air_time' in flights_df.columns:
#     flights_df['air_time'] = flights_df['air_time'].fillna(flights_df['air_time'].mean())
#     print("\nMissing values in 'air_time' filled with mean.")
# else:
#     print("\nColumn 'air_time' not found.")
