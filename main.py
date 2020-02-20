import os
from fileParser import *
from trie import *
import time

parser = Parser()
trie = Trie()

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
                for word in words:
                    trie.insert(word)
      return pathDirectory

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
            print('\t\tUputstvo koriscenja pretrage\n','* Moguce je pretraziti jednu/vise reci\n','* Moguca je logicka pretraga u formatu [rec AND|OR|NOT rec]')
            string = input('Unesite jednu ili vise reci:')
            print()
      else:
          if unos.upper() == 'X':
            running = False


  print('Vreme ubacivanja reci i linkova u trie i graph :',endInputs - startInputs)