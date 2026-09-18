import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:

    def __init__(self, data_path):

        self.data_path = data_path

        # --------------------------------
        # 1. Load Dataset
        # --------------------------------

        self.movies = pd.read_csv(data_path)

        # Remove extra spaces from column names
        self.movies.columns = (
            self.movies.columns
            .str.strip()
            .str.lower()
        )

        print("Dataset columns:")
        print(self.movies.columns.tolist())

        # --------------------------------
        # 2. Check Required Columns
        # --------------------------------

        required_columns = [
            "title",
            "genres",
            "overview"
        ]

        for column in required_columns:

            if column not in self.movies.columns:

                raise ValueError(
                    f"Required column '{column}' "
                    f"not found in dataset.\n"
                    f"Available columns: "
                    f"{self.movies.columns.tolist()}"
                )

        # --------------------------------
        # 3. Handle Missing Values
        # --------------------------------

        self.movies["title"] = (
            self.movies["title"]
            .fillna("")
            .astype(str)
        )

        self.movies["genres"] = (
            self.movies["genres"]
            .fillna("")
            .astype(str)
        )

        self.movies["overview"] = (
            self.movies["overview"]
            .fillna("")
            .astype(str)
        )

        # --------------------------------
        # 4. Combine Movie Features
        # --------------------------------

        self.movies["features"] = (
            self.movies["genres"] + " " +
            self.movies["overview"]
        )

        # --------------------------------
        # 5. TF-IDF Vectorization
        # --------------------------------

        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        self.feature_matrix = (
            self.vectorizer.fit_transform(
                self.movies["features"]
            )
        )

        # --------------------------------
        # 6. Calculate Cosine Similarity
        # --------------------------------

        self.similarity_matrix = (
            cosine_similarity(
                self.feature_matrix
            )
        )

        # --------------------------------
        # 7. Movie Title -> Index
        # --------------------------------

        self.movie_indices = pd.Series(
            self.movies.index,
            index=self.movies["title"]
            .str.lower()
            .str.strip()
        ).drop_duplicates()

        print(
            f"\nLoaded {len(self.movies)} movies successfully."
        )


    # ====================================
    # Recommendation Function
    # ====================================

    def recommend(self, movie_title, n=5):

        movie_title = (
            movie_title
            .lower()
            .strip()
        )

        # Check movie exists
        if movie_title not in self.movie_indices:

            return pd.DataFrame()

        # Get movie index
        movie_index = self.movie_indices[
            movie_title
        ]

        # --------------------------------
        # Similarity Scores
        # --------------------------------

        similarity_scores = list(
            enumerate(
                self.similarity_matrix[
                    movie_index
                ]
            )
        )

        # Sort highest similarity first
        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        # Remove selected movie
        similarity_scores = (
            similarity_scores[1:n + 1]
        )

        # --------------------------------
        # Get Movie Indexes
        # --------------------------------

        movie_indexes = [
            index
            for index, score
            in similarity_scores
        ]

        # --------------------------------
        # Create Recommendation DataFrame
        # --------------------------------

        recommendations = self.movies.iloc[
            movie_indexes
        ][
            ["title", "genres"]
        ].copy()

        # Add similarity score
        recommendations["similarity"] = [
            round(score, 3)
            for index, score
            in similarity_scores
        ]

        return recommendations


# ========================================
# Test the Recommendation Engine
# ========================================

if __name__ == "__main__":

    print("\nStarting Movie Recommendation Engine...\n")

    recommender = MovieRecommender(
        "data/movies.csv"
    )

    results = recommender.recommend(
        "Interstellar",
        5
    )

    print(
        "\nRecommended Movies:\n"
    )

    if results.empty:

        print(
            "Movie not found."
        )

    else:

        print(
            results.to_string(
                index=False
            )
        )