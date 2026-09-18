# 🎬 AI Movie Recommendation Engine

An AI-powered movie recommendation system built with **Python, Pandas, Scikit-learn, and Streamlit**.

The system recommends movies based on their content using **TF-IDF vectorization** and **Cosine Similarity**.

---

## 📌 Project Overview

The AI Movie Recommendation Engine analyzes movie information such as:

* Movie title
* Genres
* Overview/description

It converts movie content into numerical vectors using **TF-IDF** and calculates the similarity between movies using **Cosine Similarity**.

When a user selects a movie, the system finds and displays the most similar movies.

### Example

If the user selects:

> Interstellar

The system may recommend:

```text
The Martian
Gravity
Arrival
Inception
Avatar
```

---

## 🚀 Features

* 🎬 Movie selection through an interactive UI
* 🤖 Machine-learning-based recommendations
* 🔍 Content-based filtering
* 📊 TF-IDF feature extraction
* 📐 Cosine similarity calculation
* ⭐ Similarity score for every recommendation
* 🎨 Interactive Streamlit interface
* 🐍 Built completely with Python

---

## 🛠️ Technology Stack

| Technology        | Purpose                      |
| ----------------- | ---------------------------- |
| Python            | Main programming language    |
| Pandas            | Data processing              |
| NumPy             | Numerical operations         |
| Scikit-learn      | Machine learning             |
| TF-IDF            | Text feature extraction      |
| Cosine Similarity | Movie similarity calculation |
| Streamlit         | Web interface                |

---

## 📂 Project Structure

```text
movie-recommendation-engine/
│
├── data/
│   └── movies.csv
│
├── src/
│   ├── __init__.py
│   └── recommender.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

The recommendation pipeline works in the following steps:

```text
Movie Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Combine Genres + Overview
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Movie Feature Matrix
      │
      ▼
Cosine Similarity
      │
      ▼
Find Similar Movies
      │
      ▼
Top-N Recommendations
      │
      ▼
Streamlit Interface
```

---

## 🔬 Machine Learning Method

### 1. TF-IDF

TF-IDF stands for **Term Frequency-Inverse Document Frequency**.

It converts movie text into numerical feature vectors.

The system combines:

```text
Genres + Movie Overview
```

For example:

```text
Action Sci-Fi Thriller
A computer hacker discovers that reality is not what it seems.
```

This text is transformed into numerical features.

---

### 2. Cosine Similarity

After converting the movie descriptions into vectors, cosine similarity is used to determine how similar two movies are.

The formula is:

$$
Similarity(A,B)=
\frac{A\cdot B}
{||A||\,||B||}
$$

A higher value means the movies have more similar content.

---

## 💻 Installation

### 1. Clone the project

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd movie-recommendation-engine
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

---

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Recommendation Engine

To test the recommendation model directly:

```bash
python src/recommender.py
```

You should see output similar to:

```text
Starting Movie Recommendation Engine...

Dataset columns:
['title', 'genres', 'overview']

Loaded movies successfully.

Recommended Movies:

The Martian
Gravity
Arrival
Inception
Avatar
```

---

## 🌐 Run the Web Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

## 📊 Dataset Format

The `movies.csv` file should contain the following columns:

```text
title
genres
overview
```

Example:

```csv
title,genres,overview
Interstellar,"Adventure Drama Sci-Fi","A group of explorers travel through space searching for a new home."
The Martian,"Adventure Drama Sci-Fi","An astronaut becomes stranded on Mars and must find a way to survive."
Gravity,"Drama Sci-Fi Thriller","An astronaut struggles to survive after an accident in space."
```

---

## 🎯 Recommendation Example

### Input

```text
Movie: Interstellar
Recommendations: 5
```

### Output

```text
Recommended Movies

1. The Martian
2. Gravity
3. Arrival
4. Inception
5. Avatar
```

Each recommendation also includes a similarity score.

---

## 📈 Future Improvements

The current version uses content-based filtering. Future versions can include:

### Collaborative Filtering

Use user ratings and viewing history to understand user preferences.

```text
User
 │
 ├── Rated Movie A → 5 ⭐
 ├── Rated Movie B → 4 ⭐
 └── Rated Movie C → 5 ⭐
             │
             ▼
     User Preference Model
             │
             ▼
      Movie Recommendations
```

### Hybrid Recommendation

Combine multiple recommendation techniques:

```text
Content-Based Filtering
          +
Collaborative Filtering
          +
User Preferences
          +
Movie Popularity
          │
          ▼
     Hybrid Model
```

### Deep Learning

TensorFlow/Keras can be added for:

* User embeddings
* Movie embeddings
* Neural collaborative filtering
* Personalized rating prediction

### Additional Features

* User accounts
* Movie ratings
* Like/dislike system
* Watch history
* Genre preferences
* Movie posters
* Movie trailers
* Personalized recommendations
* Recommendation evaluation
* REST API using FastAPI

---

## 📊 Possible Evaluation Metrics

For future versions, the recommendation system can be evaluated using:

* RMSE
* MAE
* Precision@K
* Recall@K
* F1@K
* NDCG@K

These metrics can help compare different recommendation algorithms.

---

## 🎓 Learning Objectives

This project demonstrates practical implementation of:

* Data preprocessing
* Natural Language Processing
* Feature extraction
* TF-IDF
* Vector similarity
* Machine learning
* Recommendation systems
* Python programming
* Streamlit application development

---

## 🔮 Future Architecture

```text
                 MOVIE DATA
                     │
                     ▼
              Data Preprocessing
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   Content Features       User Behavior
          │                     │
          ▼                     ▼
       TF-IDF            Collaborative
          │                 Filtering
          ▼                     │
 Cosine Similarity               │
          │                     │
          └──────────┬──────────┘
                     ▼
               Hybrid Model
                     │
                     ▼
             Neural Model
              (TensorFlow)
                     │
                     ▼
          Personalized Results
                     │
                     ▼
             Streamlit App
```

---

## 👨‍💻 Author

**Mohit Prajapati**

AI Movie Recommendation Engine

Built using Python and Machine Learning.

---

## 📜 License

This project is intended for educational and learning purposes.

```

**Note:** README mein `<your-repository-url>` ko apne actual GitHub repository URL se replace kar dena.
```
