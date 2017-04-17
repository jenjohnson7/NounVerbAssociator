import sys
from nltk.corpus import brown

from nltk import sent_tokenize, word_tokenize
from nltk import pos_tag

def read_from_file(file_name):
    """ reads in a text file into a usable format"""
    #for comparison purposes
    #sentence_list = brown.tagged_sents('ca01')
    #print(sentence_list)

    f = open(file_name, 'rU')
    raw = f.read()
    sentences = sent_tokenize(raw)
    read_from_file_corpus = []
    sentence_array = []
    for sentence in sentences:
        # temp = []

        words = word_tokenize(sentence)
        word_and_pos = pos_tag(words)

        # for word in words:
        #     print(word)
        #     word_array = [word]
        #     # have to call on a list to prevent each letter from being tagger
        #     word_and_pos = pos_tag(word_array)
        #     #temp.append(word_and_pos)
        #     print(word_and_pos)

        #read_from_file_corpus.append(temp)
        sentence_array.append(word_and_pos)

    #read_from_file_corpus.append(sentence_array)

    #print(sentence_array)
    return sentence_array

def read_from_raw(raw):
    '''
    Takes raw text data and converts it
    '''
    sentences = sent_tokenize(raw)
    read_from_file_corpus = []
    sentence_array = []
    for sentence in sentences:
        # temp = []

        words = word_tokenize(sentence)
        word_and_pos = pos_tag(words)


        #read_from_file_corpus.append(temp)
        sentence_array.append(word_and_pos)

    #read_from_file_corpus.append(sentence_array)

    #print(sentence_array)
    return sentence_array


def main():
    #calls read_from_file
    sentence_array = read_from_file()

if __name__ == "__main__":
    main()
