import streamlit as st
import pickle

# ==========================
# Load Data
# ==========================
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# ==========================
# Recommendation Function
# ==========================
def recommend(movie, genre):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in movies_list:

        movie_data = movies.iloc[i[0]]

        movie_genres = movie_data["genres"]

        if genre.replace("-", "").replace(" ", "") in movie_genres:

            if movie_data["title"] != movie:
                recommended_movies.append({

    "title": movie_data["title"],

    "rating": movie_data["vote_average"],

    "year": str(movie_data["release_date"])[:4]

})

        if len(recommended_movies) == 5:
            break

    return recommended_movies

    # ==========================
# Age + Mood Recommendation
# ==========================

def get_genre(age, mood):

    if age <= 15:

        if mood == "😊 Happy":
            return "Animation"

        elif mood == "😢 Sad":
            return "Family"

        elif mood == "🤩 Excited":
            return "Adventure"

        elif mood == "😎 Relaxed":
            return "Animation"

        elif mood == "😍 Romantic":
            return "Comedy"

        else:
            return "Fantasy"

    elif age <= 30:

        if mood == "😊 Happy":
            return "Comedy"

        elif mood == "😢 Sad":
            return "Drama"

        elif mood == "🤩 Excited":
            return "Action"

        elif mood == "😎 Relaxed":
            return "Adventure"

        elif mood == "😍 Romantic":
            return "Romance"

        else:
            return "Horror"

    elif age <= 50:

        if mood == "😊 Happy":
            return "Comedy"

        elif mood == "😢 Sad":
            return "Drama"

        elif mood == "🤩 Excited":
            return "Thriller"

        elif mood == "😎 Relaxed":
            return "Drama"

        elif mood == "😍 Romantic":
            return "Romance"

        else:
            return "Crime"

    else:

        if mood == "😊 Happy":
            return "Drama"

        elif mood == "😢 Sad":
            return "Drama"

        elif mood == "🤩 Excited":
            return "Adventure"

        elif mood == "😎 Relaxed":
            return "History"

        elif mood == "😍 Romantic":
            return "Romance"

        else:
            return "Mystery"
# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 AI Movie Recommendation System")
st.markdown("### Find your next favorite movie using AI!")
st.write("---")

# ==========================
# Custom CSS
# ==========================
st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

h1{
    text-align:center;
    color:#ff4b4b;
}

.stButton>button{
    width:100%;
    background-color:#ff4b4b;
    color:white;
    font-size:18px;
    border-radius:10px;
    height:50px;
}

.stButton>button:hover{
    background-color:#ff1f1f;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Sidebar
# ==========================
st.sidebar.title("👤 User Profile")

name = st.sidebar.text_input("Enter Your Name")

age = st.sidebar.slider(
    "Select Age",
    10,
    80,
    18
)

mood = st.sidebar.selectbox(
    "Current Mood",
    [
        "😊 Happy",
        "😍 Romantic",
        "🤩 Excited",
        "😢 Sad",
        "😎 Relaxed",
        "😱 Horror"
    ]
)

st.sidebar.success("Profile Saved")

# ==========================
# Main Title
# ==========================
st.title("🎬 AI Movie Recommendation System")

st.markdown(
"""
Welcome to your **AI Movie Recommendation Website**.

Choose your favourite movie and click **Recommend**.
"""
)

# ==========================
# Movie Selection
# ==========================
movie_list = movies["title"].values

selected_movie = st.selectbox(
    "🎥 Search or Select a Movie",
    movie_list
)

# ==========================
# Recommend Button
# ==========================

if st.button("🎬 Recommend Movies"):

    selected_genre = get_genre(age, mood)
    recommendations = recommend(selected_movie, selected_genre)

    st.success(f"Hello {name if name else 'User'} 👋")

    st.write(f"🎂 Age : **{age}**")
    st.write(f"😊 Mood : **{mood}**")
    st.write(f"🎭 Recommended Genre : **{selected_genre}**")

    st.divider()

    st.subheader("⭐ Recommended Movies")

    if len(recommendations) == 0:
        st.warning("No movies found for the selected genre.")

    else:

        col1, col2 = st.columns(2)

        for index, movie in enumerate(recommendations):

            if index % 2 == 0:
                with col1:
                    st.info(
    f"""
🎬 {movie['title']}

⭐ IMDb Rating : {movie['rating']}

📅 Year : {movie['year']}
"""
)
            else:
                with col2:
                    st.info(
    f"""
🎬 {movie['title']}

⭐ IMDb Rating : {movie['rating']}

📅 Year : {movie['year']}
"""
)

# ==========================
# Footer
# ==========================
st.divider()

st.markdown(
"""
<center>

Made with ❤️ by **Pavani Naga Divya**

AI Movie Recommendation System • 2026

</center>
""",
unsafe_allow_html=True
)