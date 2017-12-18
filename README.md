# Fresh Tomatoes!

Fresh Tomatoes! is a simple application that creates a static webpage showing six of my favorite movies and enables you to watch their trailers on YouTube!

### Pre-requisites

To generate the webpage, you must download the following modules from this repo:

    fresh_tomatoes.py
    movie_helper.py
    trailer_app.py
    
Once downloaded, make sure the modules are in the same directory.

### Operation
The `fresh_tomatoes.py` module is used to supply the style and structure of the webpage, along with the functions that are used to dynamically build a webpage, based off of the movies objects created in the `trailer_app.py` module. The class for defining the movie objects created in the `trailer_app.py` module is defined in the `movie_helper.py` module.

### Usage
To create and open the webpage, simply run the `trailer_app.py` module. It should dynamically create a new HTML file in the same directory and attempt to open it in a new browser tab.
