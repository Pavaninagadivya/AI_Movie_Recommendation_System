# 🎬 AI Movie Recommendation System

An AI-powered Movie Recommendation System built using Python, Machine Learning, and Streamlit. The system recommends movies based on content similarity using genres, keywords, cast, director, and movie overview.

## 🚀 Features

- Content-Based Movie Recommendation
- Genre-Based Filtering
- Mood-Based Recommendation
- Age-Based Recommendation
- IMDb Rating Display
- Release Year Display
- Interactive Streamlit User Interface

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

```
data/
│── tmdb_5000_movies.csv
│── tmdb_5000_credits.csv
```

---

## 📦 About the Pickle Files

The files below are **not included** in this repository because they are generated automatically.

```
movies.pkl
similarity.pkl
```

Generate them by running:

```bash
python recommendation.py
```

This creates:

- movies.pkl
- similarity.pkl

These files are required before running the Streamlit application.

---

## ▶️ Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate Model Files

```bash
python recommendation.py
```

### 3. Start the Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
AI_Movie_Recommendation_System/
│
├── app.py
├── recommendation.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── movies.pkl        (Generated Automatically)
└── similarity.pkl    (Generated Automatically)
```

---

## 🔮 Future Improvements

- Movie Posters
- Movie Trailer Button
- User Login & Signup
- Favorite Movies
- Watchlist
- Personalized Recommendations
- Top Rated Movies
- Trending Movies

---

## 👩‍💻 Author

**Pavani Naga Divya**

Built as a Machine Learning and Streamlit project for learning, portfolio development, and placement preparation.
