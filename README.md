# Movie API

Welcome to the **Movie API**! This API allows you to fetch movie details and get a list of top 250 movies.

## Base URL

**https://movie-api-omega-three.vercel.app/**

## Endpoints

### 1. **Get Movie Details by Title**

GET /api/movie/<title>

**Description:**  
Fetch detailed information about a movie by providing its title.

**URL Parameters:**

- `title`: The title of the movie you want to search for. The title should be URL-encoded.

**Response Format:**

The API will return a JSON response with movie details such as:
- Title
- Year of release
- Actors
- A brief description

**Example Request:**

GET https://movie-api-omega-three.vercel.app/api/movie/Inception



**Example Response:**
```json
[
  {
    "title": "Inception",
    "year": "2010",
    "actors": "Leonardo DiCaprio, Joseph Gordon-Levitt",
    "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster."
  }
]
......... Keep in Mind that the Description is also a nested structre of json with various parameters
```


2. **Get Top 250 Movies**

```
GET /api/movie/top250
```

**Description:**  
Fetch a list of the top 250 movies based on IMDb rankings.

**Response Format:**

The API will return a JSON response containing an array of top 250 movies, with each movie's title, year of release, actors, and a brief description.

**Example Request:**
```
GET https://movie-api-omega-three.vercel.app/api/movie/top250
```

**Example Response:**
```json
[
  {
    "title": "The Shawshank Redemption",
    "year": "1994",
    "actors": "Tim Robbins, Morgan Freeman",
    "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
  },
  {
    "title": "The Godfather",
    "year": "1972",
    "actors": "Marlon Brando, Al Pacino",
    "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
  }
  // More movies...
]
```



## License

This API is open source and available for personal or commercial use. Feel free to contribute or modify it as needed.

---

### How to Contribute

If you'd like to contribute to this API, you can fork the repository, make your changes, and submit a pull request. Please ensure your code is well-documented and follows the project's coding style.
```



