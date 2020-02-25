import os
from functionality.fileParser import *
from dataStructures.trie import *
from dataStructures.graph import *
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
allFiles = []
startInputs = 0
endInputs = 0

def inputDirectory(pathDirectory):
    if not os.path.isdir(pathDirectory):
        print('\nUNELI STE NEPOSTOJECI DIREKTORIJUM')
        pathDirectory = ''
        return pathDirectory
    else:
      trie.__init__()
      graph.__init__()
      allFiles.clear()
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
            htmlPages = logical(array,trie)
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
      print('\t'*7,'---'*10,'MENI','---'*10)
      print('\t'*12,'1.Izbor direktorijuma')
      print('\t'*12,'2.Pretraga')
      print('\t'*12,'3.Napredna pretraga')
      print('\t'*12,'X.Izlaz iz programa')
      print('\t'*9,'NAPOMENA : neophodno je prvo izabrati direktorijum\n','\t'*9,'za pravilno izvrsavanje ostalih funkcionalnosti\n','\t'*7,'-'*65)
      unos = input('Odabir operacije:').strip()

      if unos == '1':
        pathDirectory = input('Unesite putanju zeljenog direktorijuma koji zelite da pretrazite: ').strip()
        startInputs = time.time()
        pathDirectory = inputDirectory(pathDirectory)
        endInputs = time.time()
        print()
      elif unos == '2':
        if pathDirectory == '':
            print('\nNiste izabrali putanju direktorijuma [procitajte napomenu]\n')
        else:
            print('\t' * 12, 'UPUTSVO KORISCENJA PRETRAGE\n', '\t' * 9, '* Moguce je pretraziti jednu/vise reci\n','\t' * 9, '* Moguca je logicka pretraga u formatu [rec AND|OR|NOT rec]\n', '\t' * 9,'* Reci and|or|not smatraju se logickim operatorima i nije ih moguce pretraziti\n')
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