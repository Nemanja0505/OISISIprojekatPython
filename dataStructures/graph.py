import sys


class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    def addEdge(self, f, t, cost=0):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], cost)

    def getVertices(self):
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())

    def insert(self, a, niz):
        for i in range(0, len(niz)):
            self.addEdge(a, niz[i])

    # sumiranje svih stranica koje pokazuju na datu stanicu i ka kojima ona pokazuje

    def sumOfConnectingLinks(self, link):
        sumConnection = 0
        list = []
        for m in self.vertices:
            for i in self.getVertex(m).connectedTo:
                if i == self.vertices[link]:
                    sumConnection = sumConnection + 1
                    list.append(m)
                    # mozda treba break pogledati posle za optimizaciju
        return sumConnection, len(self.vertices[link].connectedTo), list

    def sumOfWords(self, dictionary, list):
        sumWords = 0  # broj svih reci u svim mapama
        for i in list:
            if i in dictionary:
                sumOfDictionary = 0
                for m in dictionary[
                    i]:  # prolazimo kroz vrdnosti mape a to je niz od dva broja i saberemo ih,npr [1,3] = 4
                    sumOfDictionary = sumOfDictionary + m
                sumWords = sumWords + sumOfDictionary
        return sumWords


class Vertex:
    def __init__(self, num):
        self.id = num
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()
