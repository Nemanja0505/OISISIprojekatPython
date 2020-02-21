def showSortPages(htmlPages):

    htmlPages = sortHtmlPages(htmlPages)
    start = 0
    step = 10


    sortList = list(htmlPages)

    running2 = True
    if len(sortList) >= step:
        defaultStep = 15
    else:
        step = len(sortList)
        defaultStep = step

    showStepByStep(sortList, start, step,htmlPages)
    print('\t'*10,'SLEDECA--->')

    while running2:
        print('1.Prikazi sledecih 10 : ')
        print('2.prikazi predhodnih 10 : ')
        print('3.promeni broj prikaza stanica : ')
        print('X.izlazak iz pretrage ')

        option = input()

        if option == '1':
            if start + step == len(sortList):
                showStepByStep(sortList, start, step, htmlPages)
                print('\t'*10,'<---PRETHODNA')
            else:
                start = start + step
                if start + step == len(sortList):
                    showStepByStep(sortList, start, step,htmlPages)
                    print('\t'*10,'<---PRETHODNA')
                if len(sortList) < start + step:
                    step = len(sortList) - start
                    print(start, step)
                    showStepByStep(sortList, start, step,htmlPages)
                    print('\t'*10,'<---PRETHODNA\t|\tSLEDECA--->')
                if len(sortList) > start + step:
                    print(start, step)
                    showStepByStep(sortList, start, step,htmlPages)
                    print('\t'*10,'<---PRETHODNA\t|\tSLEDECA--->')
        elif option == '2':
            if len(sortList) == start + step:
                step = defaultStep
                if start > 0:
                    start = start - step
                showStepByStep(sortList, start, step,htmlPages)
                print('\t'*10,'<---PRETHODNA')
            else:
                if start == 0:
                    showStepByStep(sortList, start, step, htmlPages)
                    print('\t'*10,'SLEDECA--->')
                if start != 0:
                    start = start - step
                    showStepByStep(sortList, start, step,htmlPages)
                    print('\t'*10,'<---PRETHODNA\t|\tSLEDECA--->')
        elif option == '3':
            step = int(input('Unesite zeljeni korak'))
            start = 0
            if step > len(sortList):
                showStepByStep(sortList, 0, len(sortList),htmlPages)
                step = len(sortList)
                print('Uneli ste prevelik korak ukupan broj stranica je', len(sortList))
            else:
                showStepByStep(sortList, start, step,htmlPages)
                print('\t'*10,'SLEDECA--->')
            defaultStep = step

        else:
            running2 = False


def showStepByStep(sortList,start,step,htmlPages):
        if len(sortList) != 0:
            for i in range(start,start + step):
                print(i + 1,'',sortList[i],'-->RANG:',htmlPages[sortList[i]])




def sortHtmlPages(htmlPages):
    listHtmlPages = list(htmlPages.items())

    sortHtmlPages = {}
    n = len(listHtmlPages)
    merge_sort(listHtmlPages)
    for i in range(len(listHtmlPages)):
        sortHtmlPages[listHtmlPages[i][0]] = listHtmlPages[i][1]
    return sortHtmlPages


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

