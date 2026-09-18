import streamlit as st
from src.recommender import MovieRecommender


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Movie Recommendation Engine",
    page_icon="🎬",
    layout="centered"
)


# ==========================================
# LOAD RECOMMENDER
# ==========================================

@st.cache_resource
def load_recommender():

    return MovieRecommender(
        "data/movies.csv"
    )


recommender = load_recommender()


# ==========================================
# HEADER
# ==========================================

st.title("🎬 AI Movie Recommendation Engine")

st.write(
    "Find movies similar to your favorite movie "
    "using Machine Learning."
)

st.divider()


# ==========================================
# MOVIE SELECTION
# ==========================================

movie_titles = sorted(
    recommender.movies["title"]
    .dropna()
    .unique()
    .tolist()
)


selected_movie = st.selectbox(
    "🎞️ Select a movie",
    movie_titles
)


# ==========================================
# NUMBER OF RECOMMENDATIONS
# ==========================================

number_of_movies = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5
)


# ==========================================
# RECOMMEND BUTTON
# ==========================================

if st.button(
    "🚀 Recommend Movies",
    use_container_width=True
):

    recommendations = recommender.recommend(
        selected_movie,
        number_of_movies
    )

    if recommendations.empty:

        st.error(
            "Movie not found. Please select another movie."
        )

    else:

        st.success(
            f"Recommendations based on: {selected_movie}"
        )

        st.subheader(
            "🎯 Recommended Movies"
        )

        for _, movie in recommendations.iterrows():

            st.markdown(
                f"""
                ### 🎬 {movie['title']}

                **Genre:** {movie['genres']}

                **Similarity Score:** {movie['similarity']}

                ---
                """
            )


# ==========================================
# FOOTER
# ==========================================

st.caption(
    "Powered by Python, Pandas, Scikit-learn and TF-IDF"
)
