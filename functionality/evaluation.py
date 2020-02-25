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
                if isinstance(right_leaf[key], list) and isinstance(left_leaf[key], list):
                    resultSet[key] = right_leaf[key][0] + left_leaf[key][0]
                elif isinstance(right_leaf[key], list):
                    resultSet[key] = right_leaf[key][0] + left_leaf[key]
                elif isinstance(left_leaf[key], list):
                    resultSet[key] = right_leaf[key] + left_leaf[key][0]
                else:
                    resultSet[key] = right_leaf[key] + left_leaf[key]
        return resultSet

    elif root.value == '||':
        resultSet = {}
        for key in left_leaf:
            if key in right_leaf:
                if isinstance(right_leaf[key], list) and isinstance(left_leaf[key], list):
                    resultSet[key] = right_leaf[key][0] + left_leaf[key][0]
                elif isinstance(right_leaf[key], list):
                    resultSet[key] = right_leaf[key][0] + left_leaf[key]
                elif isinstance(left_leaf[key], list):
                    resultSet[key] = right_leaf[key] + left_leaf[key][0]
                else:
                    resultSet[key] = right_leaf[key] + left_leaf[key]
            else:
                if isinstance(left_leaf[key], list):
                    resultSet[key] = left_leaf[key][0]
                else:
                    resultSet[key] = left_leaf[key]

        for key in right_leaf:
            if key not in resultSet:
                if isinstance(right_leaf[key], list):
                    resultSet[key] = right_leaf[key][0]
                else:
                    resultSet[key] = right_leaf[key]

        return resultSet

    elif root.value == '!':
        resultSet = {}
        for key in allFiles:
            if key not in right_leaf:
                resultSet[key] = 0
        return resultSet
