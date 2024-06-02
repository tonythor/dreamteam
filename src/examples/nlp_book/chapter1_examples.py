import matplotlib.pyplot as plt
import nltk
from nltk.book import *

# dispersion plot
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
# plt.show()

# word frequency
fdist = FreqDist(text1)
# fdist.plot(75, cumulative=True)

# find long words using list comprehension 
corpus = set(text1)
long_words = [w for w in corpus if len(w) > 15]
sorted(long_words)


### show the first N sentences of this book.
import nltk
from nltk.tokenize import sent_tokenize

def print_sentences(corpus, start, end):
    """
    Prints sentences from the corpus within the specified range.

    Parameters:
    corpus (nltk.text.Text): The input text corpus.
    start (int): The start index of the sentence range.
    end (int): The end index of the sentence range.
    """
    text_string = ' '.join(corpus)    
    sentences = sent_tokenize(text_string)    
    selected_sentences = sentences[start:end]
    for i, sentence in enumerate(selected_sentences, start + 1):
        print(f"Sentence {i}: {sentence}")

# Example usage:
from nltk.book import text5
print_sentences(text5, 0, 50)
