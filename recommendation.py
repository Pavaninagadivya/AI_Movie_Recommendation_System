import ast
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem.porter import PorterStemmer

# Load datasets
movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

print("Movies Shape:", movies.shape)
print("Credits Shape:", credits.shape)


# Keep required columns
movies = movies[['id',
                 'title',
                 'overview',
                 'genres',
                 'keywords',
                 'vote_average',
                 'release_date']]

# Merge datasets

movies = movies.merge(credits, on='title')

print("Merged Shape:", movies.shape)

# ==========================
# Handle missing values
# ==========================
movies = movies[['movie_id',
                 'title',
                 'overview',
                 'genres',
                 'keywords',
                 'cast',
                 'crew',
                 'vote_average',
                 'release_date']]
movies.dropna(inplace=True)

print("Null Values:")
print(movies.isnull().sum())

print("Duplicate Titles:", movies['title'].duplicated().sum())

# ==========================
# Convert Genres
# ==========================
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)

# ==========================
# Convert Keywords
# ==========================
movies['keywords'] = movies['keywords'].apply(convert)

# ==========================
# Convert Cast (Top 3 Actors)
# ==========================
def convert_cast(text):
    L = []
    counter = 0

    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
            counter += 1
        else:
            break

    return L

movies['cast'] = movies['cast'].apply(convert_cast)

# ==========================
# Fetch Director
# ==========================
def fetch_director(text):
    L = []

    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
            break

    return L

movies['crew'] = movies['crew'].apply(fetch_director)

# ==========================
# Convert Overview into List
# ==========================
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# ==========================
# Remove Spaces
# ==========================
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])

movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])

movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])

movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

# ==========================
# Create Tags
# ==========================
movies['tags'] = (
    movies['overview']
    + movies['genres']
    + movies['keywords']
    + movies['cast']
    + movies['crew']
)

# ==========================
# Final Dataset
# ==========================
new_df = movies[['movie_id',
                 'title',
                 'genres',
                 'vote_average',
                 'release_date',
                 'tags']].copy()

# Convert list to string
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

# Convert to lowercase
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

# ==========================
# Stemming
# ==========================

ps = PorterStemmer()

def stem(text):
    y = []

    for word in text.split():
        y.append(ps.stem(word))

    return " ".join(y)

new_df['tags'] = new_df['tags'].apply(stem)

print("\nAfter Stemming:")
print(new_df['tags'].head())

# ==========================
# Text Vectorization
# ==========================

cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(new_df['tags']).toarray()

print("\nVector Shape:")
print(vectors.shape)

# ==========================
# Cosine Similarity
# ==========================

similarity = cosine_similarity(vectors)

print("\nSimilarity Matrix Shape:")
print(similarity.shape)

# ==========================
# Recommendation Function
# ==========================

def recommend(movie):
    movie = movie.lower()

    matches = new_df[new_df['title'].str.lower() == movie]

    if matches.empty:
        print("Movie not found!")
        return

    index = matches.index[0]

    distances = list(enumerate(similarity[index]))

    movies_list = sorted(
        distances,
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    print("\nRecommended Movies:\n")

    for i in movies_list:
        print(new_df.iloc[i[0]].title)

# ==========================
# Show Output
# ==========================
print("\nFinal Dataset:")
print(new_df.head())

print("\nDataset Shape:", new_df.shape)

print("\nSample Tags:")
print(new_df['tags'][0])

recommend("Avatar")

# ==========================
# Save Model Files
# ==========================

pickle.dump(new_df, open('movies.pkl', 'wb'))

pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("\nmovies.pkl created successfully!")
print("similarity.pkl created successfully!")