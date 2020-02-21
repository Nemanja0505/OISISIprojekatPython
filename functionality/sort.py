def showSortPages(htmlPages):

    htmlPages = sortHtmlPages(htmlPages)
    print('SORTIRANE HTML STRANICE NA OSNOVU RANGA')
    for key in htmlPages:
        print('RANG:',htmlPages[key],'-->',key)


def sortHtmlPages(hasMap):
    lista = list(hasMap.items())

    hasMapNova = {}
    n = len(lista)
    merge_sort(lista)
    for i in range(len(lista)):
        hasMapNova[lista[i][0]] = lista[i][1]
    return hasMapNova


def merge(s1, s2, s):
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i][1] > s2[j][1]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1


def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]

    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, s)

