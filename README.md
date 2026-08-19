# 🎬 AI Movie Recommendation System

An AI-powered Movie Recommendation System built using Python, Machine Learning, and Streamlit. The system recommends movies based on content similarity using genres, keywords, cast, director, and movie overview. It also provides genre recommendations based on the user's age and mood.

## 🚀 Features

- Content-Based Movie Recommendation
- Genre-Based Filtering
- Mood-Based Recommendation
- Age-Based Recommendation
- AI Similarity Score
- IMDb Rating Display
- Release Year Display
- Interactive Streamlit User Interface
- Fallback Recommendations

---

## 🧠 Recommendation Technique

The system uses **Content-Based Filtering** to recommend similar movies.

Movie information such as:

- Movie Overview
- Genres
- Keywords
- Cast
- Director

is combined to create movie tags.

The tags are processed using:

- Porter Stemmer
- CountVectorizer
- Cosine Similarity

The system also uses the user's **age and current mood** to select a suitable movie genre.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- NLTK
- Pickle

---

## 📂 Dataset

This project uses the **TMDB 5000 Movie Dataset**.

Download the following files and place them inside a folder named **data**:
