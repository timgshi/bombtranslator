import sys, re, time
import collections, codecs, csv

class Word():
    def __init__(self, pos, spanish, english):
        self.pos = pos
        self.spanish = spanish
        self.english = english

def buildPOSDict():
    pos = {}
    f = open("mobypos.txt", 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.strip('\r')
        line = line.split('\\')
        pos[line[0]] = list(line[1])
    return pos
def buildDictionary():
        dict ={}
        dictname = 'dict.txt'
        d = codecs.open(dictname, 'r', 'utf-8')
        for line in d:
            line = line.strip('\n')
            line = line.split()
            dict[line[0].lower()] = line[1]
        return dict

def translate(text, dictionary, POSDictionary):
    document = []        

    for line in text:
        for word in line.split():
#            word = word.strip('.,')
            punc = ''
            if "." in word:
                word = word.strip('.')
                punc = '.'
            elif "," in word:
                word = word.strip(',')
                punc = ','
            if (word.lower() in dictionary):
                english = dictionary[word.lower()]
                document.append(Word(POSDictionary[english], word.lower(), english))
                if len(punc) > 0:
                    document.append(Word('punc', punc, punc))
    return document
            
        
#i know this is lame...so don't say anything GOD
if __name__ == '__main__':
    filename = "spanish_text.txt"
    f = codecs.open(filename, 'r', 'utf-8')
    textfile = []
    for line in f:
        textfile.append(line)
    spanishDict = buildDictionary()
    f.close()
    posDict = buildPOSDict()
    
    englishDoc = translate(textfile, spanishDict, posDict)
    