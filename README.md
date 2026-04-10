🎬 CineMatch — AI Movie Recommendation System

CineMatch is a content-based movie recommendation system that suggests similar movies based on user selection. The app uses cosine similarity on movie metadata and integrates with the TMDB API to display posters, ratings, and descriptions.

The application is built with Streamlit and deployed as an interactive web app.

🚀 Features
Movie recommendation based on similarity
Searchable dropdown movie selector
Movie posters from TMDB API
Movie rating display
Movie overview description
Fast cached API calls
Clean Netflix-style UI
Streamlit interactive web app
Deployment-ready project
🧠 How It Works

The recommendation system follows these steps:

Load TMDB movie dataset
Combine important features (genre, keywords, cast, crew, overview)
Convert text into vectors using CountVectorizer
Compute cosine similarity between movies
Select top similar movies
Fetch posters, ratings, and overview from TMDB API
Display recommendations in Streamlit UI
🛠️ Tech Stack
Python
Pandas
Scikit-learn
Streamlit
TMDB API
Requests
Pickle
Cosine Similarity
NLP (CountVectorizer)
📂 Project Structure
movie-recommender/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Installation

Clone the repository

git clone https://github.com/yourusername/cinematch.git

Go to project folder

cd cinematch

Install dependencies

pip install -r requirements.txt

Run the app

streamlit run app.py
🔑 TMDB API Setup

Create a TMDB account and get your API key.

Then create .env file:

TMDB_API_KEY=your_api_key_here
🎯 Example

Input:

Interstellar

Output:

Gravity
The Martian
Ad Astra
Contact

With posters, ratings, and descriptions.
