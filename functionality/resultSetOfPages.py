from functionality.rankingPages import *

def logical(array, trie,setOfPages):
    first = set()
    second = set()
    existingWord1, htmlPagesOfWord1 = trie.search(array[0])
    existingWord2, htmlPagesOfWord2 = trie.search(array[2])
    operation = array[1].upper()
    if existingWord1:
        for key in htmlPagesOfWord1:
            first.add(key)
    if existingWord2:
        for key in htmlPagesOfWord2:
            second.add(key)

    unionHtmlPages = {}
    setOfPages.operations(first, second, operation)
    for key in setOfPages.result:
        unionHtmlPages[key] = []
        if key in htmlPagesOfWord1:
            unionHtmlPages[key].append(htmlPagesOfWord1[key])
        if key in htmlPagesOfWord2:
            unionHtmlPages[key].append(htmlPagesOfWord2[key])

    return unionHtmlPages


def regular(array,trie):
    htmlPages = {}
    arrayOfDictionary = []
    for i in range(len(array)):
        existingWord, htmlPagesOfOneWord = trie.search(array[i])
        arrayOfDictionary.append(ranking(htmlPagesOfOneWord,0.2))
        if existingWord == 'True':
            for key in htmlPagesOfOneWord:
                if (key not in htmlPages):
                    htmlPages[key] = []
                    htmlPages[key].append(htmlPagesOfOneWord[key])
                else:
                    htmlPages[key].append(htmlPagesOfOneWord[key])

    return htmlPages,arrayOfDictionary