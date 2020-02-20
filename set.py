class Set:

    def __init__(self):
        self.result = {}

    def operations(self,first,second,operation):
        if operation == 'AND':
            self.result = first.intersection(second)
        elif operation == 'OR':
            self.result = first.union(second)
        else:
            self.result = first.difference(second)
