def ranking(htmlPages, step):

    rankingDictionary = {}

    for key in htmlPages:
        if isinstance(htmlPages[key], list):
            rankingDictionary[key] = htmlPages[key][0] * step
        else:
            rankingDictionary[key] = htmlPages[key] * step

    return rankingDictionary


def rankDictionary(htmlPages, arrayOfDictionary, graph):
    dictionaryOfLinks = {}
    dictionaryOfWordsInLinks = {}

    for key in htmlPages:
        wordsNumber = htmlPages[key]  # broj reci koje smo pretrazili u tom linku
        linksNumber1, linksNumber2, pointingPages = graph.sumOfConnectingLinks(key)  # broj linkova koji pokazuju na
        # njega,broj linkova na koje pokazuje i lista linkova koji pokazuju na njega
        wordsNumberInPage = graph.sumOfWords(htmlPages, pointingPages)  # broj reci u stranici koja sadrzi link
        dictionaryOfLinks[key] = linksNumber1
        dictionaryOfWordsInLinks[key] = wordsNumberInPage  # mapa straniceKojeSdrzeLink-->brojTrazeneReciNaTojStranici


    dictionary1 = {}  # rangirana mapa za broj reci u Linku (spajanje prethodono dobijenih mapa koje se nalaze u nizu
    # arrayOfDictionary)
    for i in range(len(arrayOfDictionary)):
        for key in arrayOfDictionary[i]:
            if key in dictionary1:
                dictionary1[key] = dictionary1[key] + arrayOfDictionary[i][key]
            else:
                dictionary1[key] = arrayOfDictionary[i][key]
#   print('RANGIRANJE DRUGE KOLONE')
    dictionary2 = ranking(dictionaryOfLinks, 0.3)
#    print('RANGIRANJE POSLEDNJE KOLONE')
    dictionary3 = ranking(dictionaryOfWordsInLinks, 0.1)

    rankingDictionary = {}  # recnik sa uracunatim svim kriterijumima rangiranja

    for key in dictionary1:
        if key in dictionary2:
            if key in dictionary3:
                rankingDictionary[key] = dictionary1[key] + dictionary2[key] + dictionary3[key]

    return rankingDictionary


def logicalRanking(htmlPages, array, trie, graph):
    arrayOfDictionary = []

    if array[1].upper() == 'OR' or array[1].upper() == 'AND':
        if array[0].upper() != array[2].upper():
            existingWord1, htmlPages1 = trie.search(array[0])
            arrayOfDictionary.append(ranking(htmlPages1, 0.5))

        existingWord2, htmlPages2 = trie.search(array[2])
        arrayOfDictionary.append(ranking(htmlPages2, 0.5))

#kada imamo dve iste reci npr java and java tada treba samo da se ispise kao da imamo samo jednu javu
        if array[0].upper() == array[2].upper():
            htmlPages.clear()
            for key in htmlPages2:
                htmlPages[key] = [htmlPages2[key]]

    else:
        arrayOfDictionary.append(ranking(htmlPages, 0.5))

    htmlPages = rankDictionary(htmlPages, arrayOfDictionary, graph)

    return htmlPages


def complexRanking(htmlPages, graph):
    resultHtmlPages = {}

    for key in htmlPages:
        array = []
        array.append(htmlPages[key])
        resultHtmlPages[key] = array

    arrayOfDictionary = []
    rankingDictionary = ranking(resultHtmlPages, 0.5)
    arrayOfDictionary.append(rankingDictionary)

    resultHtmlPages = rankDictionary(resultHtmlPages, arrayOfDictionary, graph)

    return resultHtmlPages
