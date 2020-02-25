
def evaluateExpressionTree(root, tree,allFiles):

    if root is None:
        return None

    # leaf node
    if root.left is None and root.right is None:
        existingWord,htmlPagesOfOneWord = tree.search(root.value)
        if existingWord == 'True':
            return htmlPagesOfOneWord
        else:
            return {}

    left_leaf = evaluateExpressionTree(root.left,tree,allFiles)
    right_leaf = evaluateExpressionTree(root.right,tree,allFiles)

    if root.value == '&&':
        resulSet = {}
        for key in left_leaf:
            if key in right_leaf:
                if isinstance(right_leaf[key],list) and isinstance(left_leaf[key],list):
                    resulSet[key] = right_leaf[key][0] + left_leaf[key][0]
                elif isinstance(right_leaf[key],list):
                    resulSet[key] = right_leaf[key][0] + left_leaf[key]
                elif isinstance(left_leaf[key],list):
                    resulSet[key] = right_leaf[key] + left_leaf[key][0]
                else:
                    resulSet[key] = right_leaf[key] + left_leaf[key]
        return resulSet

    elif root.value == '||':
        resulSet = {}
        for key in left_leaf:
            if key in right_leaf:
                if isinstance(right_leaf[key],list) and isinstance(left_leaf[key],list):
                    resulSet[key] = right_leaf[key][0] + left_leaf[key][0]
                elif isinstance(right_leaf[key],list):
                    resulSet[key] = right_leaf[key][0] + left_leaf[key]
                elif isinstance(left_leaf[key],list):
                    resulSet[key] = right_leaf[key] + left_leaf[key][0]
                else:
                    resulSet[key] = right_leaf[key] + left_leaf[key]
            else:
                if isinstance(left_leaf[key],list):
                    resulSet[key] = left_leaf[key][0]
                else:
                    resulSet[key] = left_leaf[key]

        for key in right_leaf:
            if key not in resulSet:
                if isinstance(right_leaf[key],list):
                    resulSet[key] = right_leaf[key][0]
                else:
                    resulSet[key] = right_leaf[key]

        return resulSet

    elif root.value == '!':
        resultSet = {}
        for key in allFiles:
            if key not in right_leaf:
                resultSet[key] = 0
        return resultSet