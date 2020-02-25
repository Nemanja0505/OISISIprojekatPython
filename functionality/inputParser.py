def parseInput(string):
    character = False

    string = string.replace('\t', ' ')
    for ch in string:
        if ch == ' ':
            continue
        else:
            character = True
            break

    array = string.split(' ')

    resultArray = []

    for element in array:
        if element != '':
            resultArray.append(element)

    if not character:
        return [], False, False

    if len(resultArray) == 0:
        return [], False, False

    validInput = False
    logicalInput = False
    if len(resultArray) == 3:
        if resultArray[1].upper() == 'AND' or resultArray[1].upper() == 'OR' or resultArray[1].upper() == 'NOT':
            validInput = True
            logicalInput = True
        else:
            validInput = True
    if len(resultArray) == 3 and (
            (resultArray[0].upper() == 'AND' or resultArray[0].upper() == 'OR' or resultArray[0].upper() == 'NOT') or (
            resultArray[2].upper() == 'AND' or resultArray[2].upper() == 'OR' or resultArray[2].upper() == 'NOT')):
        validInput = False
    if len(resultArray) != 3:
        validInput = True
        for i in range(len(resultArray)):
            if resultArray[i].upper() == 'AND' or resultArray[i].upper() == 'OR' or resultArray[i].upper() == 'NOT':
                validInput = False
                break

    for i in range(len(resultArray)):
        resultArray[i] = resultArray[i].lower()

    return resultArray, validInput, logicalInput


def parseComplexInput(string):
    string = string.replace('\t', ' ')

    if len(string) == 0:
        print('GRESKA! *Niste uneli nijednu rec')
        return [], False

    arrayOfWords = []
    word = ''
    counter = 0
    valid = True
    for i in range(len(string)):
        if string[i] == ' ':
            if word != '':
                arrayOfWords.append(word)
            word = ''
        else:
            if string[i] in ['&', '|']:
                if word != '':
                    arrayOfWords.append(word)
                    word = ''

                if counter == 1:
                    counter = 0
                    if string[i] == string[i - 1]:
                        word = string[i] + string[i - 1]
                        arrayOfWords.append(word)
                        word = ''
                else:
                    if i + 1 < len(string):
                        if string[i] != string[i + 1]:
                            print('Neispravan unos pretrage')
                            valid = False
                    else:
                        print('Neispravan unos pretrage')
                        valid = False
                    counter += 1
                    continue

            elif string[i] == '!':
                if word != '':
                    arrayOfWords.append(word)
                    word = ''
                arrayOfWords.append(string[i])

            elif string[i] in [')', '(']:
                if word != '':
                    arrayOfWords.append(word)
                    word = ''
                arrayOfWords.append(string[i])

            else:
                word += string[i]

    if word != '':
        arrayOfWords.append(word)

    resultArray = []
    counter2 = 0
    leftParentheses = 0
    rightParentheses = 0
    for i in range(len(arrayOfWords)):
        if arrayOfWords[i] in [')', '(']:
            if arrayOfWords[i] == ')':
                rightParentheses += 1
            else:
                leftParentheses += 1
            counter2 += 1

    if counter2 % 2 != 0:
        print('GRESKA! *Proverite zagrade(broj zagrada mora biti paran)')
        valid = False

    if leftParentheses != rightParentheses:
        print('GRESKA! *Proverite zagrade(broj otvorenih i zatvorenih zagrada mora biti jednak)')
        valid = False

    if arrayOfWords[0] in ['&&', '||']:
        print('GRESKA! *Upit ne moze da pocne operatorom')
        valid = False

    if arrayOfWords[len(arrayOfWords) - 1] in ['&&', '||', '!']:
        print('GRESKA! *Upit ne moze da se zavrsi operatorom')
        valid = False

    if arrayOfWords[0] in [')']:
        print('GRESKA! *Proverite zagrade(upit ne moze da pocne zatvorenom zagradom)')
        valid = False

    if arrayOfWords[len(arrayOfWords) - 1] in ['(']:
        print('GRESKA! *Proverite zagrade(upit ne moze da se zavrsi sa otvorenom zagradom)')
        valid = False

    for i in range(len(arrayOfWords) - 1):
        resultArray.append(arrayOfWords[i])
        if arrayOfWords[i] in ['&&', '||', '!']:
            if arrayOfWords[i + 1] in ['&&', '||', ')']:
                print(
                    'GRESKA! *Nije moguce uneti dva operatora jedan do drugog(osim komplementa)\n*Posle operatora ne '
                    'moze da ide zatvorena zagrada')
                valid = False
        elif arrayOfWords[i] not in ['(', ')']:
            if arrayOfWords[i + 1] not in [')', '&&', '||']:
                resultArray.append('||')
        elif arrayOfWords[i] == ')' and (arrayOfWords[i + 1] not in ['&&', '||', ')']):
            resultArray.append('||')
        elif arrayOfWords[i] == '(' and (arrayOfWords[i + 1] in ['&&', '||',')']):
            print('GRESKA! *Posle otvorene zagrade nije moguce uneti operatore && i || niti zatvorenu zagradu')
            valid = False

    resultArray.append(arrayOfWords[len(arrayOfWords) - 1])
    print('Niz koji se prosledjuje')
    print(resultArray)

    return resultArray, valid
