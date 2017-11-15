'''Start from here.'''

import os
import media
import fresh_tomatoes

TEXT_FILE_NAME = 'movies.txt'


def read_file(file_name):
    '''Read text file and return its content as a List.

    Args:
        file_name: Name of file to read.

    Returns:
        file_content: A List of file's content
    '''

    file_path = os.path.join(os.getcwd(), file_name)
    open_file = open(file_path)
    file_content = open_file.read().split('\n\n')
    open_file.close()

    return file_content


def create_movies(movie_list):
    '''Create a List of movie instances.

    Args:
        movie_list: List of movie infomation. 
            Each item contains one movie's name, storyline, 
            poster_image_url and trailer_url.

    Returns:
        movies: A List of Movie instance.
    '''

    movies = []

    for item in movie_list:
        movie = item.split('\n')

        if len(movie) == 3:
            movie.append('')

        movies.append(media.Movie(movie[0], movie[1], movie[2], movie[3]))

    return movies


def main():
    '''The main function.'''

    movie_list = read_file(TEXT_FILE_NAME)
    movies = create_movies(movie_list)
    fresh_tomatoes.open_movies_page(movies)


main()
