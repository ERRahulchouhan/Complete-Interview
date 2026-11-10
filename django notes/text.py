from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

def rephrase_sentence(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)

    # Initialize an empty list to store the rephrased words
    rephrased_words = []

    # Iterate over each word in the sentence
    for word in words:
        # Get synonyms for the word from WordNet
        synonyms = wordnet.synsets(word)

        # If synonyms exist, choose the first one as a rephrased word
        if synonyms:
            rephrased_word = synonyms[0].lemmas()[0].name()
        else:
            rephrased_word = word

        # Add the rephrased word to the list
        rephrased_words.append(rephrased_word)

    # Join the rephrased words to form a sentence
    rephrased_sentence = ' '.join(rephrased_words)

    return rephrased_sentence

# Example usage
sentence = "How to do rephrase using Python?"
rephrased_sentence = rephrase_sentence(sentence)
print(rephrased_sentence)
