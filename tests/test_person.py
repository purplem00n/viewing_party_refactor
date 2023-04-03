import pytest
from viewing_party.person import Person

def test_create_person():
    # Arrange / Act
    kendall = Person("Kendall", ["Nancy"])

    # Assert
    assert isinstance(kendall, Person)

def test_person_name_is_set_correctly():
    # Arrange / Act
    nancy = Person("Nancy", ["Kendall"])
    danica = Person("Danica", ["Ping"])

    # Assert
    assert nancy.name == "Nancy"
    assert danica.name == "Danica"

def test_person_friends_list_is_set_correctly():
    # Arrange / Act
    ana = Person("Ana", ["Ariel"])

    # Assert
    assert ana.friends == ["Ariel"]

def test_friend_added_to_person():
    # Arrange
    laura = Person("Laura", ["Sage"])

    # Act
    laura.add_friend("Elizabeth")

    # Assert
    assert laura.friends == ["Sage", "Elizabeth"]

def test_no_duplicate_friends_added():
    # Arrange
    moyo = Person("Moyo", ["Sarah"])

    # Act
    moyo.add_friend("Sarah")

    # Assert
    assert moyo.friends == ["Sarah"]

# ---------------
# Part 3
# ---------------

def test_add_movie_to_watchlist_adds_movie():
    #Arrange
    moyo = Person("Moyo", ["Sarah"])
    #Act
    moyo.add_to_watchlist("matrix")
    #Assert
    assert moyo.watchlist == ["matrix"]

def test_no_duplicate_movies_added_to_watchlist():
    #Arrange
    moyo = Person("Moyo", ["Sarah"])
    #Act
    moyo.add_to_watchlist("matrix")
    moyo.add_to_watchlist("matrix")
    #Assert
    assert moyo.watchlist == ["matrix"]

def test_add_to_watched_adds_movie():
    #Arrange
    moyo = Person("Moyo", ["Sarah"])
    #Act
    moyo.add_to_watched("matrix")
    #Assert
    assert moyo.watched == ["matrix"]

def test_no_duplicate_movies_added_to_watched():
    #Arrange
    moyo = Person("Moyo", ["Sarah"])
    #Act
    moyo.add_to_watched("matrix")
    moyo.add_to_watched("matrix")
    #Assert
    assert moyo.watched == ["matrix"]


# --------------
# user unique watched
# ---------------
# I don't know how we reference friends' data

def test_user_unique_watched_returns_list():
    # Arrange
    ariel = Person("Ariel", [])
    moyo = Person("Moyo", [ariel])
    ariel.add_friend(moyo)
    ariel.add_to_watched("matrix")
    ariel.add_to_watched("mulan")
    moyo.add_to_watched("matrix")
    # Act
    result = ariel.user_unique_watched()
    # Assert
    assert result == ["mulan"]