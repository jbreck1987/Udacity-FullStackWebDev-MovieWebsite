# Fresh Tomatoes!

Fresh Tomatoes! is a simple application that creates a static webpage showing six of my favorite movies and enables you to watch their trailers on YouTube!

### Pre-requisites

This small applicaton is a project to help me learn basic OOP and also how to connect to and interact with an API. There are two versions in this repo: a version that uses manual input to get the data for the webpage and a version that uses calls to an API to get the data. To generate the webpage with manual input, you must download the following modules from this repo:

    fresh_tomatoes.py
    movie_helper.py
    trailer_app.py
    
For the API version, you must download the following modules from this repo:

    /api-version/fresh_tomatoes2.py
    /api-version/movie_helper2.py
    /api-version/trailer_app2.py

The API version also requires the Python "requests" module.
    
Once downloaded, make sure the modules of the same version are in the same directory.

### Operation
The `fresh_tomatoes(2).py` module is used to supply the style and structure of the webpage, along with the functions that are used to dynamically build a webpage, based off of the movies objects created in the `trailer_app(2).py` module. The class for defining the movie objects created in the `trailer_app(2).py` module is defined in the `movie_helper(2).py` module.

If you plan on using the API version, you must create an account at https://www.themoviedb.org and request an API Key that is used for authentication of the requests. The API key will need to be added to the `trailer_app2.py` module.

### Usage
To create and open the webpage, simply run the `trailer_app(2).py` module. It should dynamically create a new HTML file in the same directory and attempt to open it in a new browser tab.

### Acknowledgements
This product uses the TMDb API but is not endorsed or certified by TMDb.
