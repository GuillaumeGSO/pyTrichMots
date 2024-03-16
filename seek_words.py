import time
import codecs
import unidecode

def isListEmptyOrFullOfNone(lst):
    if not lst:
        #print("List empty")
        return True
    if all(x is None or not x for x in lst):
        #print("List with None ou "" only")
        return True
    #print("List no empty")
    return False


def isSearchByContent(word, lstCar=[]):
    """
    Returns False if word is not set
    Returns False if lstCar is empty
    Returns False if less caracters in lstCar than in word
    Returns True if each and every caracters are in lstCar
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
        #print(f"Search {car} in {word}")
        if car in temp:
            temp.remove(car)
        else:
            return False
    return True


def isSearchByHint(word, lstHint=[]):
    """
    Returns False if word empty
    Returns True if no hint provided
    """
    if not word:
        return False
    if isListEmptyOrFullOfNone(lstHint):
        return True
    for idx, lettre in enumerate(lstHint):
        if lettre:
            #print(f"seek for {lettre} at position {idx} in {word}")
            if word.find(lettre) != idx:
                #print(f"give up car {lettre} not at {idx} in {word}")
                return False
    return True


def searchInFile(lang="fr", nbCar=99, lstCar=[], lstHint=[]):
    if isListEmptyOrFullOfNone(lstCar) and isListEmptyOrFullOfNone(lstHint):
        raise Exception(
            "Parameters lstCar et lstHint cannot be empty at the same time")

    for line in codecs.open(f"assets/{lang}/{str(nbCar)}.txt", "r", "utf-8"):
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