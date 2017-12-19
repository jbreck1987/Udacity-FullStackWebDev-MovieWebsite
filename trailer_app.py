import movie_helper
import fresh_tomatoes

"""
    trailer_app.py is the 'Main' module for this application.
    It is used to instantiate objects of type 'Movie' and then creates
    a static webpage that displays the movies that are created. 
"""

# Instantiate all the movies to be displayed on the webpage
inception_movie = movie_helper.Movie('Inception',
                                     'Team journeys into dreams '
                                     'to solve mysteries',
                                     'https://youtu.be/YoHD9XEInc0?t=6s',
                                     'https://images-na.ssl-'
                                     'images-amazon.com/images/'
                                     'M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFt'
                                     'ZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,'
                                     '675,1000_AL_.jpg')


dogma_movie = movie_helper.Movie('Dogma',
                                 'Plain Jane tries to '
                                 'foil plans of two angels '
                                 'trying to backdoor their way '
                                 'back into Heaven',
                                 'https://youtu.be/20CRw3XdETA?t=11s',
                                 'https://images-na.ssl-images-amazon.'
                                 'com/images/M/MV5BYzAyOWUyZjQtNDBiMy0'
                                 '0ZDExLTgwNmMtZDdmY2ViNz'
                                 'kyN2Y0XkEyXkFqcGdeQXVyMTQxNzM'
                                 'zNDI@._V1_SY1000_CR0'
                                 ',0,679,1000_AL_.jpg')


big_lebowski_movie = movie_helper.Movie('The Big Lebowski',
                                        '"The Dude" just wants '
                                        'someone to pay for his rug',
                                        'https://youtu.be/ngV0RBhGZmE?t=6s',
                                        'https://images-na.ssl-images-amazon'
                                        '.com/images/M/MV5BZTFjMjBiYzItNzU5YS'
                                        '00MjdiLWJkOTktNDQ3MTE3ZjY2YTY5XkEyXkF'
                                        'qcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0'
                                        ',0,665,1000_AL_.jpg')


american_pie_movie = movie_helper.Movie('American Pie',
                                        'Group of HS seniors try and lose '
                                        'their virginity before college',
                                        'https://youtu.be/iUZ3Yxok6N8?t=8s',
                                        'https://images-na.ssl-images-amazon'
                                        '.com/images/M/MV5BMTg3ODY5ODI1NF5BMl'
                                        '5BanBnXkFtZTgwMTkxNTYxMTE@._V1_SY100'
                                        '0_CR0,0,675,1000_AL_.jpg')


blade_movie = movie_helper.Movie('Blade',
                                 'A bad, bad Vampire vs. evil vampires',
                                 'https://youtu.be/kaU2A7KyOu4?t=6s',
                                 'https://images-na.ssl-images-amazon.c'
                                 'om/images/M/MV5BMTQ4MzkzNjcxNV5BMl5Ba'
                                 'nBnXkFtZTcwNzk4NTU0Mg@@._V1_.jpg')


the_matrix_movie = movie_helper.Movie('The Matrix',
                                      'Is reality really real?',
                                      'https://youtu.be/vKQi3bBA1y8?t=5s',
                                      'https://images-na.ssl-images-amazon'
                                      '.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi'
                                      '00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYW'
                                      'dlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY'
                                      '1000_CR0,0,665,1000_AL_.jpg')


# Create a List including all Movie objects created above.
movie_list = [inception_movie, big_lebowski_movie, blade_movie,
              the_matrix_movie, american_pie_movie, dogma_movie]


# Pass List with all Movie objects into the function that
# creates and opens the movies page.
fresh_tomatoes.open_movies_page(movie_list)
