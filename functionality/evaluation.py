def evaluateExpressionTree(root, tree, allFiles):
    if root is None:
        return None

    if root.left is None and root.right is None:
        existingWord, htmlPagesOfOneWord = tree.search(root.value)
        if existingWord == 'True':
            return htmlPagesOfOneWord
        else:
            return {}

    left_leaf = evaluateExpressionTree(root.left, tree, allFiles)
    right_leaf = evaluateExpressionTree(root.right, tree, allFiles)

    if root.value == '&&':
        resultSet = {}
        for key in left_leaf:
            if key in right_leaf:
                if root.left.value != root.right.value:
                    resultSet[key] = right_leaf[key] + left_leaf[key]
                else:
                    resultSet[key] = right_leaf[key]
        return resultSet

    elif root.value == '||':
        resultSet = {}
        for key in left_leaf:

            if key in right_leaf:
                if root.left.value != root.right.value:
                    resultSet[key] = right_leaf[key] + left_leaf[key]
                else:
                    resultSet[key] = right_leaf[key]
            else:
                resultSet[key] = left_leaf[key]

        for key in right_leaf:
            if key not in resultSet:
                resultSet[key] = right_leaf[key]

        return resultSet

    elif root.value == '!':
        resultSet = {}
        for key in allFiles:
            if key not in right_leaf:
                resultSet[key] = 0
        return resultSet
