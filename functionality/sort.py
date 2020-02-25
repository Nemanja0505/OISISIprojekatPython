def showSortPages(htmlPages):

    htmlPages = sortHtmlPages(htmlPages)
    start = 0
    step = 10


    sortList = list(htmlPages)

    running2 = True
    if len(sortList) >= step:
        defaultStep = 10
    else:
        step = len(sortList)
        defaultStep = step

    showStepByStep(sortList, start, step,htmlPages)
    if(len(sortList) > defaultStep):
      print('\t'*18,'SLEDECA--->')
    print('\t' * 18, start + step, '/', len(sortList))


    while running2:
        print('1.Prikazi sledecu stranicu : ')
        print('2.Prikazi predhodnu stranicu : ')
        print('3.Promeni broj prikaza stanica : ')
        print('X.Izlaz iz pretrage: ')

        option = input().strip()

        if option == '1':
            if start + step == len(sortList):
                if len(sortList) > step:
                    showStepByStep(sortList, start, step, htmlPages)
                    print('\t'*17,'<---PRETHODNA')
                    print('\t' * 18, start + step, '/', len(sortList))
                else:
                    showStepByStep(sortList, start, step, htmlPages)
                    print('\t'*18,start + step,'/',len(sortList))
            else:
                start = start + step
                if start + step == len(sortList):
                    showStepByStep(sortList, start, step,htmlPages)
                    print('\t'*17,'<---PRETHODNA')
                    print('\t' * 18, start + step, '/', len(sortList))
                if len(sortList) < start + step:
                    step = len(sortList) - start
                    showStepByStep(sortList, start, step,htmlPages)
                    print('\t'*14,'<---PRETHODNA\t|\tSLEDECA--->')
                    print('\t' * 17, start + step, '/', len(sortList))
                if len(sortList) > start + step:
                    showStepByStep(sortList, start, step,htmlPages)
                    print('\t'*14,'<---PRETHODNA\t|\tSLEDECA--->')
                    print('\t' * 17, start + step, '/', len(sortList))
        elif option == '2':
            if len(sortList) == start + step:
                step = defaultStep
                if start > 0:
                    start = start - step
                showStepByStep(sortList, start, step,htmlPages)
                print('\t'*17,'<---PRETHODNA')
                print('\t' * 18, start + step, '/', len(sortList))
            else:
                if start == 0:
                    showStepByStep(sortList, start, step, htmlPages)
                    print('\t'*18,'SLEDECA--->')
                    print('\t' * 18, start + step, '/', len(sortList))
                if start != 0:
                    start = start - step
                    showStepByStep(sortList, start, step,htmlPages)
                    print('\t'*14,'<---PRETHODNA\t|\tSLEDECA--->')
                    print('\t' * 17, start + step, '/', len(sortList))
        elif option == '3':
            valid = True
            try:
                step = int(input('Unesite zeljeni korak'))
            except:
                print('MORATE UNETI BROJ \n')
                valid = False
            if valid:
                start = 0
                if step > len(sortList):
                    showStepByStep(sortList, 0, len(sortList),htmlPages)
                    print('\t' * 17, 0 + len(sortList), '/', len(sortList))
                    step = len(sortList)
                    print('\t'*5,'Uneli ste prevelik korak,ukupan broj stranica je\n', len(sortList))
                else:
                    showStepByStep(sortList, start, step,htmlPages)
                    print('\t'*18,'SLEDECA--->')
                    print('\t' * 18, start + step, '/', len(sortList))
                defaultStep = step

        else:
            if option.upper() == 'X':
                 running2 = False


def showStepByStep(sortList,start,step,htmlPages):
        if len(sortList) != 0:
            print('\t'*6,'RB','\t'*10,'HTML STRANICE','%69s' %('RANG'))
            for i in range(start,start + step):
                print('\t'*5,'%5d' %(i+1),'% -120s' % sortList[i],round(htmlPages[sortList[i]],4))




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

