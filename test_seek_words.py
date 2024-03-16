import seek_words as sw
import pytest

"""
File 99.txt content is :
abc
abd
xyz
opa
api
été
"""

"""
isListEmptyOrFullOfNone
"""


def test_isListEmptyOrFullOfNone():
    with pytest.raises(TypeError):
        assert sw.isListEmptyOrFullOfNone()
    assert sw.isListEmptyOrFullOfNone([])
    assert sw.isListEmptyOrFullOfNone([None, None])
    assert sw.isListEmptyOrFullOfNone(['', ""])
    assert sw.isListEmptyOrFullOfNone([None, "", ''])


"""
isSearchByContent
"""

def test_searchByContent_NoWord():
    # Returns False if word is not set
    assert sw.isSearchByContent("") == False
    assert sw.isSearchByContent(None) == False


def test_searchByContent_NoLst():
    # Returns False if lstCar is empty
    assert sw.isSearchByContent("ab") == False
    assert sw.isSearchByContent("ab", [None, None]) == False


def test_searchByContent_LessCar():
    # Returns False if less caracters in lstCar than in word
    assert sw.isSearchByContent("ab", ["a"]) == False


def test_searchByContent_SameCar():
    # Returns True if each and every caracters are in lstCar
    assert sw.isSearchByContent("ab", ["b", 'a'])


def test_searchByContent_MoreCars():
    # Returns True if each and every caracters are in lstCar
    assert sw.isSearchByContent("ab", ["b", 'c', 'a', 'r'])


"""
isSearchByHint
"""


def test_isSearchByHint_NoWord():
    # Returns False if lstCar is empty
    assert sw.isSearchByHint('') == False
    # Exception if no word
    with pytest.raises(TypeError):
        assert sw.isSearchByHint()


def test_isSearchByHint_NoHint():
    # Returns True if no hint provided
    assert sw.isSearchByHint('abc')
    assert sw.isSearchByHint('abc', [None, None, None])


def test_isSearchByHint_Hint():
    # Returns True if no hint provided
    assert sw.isSearchByHint('abc', [None, 'b', ''])
    assert sw.isSearchByHint('abc', ['', '', 'c'])


"""
searchInFile
"""

def test_search_exception():
    # Exception ValueError if no list provided
    with pytest.raises(Exception) as excp:
        assert sw.searchInFile(nbCar=99)
        excp.match("Les paramètres lstCar et lstHint ne peuvent pas être vides en même temps")


def test_search_1_car():
    result = list(sw.searchInFile(nbCar=99, lstCar=['a']))
    # No word contains all letter
    assert len(result) == 0


def test_search_1_car_rien():
    result = list(sw.searchInFile(nbCar=99, lstCar=['u']))
    # No word contain all letter
    assert len(result) == 0


def test_search_2_cars():
    result = list(sw.searchInFile(nbCar=99, lstCar=['b', 'a']))
    # No word contain all letter
    assert len(result) == 0


def test_search_3_cars():
    result = list(sw.searchInFile(nbCar=99, lstCar=['c', 'a', 'b']))
    # One word only contains all letter
    assert len(result) == 1
    assert "bac" in result

def test_search_7_cars_with_accent():
    result = list(sw.searchInFile(nbCar=99, lstCar=['e', 'e', 'e','i','o','u']))
    # One word only contains all letter
    assert len(result) == 1
    assert "éèêiôù" in result

def test_search_3_cars_et_plus():
    # All letter are in the words
    result = list(sw.searchInFile(nbCar=99, lstCar=[
                  'a', 'b', 'c', 'd', 'i', 'o', 'p', 'x', 'y', 'z']))
    #We get all words
    assert len(result) == 4
    assert "bac" in result
    assert "opa" in result
    assert "api" in result
    assert "xyz" in result

def test_aboulie():
    result = list(sw.searchInFile(nbCar=99, lstCar=[
                  'g', 'u', 'i', 'l', 'l', 'a', 'u', 'm', 'e']))
    # aboulie should not be selected although 7 letters in common
    #(because of double "l")
    #aiguail shoudn't be selected : 2 times a    
    assert len(result) == 0

def test_recherche_hint_1():
    result = list(sw.searchInFile(nbCar=99, lstHint=[None, "p", None]))
    # All words with "p" in second position
    assert len(result) == 2
    assert "opa" in result
    assert "api" in result


def test_recherche_hint_2():
    result = list(sw.searchInFile(nbCar=99, lstHint=[None, "y"]))
    assert len(result) == 1
    assert "xyz" in result


def test_recherche_hint_3():
    result = list(sw.searchInFile(nbCar=99, lstHint=["a"]))
    # All words that start with "a"
    assert len(result) == 3
    assert "api" in result
    assert "aboulie" in result
    assert "aiguail" in result

def test_recherche_complete():
    # All existing letters
    result = list(sw.searchInFile(nbCar=99, lstCar=[
                  'a', 'b', 'c', 'd', 'i', 'o', 'p', 'x', 'y', 'z'], lstHint=['a']))
    assert len(result) == 1
    assert "api" in result