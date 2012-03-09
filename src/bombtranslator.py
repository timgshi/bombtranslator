import sys, re, time
import collections, codecs, csv

class Translator:
    def __init__(self):
        self.vocab = list()
        self.spanishDict = {}

def buildDictionary():
        dict ={}
        dictname = 'dict.txt'
        d = codecs.open(dictname, 'r', 'utf-8')
        for line in d:
            line = line.strip('\n')
            line = line.split()
            print(line[0])
            dict[line[0].lower()] = line[1]
        return dict

def translate(text, translator):        
    filename = 'english.txt'
    f = open(filename, 'w')
    print('\n')
    for line in text:
        for word in line.split():
            word = word.strip('.,')
            if (word.lower() in translator.spanishDict):
                f.write(translator.spanishDict[word.lower()] + " ")
            else:
                print('not found' + word)
    f.close()
            
        
#i know this is lame...so don't say anything GOD
if __name__ == '__main__':
    filename = "spanish_text.txt"
    f = codecs.open(filename, 'r', 'utf-8')
    textfile = []
    for line in f:
        textfile.append(line)
    translator = Translator()
    translator.spanishDict = buildDictionary()
    f.close()

    
    translate(textfile, translator)
    
    