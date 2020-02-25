import os
from functionality.fileParser import *
from dataStructures.trie import *
from dataStructures.graph import *
from dataStructures.set import *
from functionality.inputParser import *
from functionality.resultSetOfPages import *
from functionality.sort import *
from functionality.infixToPostfix import *
from functionality.binaryTree import *
from functionality.evaluation import *
import time


parser = Parser()
trie = Trie()
graph = Graph()
set = Set()
allFiles = []

def inputDirectory(pathDirectory):
    if not os.path.isdir(pathDirectory):
        print('Uneli ste nepostojeci direktorijum')
        pathDirectory = ''
        return pathDirectory
    else:
      trie.__init__()
      if not os.path.isabs(pathDirectory):
        pathDirectory = os.path.abspath(pathDirectory)
      for root, dirs, files in os.walk(pathDirectory):
         for file in files:
            if file.endswith('html') or file.endswith('htm'):
                absPath = os.path.join(root,file)
                allFiles.append(absPath)
                links, words = parser.parse(absPath)
                graph.insert(absPath, links)
                for word in words:
                    trie.insert(word.lower(),absPath)
      return pathDirectory

def findWords(string):

    array,validInput,logicalInput = parseInput(string)
    if validInput:
        if logicalInput:
            print('Logicka pretraga')
            htmlPages = logical(array,trie,set)
            if len(htmlPages) != 0:
                 htmlPages = logicalRanking(htmlPages,array,trie,graph)
                 showSortPages(htmlPages)
            else:
                 print('Skup trazenih reci nije pronadjen')
        else:
            print('Obicna pretraga')
            htmlPages,arrayOfDictionary = regular(array,trie)
            if len(htmlPages) != 0:
                htmlPages = rankDictionary(htmlPages, arrayOfDictionary, graph)
                showSortPages(htmlPages)
            else:
                print('Trazena rec|reci nije pronadjena')
    else:
        print('Niste uneli ispravan unos')


if __name__ == '__main__':

  running = True
  pathDirectory = ''

  while running:
      print('---'*10,'MENI','---'*10)
      print('\t1.Izbor direktorijuma')
      print('\t2.Pretraga')
      print('\t3.Napredna pretraga')
      print('\tX.Izlaz iz programa')
      print('NAPOMENA : neophodno je prvo izabrati direktorijum za pravilno izvrsavanje ostalih funkcionalnosti\n','-'*65)
      unos = input('Odabir operacije:')
      unos.strip()

      if unos == '1':
        pathDirectory = input('Unesite putanju zeljenog direktorijuma koji zelite da pretrazite: ')
        pathDirectory.strip()
        startInputs = time.time()
        pathDirectory = inputDirectory(pathDirectory)
        endInputs = time.time()
        print()
      elif unos == '2':
        if pathDirectory == '':
            print('Niste izabrali putanju direktorijuma [procitajte napomenu]')
        else:
            print('\t\tUputstvo koriscenja pretrage\n','* Moguce je pretraziti jednu/vise reci\n','* Moguca je logicka pretraga u formatu [rec AND|OR|NOT rec]\n','* Reci and|or|not smatraju se logickim operatorima i nije ih moguce pretraziti')
            string = input('Unesite jednu ili vise reci:')
            findWords(string)
            print()
      elif unos == '3':
            print('\t\tUpustvo koriscenja napredne pretrage\n')
            string = input('Unesite logicki izraz koji zelite da pretrazite : ')
            arrayOfWords,valid = parseComplexInput(string)
            if not valid:
                print('Neispravan unos pretrage')
            else:
                postfixArray = InfixToPostfix(arrayOfWords)
                print(postfixArray)
                t = constructTree(postfixArray)
                inorder(t)
                htmlPages = evaluateExpressionTree(t, trie, allFiles)

                if len(htmlPages) != 0:
                    htmlPages = complexRanking(htmlPages,graph)
                    showSortPages(htmlPages)
                else:
                 print('Skup trazenih reci nije pronadjen')

      else:
          if unos.upper() == 'X':
            running = False

  if pathDirectory != '':
    print('Vreme ubacivanja reci i linkova u trie i graph :',endInputs - startInputs)

