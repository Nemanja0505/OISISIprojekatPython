import os
from functionality.fileParser import *
from dataStructures.trie import *
from dataStructures.graph import *
from dataStructures.set import *
from functionality.inputParser import *
from functionality.resultSetOfPages import *
import time


parser = Parser()
trie = Trie()
graph = Graph()
set = Set()

def inputDirectory(pathDirectory):
    if not os.path.isdir(pathDirectory):
        print('Uneli ste nepostojeci direktorijum')
        pathDirectory = ''
        return pathDirectory
    else:
      trie.__init__()
      for root, dirs, files in os.walk(pathDirectory):
         for file in files:
            if (file.endswith('html') or file.endswith('htm')):
                links, words = parser.parse(os.path.join(root, file))
                graph.insert(os.path.join(root, file), links)
                for word in words:
                    trie.insert(word,os.path.join(root,file))
      return pathDirectory

def findWords(string):
    array,validInput,logicalInput = parseInput(string)
    if validInput:
        if logicalInput:
            print('Logicka pretraga')
            htmlPages = logical(array,trie,set)

            i = 1
            for key in htmlPages:
                print(i,'',key,'--->',htmlPages[key])
                i += 1
        else:
            print('Obicna pretraga')
            htmlPages = regular(array,trie)

            i = 1;
            for key in htmlPages:
                print(i,'',key,'--->',htmlPages[key])
                i += 1
    else:
        print('Niste uneli ispravan unos')



if __name__ == '__main__':

  running = True
  pathDirectory = ''

  while running:
      print('---'*10,'MENI','---'*10)
      print('\t1.Izbor direktorijuma')
      print('\t2.Pretraga')
      print('\tX.Izlaz iz programa')
      print('NAPOMENA : neophodno je prvo izabrati direktorijum za pravilno izvrsavanje ostalih funkcionalnosti\n','-'*65)
      unos = input('Odabir operacije:')

      if unos == '1':
        pathDirectory = input('Unesite putanju zeljenog direktorijuma koji zelite da pretrazite: ')
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
      else:
          if unos.upper() == 'X':
            running = False


  print('Vreme ubacivanja reci i linkova u trie i graph :',endInputs - startInputs)