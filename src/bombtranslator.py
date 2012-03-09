import sys, re, time
import collections, codecs

class Translator:
    def __init__(self):
        self.vocab = list()
        self.spanishDict = {}
        self.spanishDict = self.buildDictionary()
    def buildVocab(self, text):
        for word in text:
            self.vocab.append(word)
        print(len(self.vochb))
    def buildDictionary(self):
        dictname = 'dict.txt'
        d = codecs.open(dictname, encoding='utf-8')
        lines = d.readlines()
        for line in lines:
            line = line.strip('\n')
            line = line.split('\t')
            print(line)
            self.spanishDict[line[0]] = line[1]
            time.sleep(1)
        
            
        
#i know this is lame...so don't say anything GOD
if __name__ == '__main__':
    filename = "spanish_text.txt"
    f = codecs.open(filename, 'r', "utf-8")
    textfile = f.read()
    print(textfile)
    exit(1)
    
    translator = Translator()
    translator.buildVocab(textfile)