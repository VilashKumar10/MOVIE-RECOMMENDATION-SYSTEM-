# 🎬 Movie Recommender System

A web-based Movie Recommendation System built with Streamlit and The Movie Database (TMDB) API. This application helps users discover movies by providing personalized recommendations based on their selected movie and displays movie posters for an enhanced browsing experience.

## 🚀 Features

* 🎥 Browse popular movies from TMDB
* 🔍 Search movies by title
* 🤖 Get movie recommendations based on selected movies
* 🖼️ Display movie posters and titles
* 🌐 Real-time data fetched from TMDB API
* 🔄 Fallback demo data when API is unavailable
* 📱 Simple and responsive Streamlit interface

## 🛠️ Technologies Used

* Python
* Streamlit
* TMDB API
* Requests Library

## 📂 Project Structure

```text
movie-recommender/
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up TMDB API Key

Create a `.env` file and add:

```env
TMDB_API_KEY=your_tmdb_api_key
```

### 4. Run the Application

```bash
streamlit run app.py
```

## 🎯 How It Works

1. Fetches popular movies from TMDB.
2. User selects or searches for a movie.
3. The application retrieves similar movie recommendations.
4. Recommended movies are displayed with posters and titles.
5. If the API is unavailable, the system automatically uses demo data.

## 📸 Features Preview

* Popular Movie Selection
* Movie Search Functionality
* Recommendation Engine
* Poster Display
* Error Handling and Offline Demo Mode

## 🔮 Future Improvements

* Content-based recommendation system using machine learning
* User authentication and watchlists
* Movie ratings and reviews
* Genre-based filtering
* Trailer integration
* Personalized recommendations

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

## 📜 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

Developed to help users discover movies and explore new entertainment options through an interactive recommendation system.

⭐ If you like this project, consider giving it a star on GitHub!
