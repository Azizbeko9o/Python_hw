################################# Merging and Joining 1 ######################################
# import sqlite3

# conn = sqlite3.connect('C:\Python\darslar\chinook.db')
# cursor = conn.cursor()

# query = '''
#     SELECT c.CustomerId, c.FirstName, c.LastName, COUNT(i.InvoiceId) AS TotalInvoices
#     FROM customers c
#     INNER JOIN invoices i ON c.CustomerId = i.CustomerId
#     GROUP BY c.CustomerId
# '''

# cursor.execute(query)

# rows = cursor.fetchall()

# for row in rows:
#     print(f"Mijoz: {row[1]} {row[2]} - Hisob-fakturalar soni: {row[3]}")

# conn.close()
################################# Merging and Joining 2 ######################################
# import pandas as pd

# movies_df = pd.read_csv('C:\Python\darslar\movie.csv')

# df_color = movies_df[['director_name', 'color']]

# df_reviews = movies_df[['director_name', 'num_critic_for_reviews']]

# left_joined_df = pd.merge(df_color, df_reviews, on='director_name', how='left')

# full_outer_joined_df = pd.merge(df_color, df_reviews, on='director_name', how='outer')

# left_join_rows = len(left_joined_df)
# full_outer_join_rows = len(full_outer_joined_df)

# print(f"Left join qatorlar soni: {left_join_rows}")
# print(f"Full outer join qatorlar soni: {full_outer_join_rows}")
################################# Grouping and Aggregating 1 ######################################
# import pandas as pd

# titanic_df = pd.read_csv('C:/Python/darslar/titanic.csv')

# grouped_df = titanic_df.groupby('Pclass').agg(
#     average_age=('Age', 'mean'),
#     total_fare=('Fare', 'sum'),
#     passenger_count=('PassengerId', 'count')
# ).reset_index()

# print(grouped_df)
################################# Grouping and Aggregating 2 ######################################
# import pandas as pd

# movies_df = pd.read_csv('C:\Python\darslar\movie.csv')

# grouped_df = movies_df.groupby(['color', 'director_name']).agg(
#     total_num_critic_for_reviews=('num_critic_for_reviews', 'sum'),
#     average_duration=('duration', 'mean')
# ).reset_index()

# print(grouped_df)
################################# Grouping and Aggregating 3 ######################################
# import pandas as pd

# dfs = pd.read_html('C:/Python/darslar/flights.htm')

# df = dfs[0]

# print(df.head())

# df['FlightDate'] = pd.to_datetime(df['FlightDate'])

# df['Year'] = df['FlightDate'].dt.year
# df['Month'] = df['FlightDate'].dt.month

# grouped_flights = df.groupby(['Year', 'Month']).agg(
#     total_flights=('FlightID', 'count'),
#     avg_arrival_delay=('ArrDelay', 'mean'),
#     max_departure_delay=('DepDelay', 'max')
# ).reset_index()

# print(grouped_flights)
################################# Using pipe 1 ######################################
# import pandas as pd
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import FunctionTransformer
# from sklearn.impute import SimpleImputer

# df = pd.read_csv('C:/Python/darslar/titanic.csv')

# def filter_survived(df):
#     return df[df['Survived'] == 1]

# imputer = SimpleImputer(strategy='mean')

# def create_fare_per_age(df):
#     df['Fare_Per_Age'] = df['Fare'] / df['Age']
#     return df

# pipeline = Pipeline(steps=[
#     ('filter_survived', FunctionTransformer(filter_survived, validate=False)),
#     ('impute_age', FunctionTransformer(lambda df: pd.DataFrame(imputer.fit_transform(df[['Age']])), validate=False)),
#     ('create_fare_per_age', FunctionTransformer(create_fare_per_age, validate=False))
# ])

# df_transformed = pipeline.fit_transform(df)

# df_transformed = pd.DataFrame(df_transformed, columns=df.columns)

# print(df_transformed.head())
################################# Using pipe 2 ######################################
# import pandas as pd
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import FunctionTransformer

# df = pd.read_csv('C:/Python/darslar/flights.htm')  

# def filter_flights(df):
#     return df[df['DepDelay'] > 30]

# def add_delay_per_hour(df):
#     df['Delay_Per_Hour'] = df['DepDelay'] / df['ScheduledDuration']
#     return df

# pipeline = Pipeline(steps=[
#     ('filter_flights', FunctionTransformer(filter_flights, validate=False)),
#     ('add_delay_per_hour', FunctionTransformer(add_delay_per_hour, validate=False))
# ])

# df_transformed = pipeline.fit_transform(df)

# df_transformed = pd.DataFrame(df_transformed, columns=df.columns)

# print(df_transformed.head())
