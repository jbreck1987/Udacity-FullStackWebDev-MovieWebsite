import movie_helper

avatar_movie = movie_helper.Movie('Avatar',
                                  'Dude remotely controls an alien with his mind.',
                                  'https://youtu.be/5PSNL1qE6VY?t=8s',
                                  'bogus_url')

dogma_movie = movie_helper.Movie('Dogma',
                                 'Plain Jane tries to foil plans of two angels '
                                 'trying to backdoor their way back into Heaven',
                                 'https://youtu.be/20CRw3XdETA?t=11s',
                                 'bogus_url')
# avatar_movie.show_trailer()
print(dogma_movie.mov_story)
dogma_movie.show_trailer()
