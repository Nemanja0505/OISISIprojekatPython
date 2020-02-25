from collections import defaultdict


class TrieNode():

    def __init__(self):
        self.children = dict()
        self.terminating = False
        self.dictionary = {}  # recnik za cuvanje skupa stranica (kljuc je link stranice,a vrednost broj pojavljivanja reci u linku)


class Trie():

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word, page):

        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])

            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)

        root.terminating = True

        # sluzi za prebrojavanje reci u prosledjenom linku
        if page not in root.dictionary:
            root.dictionary[page] = 1
        else:
            root.dictionary[page] += 1

    # pretraga reci unutar trie stabla
    # povratna vrednost pretrge je True ili False (u zavisnosti da li trazena rec postoji) i recnik koji sadrzi html stranice u kojima se data rec pojavljuje
    # kao i broj pojavljivanja zadate reci za svaku html stranicu
    def search(self, word):
        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])
            if not root:
                return str(False), {}
            root = root.children.get(index)

        if root and root.terminating:
            return str(True), root.dictionary
        else:
            return str(False), {}
