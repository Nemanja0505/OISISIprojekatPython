class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def isOperator(ch):
    if ch == '&&' or ch == '||' or ch == '!':
        return True
    else:
        return False


def inorder(tree):
    if tree is not None:
        inorder(tree.left)
        print(tree.value)
        inorder(tree.right)


def constructTree(postfix):
    stack = []

    for element in postfix:

        if not isOperator(element):
            tree = BinaryTree(element)
            stack.append(tree)

        else:
            if element == '!':
                tree = BinaryTree(element)
                t1 = stack.pop()
                tree.right = t1
                stack.append(tree)

            else:
                tree = BinaryTree(element)
                t1 = stack.pop()
                t2 = stack.pop()

                tree.right = t1
                tree.left = t2

                stack.append(tree)
    if stack != []:
        tree = stack.pop()
    else:
        return None
    return tree
