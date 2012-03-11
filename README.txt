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
1. This first rule looks for a noun and an adjective modifying the noun. In English, modifiers are always placed in front of the noun it is describing. For example, we would say “the pretty woman” in English. However, in Spanish, the adjective usually goes after the noun it is modifying. In our example, “the pretty woman” would be “la mujer bonita” in Spanish. Thus our rule sees the pattern “noun adjective” in Spanish and then flips the position of these two words for the English translation.
2. This second rule looks for a verb and more specifically one that ends in “r” in Spanish. The unconjugated form of a Spanish verb always ends in “ar”, “er”, or “ir”. This unconjugated form is English equivalent of the infinitive. For example, we would say in Spanish “Me gusta beber Diet Coke.” Directly translated to English, this would be “I like drink Diet Coke.” However, this obviously is not a grammatically correct sentence. Thus we must isolate all these instances of verbs ending in “r” in Spanish and after translating it to English, add “to” in front of the verb. Thus the correct form of our example would be “I like to drink Diet Coke.”
3. This third rule looks for the word “no” in front of a verb in Spanish. The addition of the word “no” to a verb serves to negate the verb. For example, to negate the phrase “Tengo dinero”, we would simply say “No tengo dinero.” Directly translated to English, “Tengo dinero” becomes “I have money” and “No tengo dinero” becomes “I no have money.” Unfortunately, the negated version in English is not grammatically correct. Instead, what we want to say is “I do not have money”. Thus our third rule seeks to find all the verb phrases in Spanish that are “no + verb” and turn them into “do not + verb.”
4. This fourth rule deals with direct objects. In English, all of our sentences follow the structure “subject verb directObject”. For example, we would say “I ate it.” However in Spanish, whenever the direct object becomes generalized to a direct object pronoun such as “lo”, the sentence structure is altered. In Spanish, the order becomes “subject directObject verb”. Thus “I ate it” in Spanish becomes “Me lo comí” in order for us to be grammatically correct. Then, whenever this rule sees the format “noun lo/la/los/las verb” in Spanish, it changes the order to “noun verb lo/la/los/las” for the English translation.
5. Looks for adverbs to adjust their order according to the rules of English. Adverbs found after a verb adjusted to swap positions with the verb. Example corrió rápidamente is adjusted to translate to ran quickly.
6. This rule takes care of irregularities between sentences that use "de" in Spanish and their English counterparts. Sentences are reordered to make sense in English and the "de" is removed when we find nouns or noun phrases wrapped around a "de." For example "hablado de entonces" is rearranged to "then discussed."
7. Searches for words in a sequence of noun, adjective, conjunctive, adjective, then reorders them to adjective, conjunctive, adjective, noun. This fixes sentences like "muchacho blanco y rubio" to "white and blond man."
8. Looks for intransitive verbs, which are verbs without a subject. The rule looks for intransitive verbs that are followed by a noun (proper/pronoun included). It will then switch this noun and verb form to follow english grammar of passive voice. 
9. Rule looks for sentences without a subject by looking for verbs following punctuation. It then analyzes the form of the verb and its tense using regular expressions to determine the subject of the sentence. It replaces these words' Word.english in the arrays with the subject and verb.
10. This final rule deals with the reflexive verb in Spanish. Unlike English, Spanish contains a whole subset of verbs whose unconjugated form is “verb+se” (ie. lavarse = to wash oneself, ducharse = to shower oneself, etc). For example, we would say “Yo me llamo Joey.” Directly translated to English, this would be “I I am called Joey”. However, normal English sentences do not contain the second “I”. Instead, the reflexive part is usually implicit. Thus our English translation should be simply “I am called Joey.” This rule then ignores the reflexive pronoun and simply skips the translation of that word.

Error analysis:
1. Missing Subject
Es también idioma oficial en varias de las principales organizaciones político-económicas internacionales.
[Also is] official in language more of the main political-economic international organizations.
This sentence is missing a subject at the beginning of the sentence. The issue that our rules did not catch is that Also is at the beginning of the sentence instead of a verb where our code only checks to see if there is a verb at the start of the sentence. To better implement this, we could instead search to see if there is a subject at all before a verb and if not, then deal with the issue that the subject is missing.

2. Adjective-Noun Structure
El idioma español o castellano es una lengua romance del grupo ibérico.
The Spanish or Castilian language is a [language romance] of Iberian group.

Our translation did not catch that this phrase should actually be "romance language". However, it did switch "Iberian group." 

3. Extra Subject
Es la segunda lengua más hablada del mundo por el número de personas que la tienen como lengua materna, tras el chino mandarín.

[It the] second is language more spoken of world by the to number of people It that the have as maternal language, after the Chinese mandarin.

This sentence has extra subjects placed before articles. Our algorithm looks for verbs and inserts subjects if they're missing according to the tense of the verb. If however there is an article that preceeds the verb, the additional subject is added before the article "It the." We could improve upon this error by checking for articles and not inserting prounouns as the subject when appropriate.

4. Plural disagreement
El español, como las otras lenguas romances , es una continuación moderna del latín hablado, desde el siglo III.

The Spanish, as the [others languages romances] is a modern continuation of spoken Latin, from the century III.

In English, the word "other" is only pluralized when not followed by another noun. The correct sentence should have "other languages." To fix this issue, we could write a rule checking for the word "other" and making sure that it's pluraility matches the rules of English. 



Google Translate:
Spanish or Castilian is an Iberian Romance language group.
It is one of the six official UN languages.
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

2. Extra Article
El español, como las otras lenguas romances , es una continuación moderna del latín hablado, desde el siglo III.

The Spanish, like other Romance languages, is a modern continuation of spoken Latin, from the third century.

This sentence contains an unnecessary article before the subject "Spanish" in "The Spanish." This is a difficult problem because Spanish can refer to both the language and the people. When referring to the Spaniards, Spanish should have a "The" before it. This could be improved by recognizing that the original "Español" refers to the language and ensuring that it is not preceded by an article.

Members:
Chloe built the starter code that reads a spanish file as well as a mobypos text file. Then, the code will build a dictionary that takes each spanish word in the file and stores the english translation. Finally, it will iterate through the spanish file and store an array with each element being of a class Word which stores the spanish word, english word, and the part of speech array. 
Chloe, Tim, and Victoria each took 3-4 sentences of the spanish file and translated the words, storing it into dict.txt.
Victoria wrote rules 1-4, Tim 5-7, and Chloe 8-10.

