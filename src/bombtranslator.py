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

#rule 8
def rule_qs(english, pos):
    if ((pos+2) > len(english)-1): 
        return
    word1 = english[pos]
    word2 = english[pos+2]
    if ("i" in word1.pos) and ("N" in word2.pos or "r" in word2.pos):
        english[pos] = word2
        english[pos+2] = word1
def rule_ms(english, pos):
    if (pos < 2): return
    word1 = english[pos-2]
    if 'N' in word1.pos: return
    word2 = english[pos]
    if 'V' in word2.pos or 't' in word2.pos or 'i' in word2.pos:
        print(word1.spanish, englishDoc[pos-1].spanish, word2.spanish)
def rule_reflexive(english, pos):
    if (pos+4 > len(english)-1): return
    word1 = english[pos]
    word2 = english[pos+2]
    word3 = english[pos+4]
    if ('N' in word1.pos or 'r' in word1.pos):
        if (re.match("(me|te|nos|os|se)", word2.spanish)):
            if 'V' in word3.pos or 't' in word3.pos or 'i' in word3.pos:
                print('found', word1.english, word2.english, word3.english)
                englishDoc[pos+2].english = ""
                englishDoc[pos+3].english = ""
    
        
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
    
    #build your rules in this iterator
    for index in range(0, len(englishDoc)-1):
        rule_qs(englishDoc, index)
#        rule_ms(englishDoc, index)
        rule_reflexive(englishDoc, index)
        
    for line in englishDoc:
        print(line.english)
    