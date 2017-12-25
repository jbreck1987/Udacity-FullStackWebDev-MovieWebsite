import requests


class Movie(object):
    """
    Movie object that consumes "The Movie Database" API
    This class defines Movie objects and contains
    access to information typical to a movie, such as:
    Title, Poster Art, Trailer URLs, etc. The data is all
    pulled via "The Movie Database" API (https://www.themoviedb.org/)

    Attributes:
        movie_id: String that uniquely IDs a movie within
            the movie database. Can be found via https://www.themoviedb.org/.
        api_key: String used for authentication for all calls to the API.
            Static token that is generated during account creation.
        video_id: String of the YouTube video ID of the movie's trailer.
        poster_path: String containing the URL to the poster art for the movie.
        append_vals: Optional tuple of values to append to the end of a
            request URL for the append_to_response feature of the API.
        title: String of the movie title.
        eflag: Boolean flag used to show if there was an error connecting to
            the API for this instance. Set to true on exceptions raised
            by "request" GET calls.

    """

    # Base URLs that are shared by all instances for general API
    # access
    _base_url = 'https://api.themoviedb.org/3/movie/'
    _base_config_url = 'https://api.themoviedb.org/3/configuration?api_key='

    def __init__(self, movie_id, api_key, append_vals=None):
        """"Inits the instance"""
        self.movie_id = movie_id
        self.api_key = api_key
        self.video_id = None
        self.poster_path = None
        self.title = None
        self.eflag = False

        # append_vals should only be a tuple of values.
        if type(append_vals) is not tuple:
            self.append_vals = None
        else:
            self.append_vals = append_vals

    def _url_gen(self, base_url, api_key, item, append=False):
        """
        Dynamically creates an API request URL

        Method is used to minimize repetitive code since the URL format
        for the "movie" section of the API is standardized. This also allows
        for the append_to_url feature to easily be used.

        Args:
            self: Self-explanatory
            base_url: String representing base URL for access to the 'movie'
                section of the API.
            api_key: String used for authentication
            item: String of the movie ID or item within the 'movie' section
                of the API that needs to be accessed.
            append: Optional, boolean used to tell the method that the
                append_to_values feature will be used.

        Raises: None

        Returns: String of the URL to be used for an API call.
        """

        # Basic URL construction WITHOUT the use of the append_to_response
        # feature
        full_url = '{}{}?api_key={}&language=en-US'.format(base_url,
                                                           item,
                                                           api_key)

        # If using append_to_response feature, construct the URL
        # appending all additonal values.
        if append is not False and self.append_vals is not None:
            append_url = ''
            for value in self.append_vals:
                append_url = '{}{},'.format(append_url, str(value))
            return '{}&append_to_response={}'.format(full_url,
                                                     append_url).rstrip(',')
        return full_url

    def _get_image_url(self):
        """
        Gets the full path to a poster image for the
        movie.

        The API implementation for TMDb does not return the
        full URL to access the images associated with the movie
        in the response to a call to get the primary data of a movie.
        It will only return a partial path to the image; an ID of sorts.
        To get the information to create a full URL to the image, a call
        to the API to get configuration data is necessary. See
        "https://developers.themoviedb.org/3/configuration/
        get-api-configuration" for more information on the data
        necessary to construct a full image URL.

        Args:
            Only takes self, all functionality is based off
            of instance attributes or methods.

        Raises: None

        Returns: Nothing, sets instance variables based off of config data.
        """

        # Create URL to get the config data from the API. Used to get the
        # base URL for image access, in additon to all the available sizes
        # of the images.
        config_url = '{}{}'.format(self._base_config_url, self.api_key)

        # If exception on call to config data URL,
        # set instance error flag to true.
        try:
            conf_response = requests.get(config_url, timeout=1)
            conf_response.raise_for_status()
            conf_response = conf_response.json()

        except requests.exceptions.Timeout as ct:
            print(ct)
            self.eflag = True
            self.poster_path = None

        except requests.exceptions.HTTPError as he:
            print('{}...failed to get image URL for '
                  '{}'.format(he, self.title))

            self.eflag = True
            self.poster_path = None

        except requests.exceptions.ConnectionError as ce:
            print(ce)
            self.eflag = True
            self.poster_path = None

        else:
            # Get secure base URL from response object
            image_base_url = conf_response['images']['secure_base_url']

            # If w500 size is valid, use. Fallback to original size
            if 'w500' in conf_response['images']['poster_sizes']:
                image_size = 'w500'
            else:
                image_size = 'original'

            # Set poster_path URL to new full path
            self.poster_path = '{}{}{}'.format(image_base_url, image_size,
                                               self.poster_path)

    def _get_movie_data(self):
        """
        Pulls primary data for the movie from the API. This data
        is then parsed and then some values are used to populate
        the necessary instance attributes.

        Args:
            Only takes self, all functionality is based off
            of instance attributes or methods.

        Raises:
            requests.exceptions.Timeout: "requests" exception for network
                connection timeouts.
            requests.exceptions.HTTPError: "requests" exception for HTTP
                status codes indicating error.
            requests.exceptions.ConnectionError: "requests" exception for
                non - timeout network connection errors
            See "requests" documentation for more informaton.

        Returns: Nothing, sets instance variables based off of primary
            movie data.
        """

        # Call private _url_gen method to build the API call URL for this
        # method
        req_url = self._url_gen(self._base_url,
                                self.api_key,
                                self.movie_id,
                                append=self.append_vals)
        try:
            # If exception on call to primary data URL,
            # set instance error flag to true.
            response = requests.get(req_url, timeout=1)
            response.raise_for_status()
            response = response.json()

        except requests.exceptions.Timeout as ct:
            print(ct)
            self.eflag = True

        except requests.exceptions.HTTPError as he:
            print('{}...check args passed to init'.format(he))
            self.eflag = True

        except requests.exceptions.ConnectionError as ce:
            print(ce)
            self.eflag = True

        else:
            # Get parital poster art path info from the response object.
            self.poster_path = response['poster_path']

            # Get movie title from the response object
            self.title = response['title']

            # Search the video data, if it exists, and find
            # the YouTube ID of the first video that is a
            # Trailer.
            if 'videos' in response.keys():
                for entry in response['videos']['results']:
                    if entry['type'] == 'Trailer':
                        self.video_id = entry['key']
                        break

            # Call method to get complete image URL
            self._get_image_url()

    def build(self):
        """Calls the necessary private function to fill
        the instance attributes of the movie object"""

        self._get_movie_data()
