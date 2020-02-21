def ranking(htmlPages,korak):
    rankDicitonary = {}
    i = 0
    previous = 0
    for key, value in sorted(htmlPages.items(), key=lambda item: item[1]):

        if previous != value:
            i = korak + i
            rankDicitonary[key] = i
            previous = value
        else:
            rankDicitonary[key] = i

   # for key in rankDicitonary:
    #    print(key, '----->', rankDicitonary[key])
    #print('------------' * 20)
    return rankDicitonary

def rankDictionary(htmlPages,arrayOfDictionary,graph):

    dictionaryForImprovingRank = {}

    for key in htmlPages:
        dictionaryForImprovingRank[key] = 0
        for value in htmlPages[key]:
            dictionaryForImprovingRank[key] = dictionaryForImprovingRank[key] + value

    arrayOfDictionary.append(ranking(dictionaryForImprovingRank,0.2))

    dictionaryOfLinks = {}
    dictionaryOfWordsInLinks = {}

    for key in htmlPages:
        wordsNumber = htmlPages[key]  # broj reci koje smo pretrazili u tom linku
        linksNumber1, linksNumber2, pointingPages = graph.sumOfConnectingLinks(key)  # broj linkova koji pokazuju na njega,broj linkova na koje pokazuje i lista linkova koji pokazuju na njega
        wordsNumberInPage = graph.sumOfWords(htmlPages, pointingPages)  # broj reci u stranici koja sadrzi link
        dictionaryOfLinks[key] = linksNumber1
        dictionaryOfWordsInLinks[key] = wordsNumberInPage  # mapa straniceKojeSdrzeLink-->brojTrazeneReciNaTojStranici
        print(key, '------>', wordsNumber, '  ', linksNumber1, ' ', linksNumber2, '  ', wordsNumberInPage)

    dictionary1 = {}  # rangirana mapa za broj reci u Linku (spajanje prethodono dobijenih mapa koje se nalaze u nizu arrayOfDictionary)
    for i in range(len(arrayOfDictionary)):
        for key in arrayOfDictionary[i]:
            if key in dictionary1:
                dictionary1[key] = dictionary1[key] + arrayOfDictionary[i][key]
            else:
                dictionary1[key] = arrayOfDictionary[i][key]

    dictionary2 = ranking(dictionaryOfLinks,0.2)  # rangirana mapa  za Linkove (svakoj se daje + 0.2)
    dictionary3 = ranking(dictionaryOfWordsInLinks,0.1) # rangirana mapa za ReciULinkovima (svakoj se daje +0.1)

    rankingDictionary = {}  # recnik sa uracunatim svim kriterijumima rangiranja

    for key in dictionary1:
        if key in dictionary2:
            if key in dictionary3:
                rankingDictionary[key] = dictionary1[key] + dictionary2[key] + dictionary3[key]

    return rankingDictionary
