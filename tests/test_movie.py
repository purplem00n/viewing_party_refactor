import pytest
from viewing_party.movie import Movie

def test_movie_name_and_genre_and_rating_set_correctly():
    # Arrange
    matrix = Movie("Matrix", "Sci-Fi", 3)
    # Act

    # Assert
    assert matrix.name == "Matrix"
    assert matrix.genre == "Sci-Fi"
    assert matrix.rating == 3

def test_rating_between_1_and_5():
    #Arrange
    matrix = Movie("Matrix", "Sci-Fi", 3)

    assert matrix.rating in [1,2,3,4,5]