import time
import codecs
import unidecode

def isListEmptyOrFullOfNone(lst):
    if not lst:
        #print("List vide ou nulle")
        return True
    if all(x is None or not x for x in lst):
        #print("List avec des None ou "" seulement")
        return True
    #print("Liste non vide")
    return False


def isSearchByContent(word, lstCar=[]):
    """
    Retourne faux si word est non renseigné
    Retourne faux si rien dans lstCar
    Retourne faux si il y moins de caractère dans lstCar que dans word
    Retourne vrai si chaque caractère de word est présent dans lstCar
    Retourne 
    """
    if word == None or len(word) == 0:
        return False
    if isListEmptyOrFullOfNone(lstCar):
        return False
    if len(lstCar) < len(word):
        return False
    temp=lstCar.copy()
    word_no_accent = unidecode.unidecode(word)
    for car in word_no_accent:
        #print(f"recherche de {car} dans {word}")
        if car in temp:
            temp.remove(car)
        else:
            return False
    return True


def isSearchByHint(word, lstHint=[]):
    """
    Retourne faux si word n'est pas renseigné
    Retourne vrai si pas de Hint renseigné
    """
    if not word:
        return False
    if isListEmptyOrFullOfNone(lstHint):
        return True
    for idx, lettre in enumerate(lstHint):
        if lettre:
            #print(f"recherche de {lettre} à position {idx} dans {word}")
            if word.find(lettre) != idx:
                #print(f"abandon car {lettre} n'est pas à {idx} dans {word}")
                return False
    return True


def searchInFile(nbCar=99, lstCar=[], lstHint=[]):
    if isListEmptyOrFullOfNone(lstCar) and isListEmptyOrFullOfNone(lstHint):
        raise Exception(
            "Les paramètres lstCar et lstHint ne peuvent pas être vides en même temps")

    for line in codecs.open("assets/" + str(nbCar) + ".txt", "r", "utf-8"):
        mot = line.strip()
        if isSearchByContent(mot, lstCar) and isListEmptyOrFullOfNone(lstHint):
            yield mot
        elif isListEmptyOrFullOfNone(lstCar) and isSearchByHint(mot, lstHint):
            yield mot
        elif isSearchByContent(mot, lstCar) and isSearchByHint(mot, lstHint):
            yield mot


def searchInManyFiles(lstCar=[], lstHint=[]):
    for i in reversed(range(1, len(lstCar)+1)):
        for m in searchInFile(nbCar=i, lstCar=lstCar, lstHint=lstHint):
            yield m


""" s = time.time()
print("-".join(searchInManyFiles(lstCar=[
               'i', 'n', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'q', 'u', 'e'], lstHint=['i', '', '', 'o', None,'m' , ])))

e = time.time()
print(f"{e-s} secondes")
 """