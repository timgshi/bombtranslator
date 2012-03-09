import sys, re, time
import collections

class Translator:
    def __init__(self):
        self.vocab = list()
        self.spanishDict = self.buildDictionary()
    def buildVocab(self, text):
        for word in text:
            self.vocab.append(word)
        print(len(self.vocab))
    def buildDictionary(self):
        print('hi')
        
            
        
#i know this is lame...so don't say anything GOD
if __name__ == '__main__':
    filename = "lazarillo.txt"
    f = open(filename, 'r')
    textfile = f.readlines()
    
    translator = Translator()
    translator.buildVocab(textfile)