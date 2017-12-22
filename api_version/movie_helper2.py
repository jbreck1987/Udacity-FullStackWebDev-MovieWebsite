import requests


class Movie(object):
    """
    Movie object that consumes "The Movie Database" API

    This class defines Movie objects and contains
    access to information typical to a movie, such as:
    Title, Poster Art, Trailer URLs, etc. The data is all
    pulled from "The Movie Database" API

    Attributes:
        movie_id: Unsigned integer that uniquely IDs a movie within
            the movie database. Can be found on the website.
            This is a required argument.
        api_key: String used for authentication for all calls to the API.
            Static token that is generated during account creation.
        video_id: String of the YouTube video ID of the movie's trailer.
        poster_path: String containing the URL to the poster art for the movie.
        overview: String containing a brief overview of the movie's story.
        append_vals: Tuple of values to append to the end of a URL for
            the append_to_response feature of the API.
    """

    # Base URLs that are shared by all instances for general API
    # access
    _base_url = 'https://api.themoviedb.org/3/'
    _base_config_url = 'https://api.themoviedb.org/3/configuration?api_key='

    def __init__(self, movie_id, api_key, append_vals=None):
        """"Inits the instance"""
        self.movie_id = movie_id
        self.api_key = api_key
        self.video_id = None
        self.poster_path = None
        self.overview = None
        self.title = None

        # append_vals should only be a tuple of values, nothing else.
        # Other methods will check for None in conditionals
        if type(append_vals) is not tuple:
            self.append_vals = None
        else:
            self.append_vals = append_vals

    def _url_gen(self, base_url, api_key,
                 resource, item, append=False):
        """Dynamically creates an API request URL, based on the call"""

        # Basic URL construction WITHOUT the use of the append_to_response
        # feature
        resource_seg = '{}/{}?api_key='.format(resource, item)
        full_url = '{}{}{}&language=en-US'.format(base_url, resource_seg, api_key)

        # If using append_to_response feature, this section will
        # construct the URL appending all additonal values.
        if append is not False and self.append_vals is not None:
            append_url = ''
            for value in self.append_vals:
                append_url = '{}{},'.format(append_url, str(value))
            return '{}&append_to_response={}'.format(full_url, append_url).rstrip(',')
        return full_url

    def _get_movie_data(self):
        # Call private _url_gen method to build the API call URL for this
        # method
        req_url = self._url_gen(self._base_url, self.api_key,
                                'movie', self.movie_id,
                                append=self.append_vals)

        # Make connection to API, pull all default movie data
        # and, optionally, extra data for values passed in
        # for the "append_to_response" feature
        response = requests.get(req_url, timeout=1).json()

        # Get parital poster art path info from the response object.
        # The Movie Database API does not include the entire
        # path to the poster in the movie response, only a partial
        # path. This value will be used and then overloaded in the
        # "_get_image_data" method defined later to complete
        # the full URL to access the data.
        self.poster_path = response['poster_path']

        # Get overview from the response object
        self.overview = response['overview']

        # Get movie title from the response object
        self.title = response['title']

        # Search the video data, if it exists, and find
        # the YouTube ID of the first video that is a
        # Trailer. Store that in the instance attribute.
        if 'videos' in response.keys():
            for entry in response['videos']['results']:
                if entry['type'] == 'Trailer':
                    self.video_id = entry['key']
                    break

    def _get_image_url(self):
        """
        Gets the full path to a poster image for the
        work.
        """
        # Create URL to get the config data from the API. Used to get the
        # base URL for image access, in additon to all the available sizes
        # of the images.
        config_url = '{}{}'.format(self._base_config_url, self.api_key)
        conf_response = requests.get(config_url, timeout=1).json()

        # Get secure base URL from response object
        image_base_url = conf_response['images']['secure_base_url']

        # Test for membership of the w500 size and use if still
        # valid. If not, use the original size of the image
        if 'w500' in conf_response['images']['poster_sizes']:
            image_size = 'w500'
        else:
            image_size = 'original'

        self.poster_path = '{}{}{}'.format(image_base_url, image_size,
                                           self.poster_path)

    def build(self):
        """Calls the necessary private functions to fill the instance attributes of the movie object"""

        self._get_movie_data()
        self._get_image_url()


api_key = ''
movie_id = ''
appends = ('videos', 'images')

movietest = Movie(movie_id, api_key, append_vals=appends)
movietest.build()

print(movietest.__dict__)
