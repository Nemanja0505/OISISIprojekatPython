from functionality.rankingPages import *
from dataStructures.set import *


def logical(array, trie):
    first = Set()
    second = Set()
    setOfPages = Set()
    existingWord1, htmlPagesOfWord1 = trie.search(array[0])
    existingWord2, htmlPagesOfWord2 = trie.search(array[2])
    operation = array[1].upper()
    if existingWord1:
        for key in htmlPagesOfWord1:
            first.add_element(key, htmlPagesOfWord1[key])
    if existingWord2:
        for key in htmlPagesOfWord2:
            second.add_element(key, htmlPagesOfWord2[key])

    unionHtmlPages = {}
    setOfPages.operations(first, second, operation)
    for key in setOfPages.result:
        unionHtmlPages[key] = []
        if key in htmlPagesOfWord1:
            unionHtmlPages[key].append(htmlPagesOfWord1[key])
        if key in htmlPagesOfWord2:
            unionHtmlPages[key].append(htmlPagesOfWord2[key])

    return unionHtmlPages


def regular(arrayOfAllWords, trie):
    htmlPages = {}
    arrayOfDictionary = []
    array = []

    for element in arrayOfAllWords:
        if element not in array:
            array.append(element)

    for i in range(len(array)):
        existingWord, htmlPagesOfOneWord = trie.search(array[i])
        arrayOfDictionary.append(ranking(htmlPagesOfOneWord, 0.5))
        if existingWord == 'True':
            for key in htmlPagesOfOneWord:
                if key not in htmlPages:
                    htmlPages[key] = []
                    htmlPages[key].append(htmlPagesOfOneWord[key])
                else:
                    htmlPages[key].append(htmlPagesOfOneWord[key])

    return htmlPages, arrayOfDictionary
