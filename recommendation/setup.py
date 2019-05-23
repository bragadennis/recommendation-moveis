import pandas as pd
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client.recommendation

u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('../../datasets/ml-100k/u.user', sep='|', names=u_cols,encoding='latin-1')

#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('../../datasets/ml-100k/u.data', sep='\t', names=r_cols,encoding='latin-1')

#Reading items file:
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('../../datasets/ml-100k/u.item', sep='|', names=i_cols, encoding='latin-1')

tb_users = database.users
tb_users.insert_many(users.to_dict('records')) #Converts the imported data into an array of dictionaries with each column name being the identifier for an attribute

tb_ratings = database.ratings
tb_ratings.insert_many(ratings.to_dict('records'))

tb_items = database.items
tb_items.insert_many(items.to_dict('records'))