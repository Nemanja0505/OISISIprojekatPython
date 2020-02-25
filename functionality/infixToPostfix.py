def isOperator(ch):
    if ch in ['&&', '||', '!']:
        return True
    else:
        return False


def priority(key):
    dictionary = {"||": 0, "&&": 1, "!": 2, "(": 3}
    return dictionary[key]


def hasHigherPrecedence(top, current):
    priority1 = priority(top)
    priority2 = priority(current)

    if priority1 <= priority2:
        return False
    else:
        return True


def InfixToPostfix(array):
    stack = []
    postfixArray = []

    for i in range(len(array)):

        if isOperator(array[i]):
            while stack != [] and stack[len(stack) - 1] != '(' and hasHigherPrecedence(stack[len(stack) - 1], array[i]):
                postfixArray.append(stack[len(stack) - 1])
                stack.pop()

            stack.append(array[i])

        elif array[i] == '(':
            stack.append(array[i])

        elif array[i] == ')':
            while stack != [] and stack[len(stack) - 1] != '(':
                postfixArray.append(stack[len(stack) - 1])
                stack.pop()
            if stack:
                stack.pop()
            else:
                return []
        else:
            postfixArray.append(array[i])

    while stack:
        postfixArray.append(stack[len(stack) - 1])
        stack.pop()

    return postfixArray
