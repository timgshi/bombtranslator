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

def findSubject(word):
    verb = word+' '
    if re.match("[ae]s ", verb): return 'It'
    if re.match(u'\w+o ', verb): return 'I'
    if re.match('\w+[ae] ', verb): return "It"
    if re.match('\w+[ae]s ', verb): return 'You'
    if re.match('\w+[ae]mos ', verb): return 'We'
    if re.match('\w+[ae]n ', verb): return "They"
    
    if re.match('\w+[ai]ste ', verb): return "You"
    if re.match('\w+[ai]mos', verb): return "We"
    if re.match('\w+[ai]steis ', verb): return "You"
    if re.match('\w+(a|ie)ron ',verb): return "They"
    
    return ''

#rule 8
def rule_qs(english, pos):
    if ((pos+1) > len(english)-1): 
        return
    word1 = english[pos]
    word2 = english[pos+1]
    if ("i" in word1.pos) and ("N" in word2.pos or "r" in word2.pos):
        english[pos] = word2
        english[pos+1] = word1
        print(word1.english, word2.english)

def rule_ms(english, pos):
    if (pos < 2): return
    word1 = english[pos-2]
    if 'N' in word1.pos: return
    word2 = english[pos]
    if 'V' in word2.pos or 't' in word2.pos or 'i' in word2.pos:
        english[pos-2].english = findSubject(word1.spanish) + ' ' + word1.english
def findBeginningSubject(english, pos):
    if (pos == 0): 
        if 'V' in english[0].pos or 't' in english[0].pos or 'i' in english[0].pos:
            english[0].english = findSubject(english[0].spanish) + ' ' + english[0].english
        return
    word1 = english[pos-1]
    word2 = english[pos]
    if 'V' in word2.pos or 't' in word2.pos or 'i' in word2.pos:
        if 'punc' in word1.pos:
            english[pos].english = findSubject(word2.spanish) + ' ' + word2.english
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
                englishDoc[pos+4].english = ""

def to_plus_verb_ending_in_r(english, position) :
    currentWord = english[position]
    if 'V' in currentWord.pos:
        if len(currentWord.english) > 0 and currentWord.english[-1] == 'r':
            currentWord.english = "to " + str(currentWord.english)
            english[position] = currentWord

def noun_adjective_flip(english, position):
    noun = english[position]
    if position < (len(english) - 1):
        adjective = english[position + 1]
        if 'N' in english[position].pos and 'A' in english[position + 1].pos:
            english[position] = adjective
            english[position + 1] = noun
            
def do_not(english, position):
    no = english[position]
    if no.english == "no":
        if position < (len(english) - 1):
            if 'V' in english[position + 1].pos:
                no.english = "do " + str(no.english) + "t"
                english[position] = no
                
def direct_object_verb_flip(english, position):
    subject = english[position]
    if 'N' in subject.pos:
        if position < (len(english) - 2):
            direct_object = english[position + 1]
            verb = english[position + 2]
            if direct_object.spanish == "lo" and 'V' in verb.pos:
                english[position + 1] = verb
                english[position + 2] = direct_object
                
def adv_v_o(english, position):
    if ((position+2) > len(english)-1): 
        return
    word1 = english[position]
    word2 = english[position + 2]
    if 'V' in word1.pos and 'v' in word2.pos:
        english[position] = word2
        english[position+2] = word1
        
def deal_with_de(english, position):
    if ((position + 4) > len(english)-1):
        return
    word1 = english[position]
    word2 = english[position+2]
    word3 = english[position+4]
    if word2.spanish != 'de':
        return
    if 'N' in word1.pos and 'N' in word3.pos:
        if ((position + 6) > len(english)-1):
            english[position] = word3
            english[position+2] = word1
            english[position+4] = word2
            word2.english = ""
            english[position+3].english = ""
            return
        word4 = english[position+6]
        if 'N' in word4.pos or 'A' in word4.pos:
            english[position] = word3
            english[position+2] = word4
            english[position+4] = word1
            english[position+6] = word2
            word2.english = ""
            
def fix_adjectives(english, position):
    if ((position + 6) > len(english)-1):
        return
    word1 = english[position]
    word2 = english[position+2]
    word3 = english[position+4]
    word4 = english[position+6]
    if 'N' in word1.pos and 'A' in word2.pos and 'C' in word3.pos and 'A' in word4.pos:
        english[position] = word2
        english[position+2] = word3
        english[position+4] = word4
        english[position+6] = word1
    
        
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
        to_plus_verb_ending_in_r(englishDoc, index)
        direct_object_verb_flip(englishDoc, index)
        noun_adjective_flip(englishDoc, index)
        do_not(englishDoc, index)
        
        adv_v_o(englishDoc, index)
        deal_with_de(englishDoc, index)
        fix_adjectives(englishDoc, index)
        rule_qs(englishDoc, index)
        rule_ms(englishDoc, index)
        rule_reflexive(englishDoc, index)
        
        findBeginningSubject(englishDoc, index)
        
        
        
        
        
        
    for line in englishDoc:
        print(line.english)