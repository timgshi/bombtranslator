import sys, re, time
import collections, codecs, csv

class Word():
    def __init__(self, pos, spanish, english):
        self.pos = pos
        self.spanish = spanish
        self.english = english

def buildDictionary():
        dict ={}
        dictname = 'dict.txt'
        d = codecs.open(dictname, 'r', 'utf-8')
        for line in d:
            line = line.strip('\n')
            line = line.split()
            dict[line[0].lower()] = [line[1], line[2]]
        return dict

def translate(text, dictionary):
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
                document.append(Word(dictionary[word.lower()][0], word.lower(), dictionary[word.lower()][0]))
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

    
    englishDoc = translate(textfile, spanishDict)
    
    