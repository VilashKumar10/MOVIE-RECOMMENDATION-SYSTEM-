import requests
import streamlit as st
import os


API_KEY = os.getenv("TMDB_API_KEY", "935814bedfd47e116e78f5a0e1e70a4a")
BASE_URL = "https://api.themoviedb.org/3"

DEMO_MOVIES = [
	{"id": 27205, "title": "Inception", "poster_path": "/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg"},
	{"id": 603, "title": "The Matrix", "poster_path": "/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
	{"id": 155, "title": "The Dark Knight", "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
	{"id": 157336, "title": "Interstellar", "poster_path": "/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"},
	{"id": 120, "title": "The Lord of the Rings: The Fellowship of the Ring", "poster_path": "/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg"},
]

DEMO_RECOMMENDATIONS = {
	"Inception": [
		{"title": "Interstellar", "poster_path": "/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"},
		{"title": "The Matrix", "poster_path": "/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
		{"title": "The Dark Knight", "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
	],
	"The Matrix": [
		{"title": "Inception", "poster_path": "/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg"},
		{"title": "Interstellar", "poster_path": "/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"},
		{"title": "The Dark Knight", "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
	],
	"The Dark Knight": [
		{"title": "Inception", "poster_path": "/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg"},
		{"title": "The Matrix", "poster_path": "/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
		{"title": "Interstellar", "poster_path": "/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"},
	],
	"Interstellar": [
		{"title": "Inception", "poster_path": "/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg"},
		{"title": "The Dark Knight", "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
		{"title": "The Matrix", "poster_path": "/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
	],
	"The Lord of the Rings: The Fellowship of the Ring": [
		{"title": "The Lord of the Rings: The Two Towers", "poster_path": "/5VTN0pR8gcqV3EPUHHfMGnJYN9L.jpg"},
		{"title": "The Lord of the Rings: The Return of the King", "poster_path": "/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg"},
		{"title": "Harry Potter and the Sorcerer's Stone", "poster_path": "/wuMc08IPKEatf9rnMNXvIDxqP4W.jpg"},
	],
}


def fetch_popular_movies():
	url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page=1"
	try:
		response = requests.get(url, timeout=5)
		response.raise_for_status()
		data = response.json()
		results = data.get("results", [])
		return results or DEMO_MOVIES
	except requests.RequestException:
		return DEMO_MOVIES


def search_movie(query):
	url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={query}"
	try:
		response = requests.get(url, timeout=5)
		response.raise_for_status()
		data = response.json()
		results = data.get("results", [])
		if results:
			return results
	except requests.RequestException:
		pass

	query_lower = query.casefold()
	return [movie for movie in DEMO_MOVIES if query_lower in movie["title"].casefold()]


def fetch_recommendations(movie_id, movie_title=None):
	url = f"{BASE_URL}/movie/{movie_id}/recommendations?api_key={API_KEY}&language=en-US&page=1"
	try:
		response = requests.get(url, timeout=5)
		response.raise_for_status()
		data = response.json()
		results = data.get("results", [])
		if results:
			return results
	except requests.RequestException:
		pass

	if movie_title and movie_title in DEMO_RECOMMENDATIONS:
		return DEMO_RECOMMENDATIONS[movie_title]
	return []


def get_poster_url(poster_path):
	if poster_path:
		return f"https://image.tmdb.org/t/p/w500{poster_path}"
	return "https://via.placeholder.com/500x750?text=No+Poster"


def main():
	st.title(" Movie Recommender (API Based)")

	popular_movies = []
	try:
		popular_movies = fetch_popular_movies()
	except requests.RequestException:
		st.error("Could not load popular movies right now.")

	if not popular_movies:
		popular_movies = DEMO_MOVIES
		st.info("Using demo movies because the live API could not be reached.")

	movie_names = [movie["title"] for movie in popular_movies if movie.get("title")]
	if not movie_names:
		st.warning("No movie titles were returned by the API.")
		return

	selected_movie_name = st.selectbox("Select or type a movie name", movie_names)

	if st.button("Show Recommendations"):
		try:
			search_results = search_movie(selected_movie_name)
		except requests.RequestException:
			st.error("Movie search failed. Please try again.")
			return

		if search_results:
			movie_titles = [movie["title"] for movie in search_results if movie.get("title")]
			if not movie_titles:
				st.warning("No movie titles were returned for that search.")
				return

			selected_movie_title = st.selectbox("Select the movie", movie_titles)
			selected_movie = next(
				movie for movie in search_results if movie.get("title") == selected_movie_title
			)

			try:
				recommendations = fetch_recommendations(
					selected_movie["id"], selected_movie.get("title")
				)
			except requests.RequestException:
				st.error("Could not fetch recommendations right now.")
				return

			if recommendations:
				cols = st.columns(5)
				for index in range(min(5, len(recommendations))):
					with cols[index]:
						st.text(recommendations[index].get("title", "Untitled"))
						st.image(get_poster_url(recommendations[index].get("poster_path")))
			else:
				st.warning("No recommendations found.")
		else:
			st.error("Movie not found. Try another title.")


if __name__ == "__main__":
	main()