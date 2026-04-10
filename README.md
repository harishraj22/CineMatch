# 🎬 CineMatch — AI Movie Recommendation System

CineMatch is an AI-powered movie recommendation web application that suggests similar movies based on content similarity. The system uses Natural Language Processing (NLP) and cosine similarity to recommend movies and displays posters, ratings, and overview using the TMDB API.

This project demonstrates a complete **end-to-end Machine Learning workflow** including data preprocessing, model building, API integration, UI development, and deployment.

---

# 🚀 Features

* 🔍 Search and filter movies using smart dropdown
* 🎯 Content-based movie recommendation
* 🖼️ Movie posters using TMDB API
* ⭐ Movie ratings
* 📝 Movie overview
* ⚡ Fast API calls with caching
* 🎨 Dark Netflix-style UI
* 🌍 Deployment ready

---

# 🧠 How It Works

1. Movie dataset is loaded
2. Important features combined into tags
3. Text converted to vectors using CountVectorizer
4. Cosine similarity calculated
5. Similar movies ranked
6. TMDB API fetches poster & details
7. Streamlit UI displays recommendations

---

# 🏗️ Project Architecture

```
Dataset
   ↓
Data Preprocessing
   ↓
Feature Engineering (tags)
   ↓
Vectorization (CountVectorizer)
   ↓
Cosine Similarity
   ↓
Recommendation Engine
   ↓
Streamlit UI
   ↓
TMDB API (Poster + Rating + Overview)
```

---

# 🛠️ Tech Stack

**Programming Language**

* Python

**Libraries Used**

* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Requests
* Pickle
* Python-dotenv

**Machine Learning**

* CountVectorizer
* Cosine Similarity
* NLP (Content Based Filtering)

**API**

* TMDB Movie API

---

# 📂 Project Structure

```
cinematch/
│
├── app.py
├── build_model.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---


### Install dependencies

```
pip install -r requirements.txt
```

### Run the application

```
streamlit run app.py
```

---

# 🔑 Environment Variables

Create a `.env` file in root directory:

```
TMDB_API_KEY=your_api_key_here
```

Or configure the API key in Streamlit Cloud Secrets when deploying.

---

Each recommendation includes:

* Movie Poster
* Rating
* Overview
* Similarity-based suggestion

---

# 📸 Application Preview



```
![CineMatch Screenshot](https://github.com/user-attachments/assets/e26a3023-3f01-4660-8a7d-64105e8352b8)
```

---

# 🌍 Live Demo

```
https://cinematch-hwood.streamlit.app/
```



---



# 👨‍💻 Author

**Harish Raj**

---

# ⭐ Support

If you like this project, consider giving it a star ⭐ on GitHub.
