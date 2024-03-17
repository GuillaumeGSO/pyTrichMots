import seek_words as sw
import pytest

"""
File 99.txt content is :
éèêiôù
bac
xyz
opa
api
aboulie
aiguail
"""

"""
is_list_empty_or_full_of_none
"""
def test_is_list_empty_or_full_of_none():
    with pytest.raises(TypeError):
        assert sw.is_list_empty_or_full_of_none()
    assert sw.is_list_empty_or_full_of_none([])
    assert sw.is_list_empty_or_full_of_none([None, None])
    assert sw.is_list_empty_or_full_of_none(['', ""])
    assert sw.is_list_empty_or_full_of_none([None, "", ''])


"""
is_search_by_content
"""
def test_is_search_by_content_NoWord():
    # Returns False if word is not set
    assert sw.is_search_by_content("") == False
    assert sw.is_search_by_content(None) == False


def test_is_search_by_content_NoLst():
    # Returns False if lst_car is empty
    assert sw.is_search_by_content("ab") == False
    assert sw.is_search_by_content("ab", [None, None]) == False


def test_is_search_by_content_LessCar():
    # Returns False if less caracters in lst_car than in word
    assert sw.is_search_by_content("ab", ["a"]) == False


def test_is_search_by_content_SameCar():
    # Returns True if each and every caracters are in lst_car
    assert sw.is_search_by_content("ab", ["b", 'a'])


def test_is_search_by_content_MoreCars():
    # Returns True if each and every caracters are in lst_car
    assert sw.is_search_by_content("ab", ["b", 'c', 'a', 'r'])


"""
is_search_by_hint
"""
def test_is_search_by_hint_NoWord():
    # Returns False if lst_car is empty
    assert sw.is_search_by_hint('') == False


def test_is_search_by_hint_NoHint():
    # Returns True if no hint provided
    assert sw.is_search_by_hint('abc') ==True
    assert sw.is_search_by_hint('abc', [sw.Hint(1), sw.Hint(3), sw.Hint(2)]) ==True


def test_is_search_by_hint_Hint():
    # Returns True if no hint provided
    # assert sw.is_search_by_hint('abc', [sw.Hint(1), sw.Hint(2, 'b')]) == True
    assert sw.is_search_by_hint('abc', [sw.Hint(2), sw.Hint(1), sw.Hint(3, 'c')]) == True


"""
search_in_file
"""
def test_search_in_file_exception():
    # Exception ValueError if no list provided
    with pytest.raises(Exception) as excp:
        assert sw.search_in_file(nb_car=99)
        excp.match("Les paramètres lst_car et lst_hint ne peuvent pas être vides en même temps")


def test_search_in_file_1_car():
    result = list(sw.search_in_file(lang="test", nb_car=99, lst_car=['a']))
    # No word contains all letter
    assert len(result) == 0


def test_search_in_file_1_car_rien():
    result = list(sw.search_in_file(lang="test",nb_car=99, lst_car=['u']))
    # No word contain all letter
    assert len(result) == 0


def test_search_in_file_2_cars():
    result = list(sw.search_in_file(lang="test",nb_car=99, lst_car=['b', 'a']))
    # No word contain all letter
    assert len(result) == 0


def test_search_in_file_3_cars():
    result = list(sw.search_in_file(lang="test",nb_car=99, lst_car=['c', 'a', 'b']))
    # One word only contains all letter
    assert len(result) == 1
    assert "bac" in result

def test_search_in_file_7_cars_with_accent():
    result = list(sw.search_in_file(lang="test",nb_car=99, lst_car=['e', 'e', 'e','i','o','u']))
    # One word only contains all letter
    assert len(result) == 1
    assert "éèêiôù" in result

def test_search_in_file_3_cars_et_plus():
    # All letter are in the words
    result = list(sw.search_in_file(lang="test",nb_car=99, lst_car=[
                  'a', 'b', 'c', 'd', 'i', 'o', 'p', 'x', 'y', 'z']))
    #We get all words
    assert len(result) == 4
    assert "bac" in result
    assert "opa" in result
    assert "api" in result
    assert "xyz" in result

def test_aboulie():
    result = list(sw.search_in_file(lang='test', nb_car=99, lst_car=[
                  'g', 'u', 'i', 'l', 'l', 'a', 'u', 'm', 'e'], strict=True))
    # aboulie should not be selected although 7 letters in common
    #(because of double "l")
    #aiguail shoudn't be selected : 2 times a    
    assert len(result) == 0

def test_search_in_file_hint_1():
    result = list(sw.search_in_file(lang="test", nb_car=99, lst_hint=[sw.Hint(2, "p")]))
    # All words with "p" in second position
    assert len(result) == 2
    assert "opa" in result
    assert "api" in result


def test_search_in_file_hint_2():
    result = list(sw.search_in_file(lang="test",nb_car=99, lst_hint=[sw.Hint(2, "y")]))
    assert len(result) == 1
    assert "xyz" in result


def test_search_in_file_hint_3():
    result = list(sw.search_in_file(lang="test",nb_car=99, lst_hint=[sw.Hint(1, "a")]))
    # All words that start with "a"
    assert len(result) == 3
    assert "api" in result
    assert "aboulie" in result
    assert "aiguail" in result

def test_search_in_file_complete():
    # All existing letters
    result = list(sw.search_in_file(lang="test",nb_car=99, lst_car=[
                  'a', 'b', 'c', 'd', 'i', 'o', 'p', 'x', 'y', 'z'], lst_hint=[sw.Hint(1, "a")]))
    assert len(result) == 1
    assert "api" in result

def test_search_in_file_not_starting():
    # All existing letters
    result = list(sw.search_in_file(lang="test",nb_car=99, lst_car=[
                  'a', 'b', 'c', 'd', 'i', 'o', 'p', 'x', 'y', 'z'], lst_hint=[sw.Hint(1, "a", True)]))
    assert len(result) == 3
    assert "bac" in result
    assert "xyz" in result
    assert "opa" in result