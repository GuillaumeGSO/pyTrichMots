import seek_words as sw
import pytest

"""
Le fichie 99.txt contient
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
    # Retourne faux si word est non renseigné
    assert sw.isSearchByContent("") == False
    assert sw.isSearchByContent(None) == False


def test_searchByContent_NoLst():
    # Retourne faux si rien dans la lstCar
    assert sw.isSearchByContent("ab") == False
    assert sw.isSearchByContent("ab", [None, None]) == False


def test_searchByContent_LessCar():
    # Retourne faux si il y moins de caractère dans lstCar que dans word
    assert sw.isSearchByContent("ab", ["a"]) == False


def test_searchByContent_SameCar():
    # Retourne vrai si chaque caractère de word est présent dans lstCar
    assert sw.isSearchByContent("ab", ["b", 'a'])


def test_searchByContent_MoreCars():
    # Retourne vrai si chaque caractère de word est présent dans lstCar
    assert sw.isSearchByContent("ab", ["b", 'c', 'a', 'r'])


"""
isSearchByHint
"""


def test_isSearchByHint_NoWord():
    # Retourne faux si word n'est pas renseigné
    assert sw.isSearchByHint('') == False
    # Exception si pas de word
    with pytest.raises(TypeError):
        assert sw.isSearchByHint()


def test_isSearchByHint_NoHint():
    # Retourne vrai si pas de Hint renseigné
    assert sw.isSearchByHint('abc')
    assert sw.isSearchByHint('abc', [None, None, None])


def test_isSearchByHint_Hint():
    # Retourne vrai si pas de Hint renseigné
    assert sw.isSearchByHint('abc', [None, 'b', ''])
    assert sw.isSearchByHint('abc', ['', '', 'c'])


"""
searchInFile
"""


def test_recherche_exception():
    # Exception ValueError si aucune liste fournie
    with pytest.raises(Exception) as excp:
        assert sw.searchInFile(nbCar=99)
        excp.match("Les paramètres lstCar et lstHint ne peuvent pas être vides en même temps")


def test_recherche_1_car():
    result = list(sw.searchInFile(nbCar=99, lstCar=['a']))
    # Aucun mot de contient toutes les lettres : il n'y en a pas assez
    assert len(result) == 0


def test_recherche_1_car_rien():
    result = list(sw.searchInFile(nbCar=99, lstCar=['u']))
    # Aucun mot de contient toutes les lettres
    assert len(result) == 0


def test_recherche_2_cars():
    result = list(sw.searchInFile(nbCar=99, lstCar=['b', 'a']))
    # Aucun mot de contient toutes les lettres
    assert len(result) == 0


def test_recherche_3_cars():
    result = list(sw.searchInFile(nbCar=99, lstCar=['c', 'a', 'b']))
    # Un seul mot contient toutes les lettres
    assert len(result) == 1
    assert "bac" in result

def test_recherche_7_cars_with_accent():
    result = list(sw.searchInFile(nbCar=99, lstCar=['e', 'e', 'e','i','o','u']))
    # Un seul mot contient toutes les lettres
    assert len(result) == 1
    assert "éèêiôù" in result

def test_recherche_3_cars_et_plus():
    #On passe l'ensemble des lettres existantes
    result = list(sw.searchInFile(nbCar=99, lstCar=[
                  'a', 'b', 'c', 'd', 'i', 'o', 'p', 'x', 'y', 'z']))
    #On récupère donc l'ensemble des mots
    assert len(result) == 4
    assert "bac" in result
    assert "opa" in result
    assert "api" in result
    assert "xyz" in result

def test_aboulie():
    result = list(sw.searchInFile(nbCar=99, lstCar=[
                  'g', 'u', 'i', 'l', 'l', 'a', 'u', 'm', 'e']))
    #aboulie ne doit pas ressortir bien qu'il ai 7 lettres en commun
    #(à cause du double "l")
    #aiguail ne doit pas ressortir : il y a 2 fois le a    
    assert len(result) == 0

def test_recherche_hint_1():
    result = list(sw.searchInFile(nbCar=99, lstHint=[None, "p", None]))
    # Tous les mots qui ont "p" en deuxième position
    assert len(result) == 2
    assert "opa" in result
    assert "api" in result


def test_recherche_hint_2():
    result = list(sw.searchInFile(nbCar=99, lstHint=[None, "y"]))
    assert len(result) == 1
    assert "xyz" in result


def test_recherche_hint_3():
    result = list(sw.searchInFile(nbCar=99, lstHint=["a"]))
    # Tous les mots qui commencent par "a"
    assert len(result) == 3
    assert "api" in result
    assert "aboulie" in result
    assert "aiguail" in result

def test_recherche_complete():
    #On passe l'ensemble des lettres existantes
    result = list(sw.searchInFile(nbCar=99, lstCar=[
                  'a', 'b', 'c', 'd', 'i', 'o', 'p', 'x', 'y', 'z'], lstHint=['a']))
    #On récupère donc l'ensemble des mots
    assert len(result) == 1
    assert "api" in result