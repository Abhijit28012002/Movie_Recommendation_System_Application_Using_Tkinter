import numpy as np
import pandas as pd
import difflib # Closest match of Some Value
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Loading the data
movies_data = pd.read_csv('moviesnew.csv')

# selecting relevent feature for recommendation
selected_features = ['genres','original_title','keywords','director','tagline']


# replacing the null values (if I have) with null string
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

x=movies_data['genres']
y=movies_data['original_title']

# Combining all the selected feature
combined_features = x+' '+y

# Convert the text data to feature vectors
vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_features)

# getting the similarity scores using cosine similarity
similarity = cosine_similarity(feature_vectors)

def main(movie_name):

    # createing a list with all the movie names given in the database
    list_of_all_title= movies_data['original_title'].tolist()

    # finding the close match for the movie name given by the user
    find_close_match = difflib.get_close_matches(movie_name,list_of_all_title)

    close_match = find_close_match[0]

    index_of_movie = movies_data[movies_data.title == close_match]['index'].values[0]

    # getting the list of similar movies

    similarity_score = list(enumerate(similarity[index_of_movie]))

    sorted_similar_movies = sorted(similarity_score, key= lambda x:x[1], reverse= True)
    
    s=[]
    # print the name of similar movie based on the index
    a='Movies Suggested for you:'
    s.append(a)

    i=0

    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index==index]['original_title'].values[0]
        if i<5:
            a=f'{i+1} . {title_from_index}'
            s.append(a)
            i+=1
    return s
