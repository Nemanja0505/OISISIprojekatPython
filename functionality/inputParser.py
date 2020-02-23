
def parseInput(string):
    array = string.split(' ')
    validInput = False
    logicalInput = False
    if len(array) == 3:
        if array[1].upper() == 'AND' or array[1].upper() == 'OR' or array[1].upper() == 'NOT':
           validInput = True
           logicalInput = True
        else:
           validInput = True
    if len(array) == 3 and ((array[0].upper() == 'AND' or array[0].upper() == 'OR' or array[0].upper() == 'NOT') or (array[2].upper() == 'AND' or array[2].upper() == 'OR' or array[2].upper() == 'NOT')):
        validInput = False
    if len(array) !=3:
        validInput = True
        for i in range(len(array)):
            if array[i].upper() == 'AND' or array[i].upper() == 'OR' or array[i].upper() == 'NOT':
                validInput = False
                break
    for i in range(len(array)):
        array[i] = array[i].lower()

    return array,validInput,logicalInput

