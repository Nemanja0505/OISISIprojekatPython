import os
from fileParser import *
from trie import *
from graph import *
import time

parser = Parser()
trie = Trie()
graph = Graph()

def inputDirectory(pathDirectory):
    if not os.path.isdir(pathDirectory):
        print('Uneli ste nepostojeci direktorijum')
        pathDirectory = ''
        return pathDirectory
    else:
      for root, dirs, files in os.walk(pathDirectory):
         for file in files:
            if (file.endswith('html') or file.endswith('htm')):
                links, words = parser.parse(os.path.join(root, file))
                graph.insert(os.path.join(root, file), links)
                for word in words:
                    trie.insert(word)
      return pathDirectory

def findWords(string):
    array,validInput,logicalInput = parseInput(string)
    if validInput:
        if logicalInput:
            print('Logicka pretraga')
        else:
            print('Obicna pretraga')
    else:
        print('Niste uneli ispravan unos')

def parseInput(string):
    array = string.split(' ')
    validInput = False
    logicalInput = False
    if len(array) == 3:
        if array[1].upper() == 'AND' or array[1].upper() == 'OR' or array[1].upper() == 'NOT':
           validInput = True
           logicalInput = True
        else:
           validInput = True
    if len(array) == 3 and ((array[0].upper() == 'AND' or array[0].upper() == 'OR' or array[0].upper() == 'NOT') or (array[2].upper() == 'AND' or array[2].upper() == 'OR' or array[2].upper() == 'NOT')):
        validInput = False
    if len(array) !=3:
        validInput = True
        for i in range(len(array)):
            if array[i].upper() == 'AND' or array[i].upper() == 'OR' or array[i].upper() == 'NOT':
                validInput = False
                break

    return array,validInput,logicalInput



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