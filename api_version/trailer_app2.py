from movie_helper2 import Movie
from fresh_tomatoes2 import open_movies_page

api_key = ''

blade_id = 'tt0120611'
dogma_id = 'tt0120655'
lebowski_id = 'tt0118715'
the_matrix_id = 'tt0133093'
american_pie_id = 'tt0163651'
inception_id = 'tt1375666'

appends = ('videos',)

blade_movie = Movie(blade_id, api_key, append_vals=appends)
blade_movie.build()

dogma_movie = Movie(dogma_id, api_key, append_vals=appends)
dogma_movie.build()

lebowski_movie = Movie(lebowski_id, api_key, append_vals=appends)
lebowski_movie.build()

the_matrix_movie = Movie(the_matrix_id, api_key, append_vals=appends)
the_matrix_movie.build()

american_pie_movie = Movie(american_pie_id, api_key, append_vals=appends)
american_pie_movie.build()

inception_movie = Movie(inception_id, api_key, append_vals=appends)
inception_movie.build()

movies = (blade_movie, dogma_movie, lebowski_movie, the_matrix_movie,
          american_pie_movie, inception_movie)

open_movies_page(movies)
