# TinderForMovies

How to start the app - You can use 1 on the following methods :


1.Download project from Github.
Next
Do one of the following:
 On the Welcome Screen of PyCharm, click the Open link.
 From the main menu of PyCharm, select File |Open.
In the Open File or Project dialog that opens, find location of the desired project directory. The PyCharm project are marked with  and projects created in other IDEs or in a dedicated editor are marked with .
If you select a non-PyCharm directory, PyCharm creates a new IDE project and sets up a Python interpreter.
Click OK.

OR

2.Open a project from Gitfrom on PyCharm:

Do one of the following:
 On the Welcome Screen of PyCharm, click the Get from Version Control link.
 From the main menu, select VCS | Get from Version Control.
Select the version control system where your project is stored. Here it is Git:
Specify the path to the repository and select the directory to which a project will be cloned. Alternatively, you can select GitHub on the left, login using your credentials, and select any project you want to work with.
Click Clone.

Finally, complie the program on PyCharm and run app.py. That will open the webapp on your local server on the specified port 1234.



Assignment Report -

The Tinder for Movies website has been made to give users the best experience when discovering new movies, sorting movies out according to their preference and searching up new movies. The users can watch the trailers of the top rated hollywood and bollywood movies and also search movies from all over the world.The users of this website can get to know movie ratings and watch trailers and according to their choices, place them into different categories namely - favourites, unwatched and liked. The users also have the option to unlike videos.
The website uses a built in machine-learning algorithm to show movies to the user based on their preferences. The users can also search up movies in the search bar which uses the IMDB API and Youtube API to discover movies from all over the world closest to your search query and give you the most relevant movie trailers in the results. The users also have the option to discover the top rated movies both in hollywood and bollywood. Besides all the features, the users can share the trailers of these movies on social media websites such as facebook and twitter. The website has an aesthetically appealing user interface and is fully secure. Besides that, the website has been enhanced for performance where the movies of his choice are cached for the best user experience.

Usage -

The homepage of the website is where you can login in to the TinderforMovies website or if you are a new member, create a new account. One you have done that, you are redirected to the main page where you can use the website ust like Tinder.
The heart button means "Add to Favourites"
the tick button means "Like"
the eye button means "Add to Unwatched"
the button with thecut sign - "Dislike"

To share a movie trailer, you can click on the Facebook/Twitter button on the home page. The home page also has a search bar to search movie trailers from all over the world.

Tools Used - 

Back-End - Python,Flask,MongoDB
Libraries - pymongo,Flask-Cache,google api,IMDB api
Front End - HTML,CSS,Bootstrap,Jinja,Javascript

App Structure - 

The application has been developed following industry standards using a Pycharm Virtual Environment:
The src folder of the application has different directories, each for a different purpose - 

 “Common” - directory for database interactions and database creation of the TinderForMovies website
“Model” - for the model classes namely Movie and User
“Templates” - for html files 
“Static” - for javascript, css, and image file”
“Requirements.txt” - libraries/frameworks used in the assignment for example - Pymongo,Flask
“app.py” - contains the application with all endpoints

Steps taken to create the application -

A virtual environment had to be created on Pycharm and the extensions for Flask had to be installed. Next the application had to be integrated with the MongoDB server which was done with a connection string which is unique for every user. The Database class allows you to insert,find or remove data from the MongoDB server. The library used to integrate it with Python is PyMongo.After the database integration, the app structure was created starting with the model classes - Movie and User. The flask application with all the endpoints were made along with the front end for system testing purposes.

Youtube API -

The youtube API has been used to create the movie database for the application and alos search movie trailers from all over the world and display relevant results. The youtube api is integrated with the Google api and uses a secret api-key which is unique to every user. This secret key has been used to access the Youtube API from the Flask application. The search bar is integrated with this Youtube API  which uses some carefully chosen parameters for example - regionCode,video type and query parameters to display relevant results. The application uses this api to redirect to the available movies or trailers on youtube or IMDB. These trailers can be shared on Facebook and Twitter.
 
IMDB API -

The IMDB api along with WebScraping techniques and the Youtube API  has been used to create the movie database for the TinderforMovies website. The api extracts the top hollywood and bollywood movies from the IMDB server and uses web scraping (BeautifulSoup library) to extract relevant information about the movie and add it to the website. Most movie trailers are available on IMDB and therefore when you want to watch a movie trailer or if you want to share the trailer of a movie, the imdb database is used. 

Security - 

The website has been made completely secure for its users. Every user has to register on the website with a valid email and is prompted if a proper email address is not given. Once the user enters his name, email and password; the details are stored in the MongoDB database where the passwords are saved using the salted hashing technique. Therefore the details and the preferences of the user are completely secure. Everytime a user logs into his account a session is created for that specific user which expires if the page is left idle for a long time or when he logs out. This way the user is also protected from injection attacks because a session is not created for that user.

Performance

The performance of the application has been tested with the help of a test class where all the endpoints of the server are tested for correct results. All errors that can arise are handled in the back-end model and database classes. The code is written in minimum complexity so that Database transactions are dealt with fast. The data from the Database is also cached for the best user experience. The data is cached for 5 seconds after which new memory (if any) is loaded to the main page.  


Caching

For Caching of data, The flask caching library has been used to cache the data from the database. The data is extracted from the database and is cached close to the server with a key prefix and a timeout for 5 seconds . This time has been chosen since it is the maximum time it can take to load data to the front end of the application.

Search Feature -

The search functionality has been implemented in the application with the help of the Youtube and IMDB api. These APIs are used to extract data from their specific databases along with the help of some web scraping techniques. The technique that I used to extract such data was with the help of the Beautiful Soup library which helps you parse html data. The search algorithm checks the database of TinderforMovies website for results and also provides relevant results from the Youtube database. Therefore, you can search up any movie and get relevant results.

Machine Learning -

A smart machine learning algorithm has been designed which filters movies based on the user’s choices. Once the user starts using the website, he likes,dislikes and adds them to his favourites etc. This data is stored in the database and the next movie which is suggested to the user is calculated from these parameters. The liked movies are given the highest preference and the the like genre and category of the movie is looked up in the database and a movie is suggested from those search results. The AI also removes duplicates and movies that have already been liked or disliked. This way , the user is always suggested a new movie of his preference. 

Tinder-Functionality -

The website has been designed just like the Tinder website where you are shown a movie and provided with 4 buttons in the main page. You can either like,dislike , add to favourites or add to the unwatched list for each movie. You can share the trailers of movies on social media sites such as Facebook and Twitter. 

Extra Features

Apart from the above mentioned features, the user can also explore top rated IMDB movies in the dropdown section. He has a choice of all top movies and top bollywood movies. The back-end to display movies according to genre has also been created which can allow the users to categorize movies according to the genre of his preference - Comedy, Crime, Animation etc

Front-end -

An aesthetically appealing front end has been created for the best user experience.The tools that are used to create the front end of the application are HTML,CSS,bootstrap and a little bit of Javascript. A frontend framework called Jinja was also used to integrate the backend with the front end.

Optimization solutions - 

The TinderforMovies database is not very vast and can be added with more movies from different regions of the world. The machine learning algorithm and the search algorithm can be enhanced to produce better results. More features such as dropdowns for categorizing movies according to genre and category can be added to the front end(back end already exists).
