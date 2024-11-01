# TinderForMovies

## Overview

TinderForMovies is a web application designed to enhance users' experience in discovering and exploring new movies. The application allows users to sort movies based on their preferences, watch trailers, and categorize them as favorites, unwatched, or liked. Users can search for movies globally through the IMDB and YouTube APIs, watch trailers, and share them on social media.

## Usage

To run the application, simply execute `app.py`. This will start the web app on your local server at the specified port (1234).

Upon visiting the homepage, users can log in to their account or create a new one. After logging in, they will be redirected to the main page, where they can explore and categorize movies. The following buttons are available for each movie:
- Heart: **Add to Favorites**
- Tick: **Like**
- Eye: **Add to Unwatched**
- Cut Sign: **Dislike**

Movies can also be shared on social media through buttons for Facebook and Twitter.

## Features

- **Personalized Recommendations**: The app uses machine learning to suggest movies based on user preferences, considering previous likes, dislikes, and favorites.
- **Global Search**: Users can search for movies through a search bar, with results powered by the IMDB and YouTube APIs, ensuring relevant and diverse results.
- **Top-Rated Movies**: Users can discover popular Hollywood and Bollywood movies, with additional options for different genres in a dropdown menu.
- **Social Sharing**: Share movie trailers directly to Facebook or Twitter from the app.

## Tools and Technology Stack

- **Back-End**: Python, Flask, MongoDB
- **Libraries**: `pymongo`, `Flask-Cache`, `google-api`, `IMDB-api`
- **Front-End**: HTML, CSS, Bootstrap, Jinja, JavaScript

## Application Structure

The project follows a modular structure with directories designated for different components:

- **Common**: Database interactions and creation.
- **Model**: Contains model classes (e.g., `Movie` and `User`).
- **Templates**: HTML files for the frontend.
- **Static**: Holds JavaScript, CSS, and image files.
- **Requirements.txt**: Lists dependencies (e.g., `Pymongo`, `Flask`).
- **app.py**: Main application file with all endpoints.

## Technical Details

### Database Integration
The application uses MongoDB as its primary database. The `Database` class handles database operations, and `PyMongo` enables integration with Flask. User details are securely stored using salted hashing, protecting sensitive information.

### APIs

1. **YouTube API**: Fetches and displays movie trailers in the app and supports global searches for movies.
2. **IMDB API**: Retrieves top Hollywood and Bollywood movies, with additional data parsing through BeautifulSoup for accurate movie information.

### Security and Performance

- **User Security**: User sessions are securely managed, preventing unauthorized access and SQL injection attacks.
- **Performance Optimization**: Data is cached using `Flask-Cache` for faster load times, and backend code has been optimized for minimal complexity.

### Front-End

A user-friendly front end is built using HTML, CSS, Bootstrap, and JavaScript, providing a responsive, visually appealing interface. Jinja is used to seamlessly integrate backend data with the frontend.

### Additional Features and Future Enhancements

The application could expand its database with movies from various global regions and further improve the recommendation algorithm for more accurate suggestions. Front-end dropdowns can be developed to allow users to filter movies by genre and category.
