from nltk.corpus import inaugural
import re


# inaugural.fileids()

bonehead =  inaugural.raw('2017-Trump.txt')
# bonehead[0:300]
trump_substrings = re.split(r'[ \n]+', bonehead)
trump_corpus = set(trump_substrings)
trump_long_words = [w for w in trump_corpus if len(w) > 10]
sorted(trump_long_words)


obama = inaugural.raw('2009-Obama.txt')
obama_substrings = re.split(r'[ \n]+', obama)
obama_corpus = set(obama_substrings)
obama_long_words = [w for w in obama_corpus if len(w) > 10]
sorted(obama_long_words)


from nltk.corpus import wordnet as wn
print(wn.synsets('motorcar'))
print(wn.synset('car.n.01').lemma_names())
print(wn.synset('car.n.01').definition())
motorcar = wn.synset('car.n.01')
print(motorcar)
print() 
print("hyponyms")
types_of_motorcar = motorcar.hyponyms()
print(types_of_motorcar)
print()
print("hyponym paths")
paths = motorcar.hypernym_paths()
print(paths)