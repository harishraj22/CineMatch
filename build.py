import pandas as pd
import numpy as np
import ast



#Load and merge datasets
movies = pd.read_csv(r"C:\\Users\\Harish Raj\\OneDrive\\Documents\\Movie Recommender\\Data\\tmdb_5000_movies.csv")
credits = pd.read_csv(r"C:\Users\Harish Raj\OneDrive\Documents\Movie Recommender\Data\tmdb_5000_credits.csv")

movies = movies.merge(credits, on="title")

#useful columns
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

#Handle missing values
movies.dropna(inplace=True)

#Convert JSON strings to lists
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert)

#Extract director
def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L

movies['crew'] = movies['crew'].apply(fetch_director)   

#Prepare the overview
movies['overview'] = movies['overview'].apply(lambda x: x.split())

#Create a single "tags" column
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))

#Vectorize text
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

#calculate cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)

#saving the model
import pickle

pickle.dump(movies, open('movies.pkl','wb'))
pickle.dump(similarity, open('similarity.pkl','wb'))