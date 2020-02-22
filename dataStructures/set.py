class Set:

    def __init__(self):
        self.result = {}

    def add_element(self, key, array):
        if key not in self.result:
            self.result[key] = array


    def intersection(self,first,second):
        resulSet = {}
        for key in first.result:
            if key in second.result:
                array = []
                array.append(first.result[key])
                array.append(second.result[key])
                resulSet[key] = array
        return resulSet

    def union(self, first, second):
        resulSet = {}
        for key in first.result:
            array = []
            if key in second.result:
                array.append(first.result[key])
                array.append(second.result[key])
            else:
                array.append(first.result[key])
            resulSet[key] = array

        for key in second.result:
            array = []
            if key not in resulSet:
                array.append(second.result[key])
                resulSet[key] = array

        return resulSet

    def complement(self, first, second):
        resultSet = {}
        for key in first.result:
            array = []
            if key not in second.result:
                array.append(first.result[key])
                resultSet[key] = array
        return resultSet




    def operations(self,first,second,operation):
        if operation == 'AND':
            self.result = self.intersection(first,second)
        elif operation == 'OR':
            self.result = self.union(first,second)
        else:
            self.result = self.complement(first,second)
