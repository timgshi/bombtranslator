CS124 Final Assignment

Tim Shi
Chloe Yeung
Victoria Kwong

F Language: Spanish
1. One of the differences between Spanish and English is that Spanish sentences may start with a subjectless sentence. For example, Es una muter. The sentence requires context from previous sentence(s) to determine the subject of the sentence. 
2. Spanish has strong rules with regards to how verbs are conjugated. 
3. Spanish has a multiple forms of past tense that suggest either an action that occurred once or multiple times. Some of these translations are not always fully expressed in English.
4. In english, adjectives typically appear before a noun but in Spanish, adjectives follow after the noun. For example, idioma español.  

Input:
El idioma español o castellano es una lengua romance del grupo ibérico. 
Es uno de los seis idiomas oficiales de la ONU. 
Es la segunda lengua más hablada del mundo por el número de personas que la tienen como lengua materna, tras el chino mandarín.
Es también idioma oficial en varias de las principales organizaciones político-económicas internacionales.
Lo hablan como primera y segunda lengua más de 450 millones, y supera los 500 millones de personas si contamos a los que lo han aprendido como lengua extranjera, pudiendo ser la tercera lengua más hablada por el total de hablantes.
El español, como las otras lenguas romances , es una continuación moderna del latín hablado, desde el siglo III.
La historia del idioma español comienza con el latín vulgar del Imperio romano, concretamente con el de la zona central del norte de Hispania.
Tras la caída del Imperio romano en el siglo V , la influencia del latín culto en la gente común fue disminuyendo paulatinamente.
El latín hablado de entonces fue el fermento de las variedades romances hispánicas, origen de la lengua española.
En el siglo VIII , la invasión musulmana de la Península Ibérica hace que se formen dos zonas bien diferenciadas.

Output: 
The Spanish or Castilian language is a language romance of Iberian group.
It is one of the six official languages of the UN.
The second is language more spoken of world by the to number of people that the have as maternal language, after the Chinese mandarin.
Also is official in language more of the main political-economic international organizations.
It as first and second language more speak of 450 million, and than the 500 people if million  we to the that it learned have as foreign language,
I can the third language more be by the spoken total of speakers.
The Spanish, as the others languages romances is a modern continuation of spoken Latin, from the century III.
The history of Spanish language begins with the vulgar Latin of Roman Empire, specifically with the of the central area of north of Hispanic.
After the fall of Roman in Empire the century V the influence of Latin in cult the common people was gradually decreasing.
The spoken Latin of then the was ferment of the varieties Hispanic romances, origin of the Spanish language.
In the century VIII the Muslim invasion of the Iberian peninsula ago that is form two well areas differentiated.


Rules:
1.
2.
3.
4.
5. Looks for adverbs to adjust their order according to the rules of English. Adverbs found two positions after a verb adjusted to swap positions with the verb.
6. Swaps the order of words around the Spanish "de." In Spanish the possessive object comes before the subject and the order needs to be swapped to match the ordering of English. If the noun after the "de" is also followed by either a noun or adjective, both the third and fourth words are moved to be in front of the "de."
7. Searches for words in a sequence of noun, adjective, conjunctive, adjective, then reorders them to adjective, conjunctive, adjective, noun. 
8. Looks for intransitive verbs, which are verbs without a subject. The rule looks for intransitive verbs that are followed by a noun (proper/pronoun included). It will then switch this noun and verb form to follow english grammar of passive voice. 
9. Rule looks for sentences without a subject by looking for verbs following punctuation. It then analyzes the form of the verb and its tense using regular expressions to determine the subject of the sentence. It replaces these words' Word.english in the arrays with the subject and verb.
10.

Error analysis:
1. Missing Subject
Es también idioma oficial en varias de las principales organizaciones político-económicas internacionales.
[Also is] official in language more of the main political-economic international organizations.
This sentence is missing a subject at the beginning of the sentence. The issue that our rules did not catch is that Also is at the beginning of the sentence instead of a verb where our code only checks to see if there is a verb at the start of the sentence. To better implement this, we could instead search to see if there is a subject at all before a verb and if not, then deal with the issue that the subject is missing.

2. Adjective-Noun Structure
El idioma español o castellano es una lengua romance del grupo ibérico.
The Spanish or Castilian language is a [language romance] of Iberian group.

Our translation did not catch that this phrase should actually be "romance language". However, it did switch "Iberian group." 

Google Translate:
Spanish or Castilian is an Iberian Romance language group.
It is one of the six official UN languages​​.
It is the second most spoken language in the world by the number of people who are native speakers, after Mandarin Chinese.
It is also an official language in several major international political and economic organizations.
It is spoken as a first and second language more than 450 million and more than 500 million people if you count those who have learned as a foreign language can be the third most spoken language by total speakers.
The Spanish, like other Romance languages, is a modern continuation of spoken Latin, from the third century.
The story begins with the Spanish language Vulgar Latin of the Roman Empire, specifically that of the central part of northern Spain.
After the fall of the Roman Empire in the V century, the influence of Latin worship in the common people was gradually diminishing.
The spoken Latin of that time was the ferment of Hispanic Romance varieties, of Spanish origin.
In the eighth century, the Muslim invasion of the Iberian Peninsula makes the formation of two distinct areas.

Google Analysis:
1. Sentence Structure
Es la segunda lengua más hablada del mundo por el número de personas que la tienen como lengua materna, tras el chino mandarín.
It is the second most spoken language in the world by the number of people who are native speakers, after Mandarin Chinese.

The sentence structure of the placement of "by the number…speakers" makes the English translation difficult to comprehend upon first read. While the meaning can be deciphered, ie. it makes some sense, the sentence is not well structured. It appears, when comparing it to the original Spanish sentence, that Google directly translated this sentence as there appears no way to correctly rearrange the sentence without rearranging all of the sentence structure. (Ie. By the number of people who are native speakers, Spanish is the second most spoken language, after Mandarin, in the world.  

Members:
Chloe built the starter code that reads a spanish file as well as a mobypos text file. Then, the code will build a dictionary that takes each spanish word in the file and stores the english translation. Finally, it will iterate through the spanish file and store an array with each element being of a class Word which stores the spanish word, english word, and the part of speech array. 
Chloe, Tim, and Victoria each took 3-4 sentences of the spanish file and translated the words, storing it into dict.txt.
Victoria wrote rules 1-4, Tim 5-7, and Chloe 8-10.