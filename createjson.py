import sys
import json
import string

import tokenizer_test

from nltk.corpus import brown
from nltk.corpus import gutenberg
#from nltk.corpus import gutenberg
from nltk import sent_tokenize
from nltk import pos_tag
import operator
from collections import OrderedDict

def strip_sentence_v1(sentence):
    '''
    Parameters: sentence [tokenized and speech tagged sentence (should be
        array of tuples)]
    Return: array with noun in a[0] and verbs following it.

    Takes a tokenized sentence and strips down into a single array where index
    0 contains the first appearing noun and the subsequent elements are the
    following verbs in the sentence.

    Takes first noun and all following verbs
    '''
    found = False #if noun has been found, don't find other nouns
    stripped_sent = []

    for pairs in sentence: #pairs are just word and pos pairs
        #print(pairs)

        #NN=singular noun, NNS=plural noun, NNPS= proper noun plural
        if (pairs[1] == 'NN' or pairs[1] == 'NNS' or pairs[1] == 'NNPS') and (not found): #checking for noun
            stripped_sent.append(pairs[0])
            found = True

        elif (pairs[1][0] == 'V') and (found): #checking for subsequent verbs
            stripped_sent.append(pairs[0])

    return stripped_sent

def strip_sentence_v2(sentence):
    '''
    Parameters: sentece [tokenized and speech tagged sentence (array of tuples)]
    Returns: an array where 0,2,4,etc... are nouns and odds are verbs.

    Finds each noun in the sentence and stores the immediate following verb.
    '''
    find_noun = True #true means to search for noun, false means search for verb
    stripped_sent = []

    for pairs in sentence:

        if (pairs[1] == 'NN' or pairs[1] == 'NNS' or pairs[1] == 'NNPS') and (find_noun):
            stripped_sent.append(pairs[0])
            find_noun = False

        elif (pairs[1][0] == 'V') and not (find_noun):
            stripped_sent.append(pairs[0])
            find_noun = True

    return stripped_sent


def filter_noun(input_noun):
    '''
    Parameters: noun (string)
    Returns: noun (string)
    Takes a noun, makes it singular, removes proper nouns, and lowers it's case.
    '''
    #proper nouns can be ignored if we make sure that the NN tagging is not NNP
    #this would also solve the case for POS because POS would be NNP if not POS

    #input_noun = noun.singular(input_noun) <== need en library
    input_noun = input_noun.lower()
    #noun = noun.strip(string.punctuation) #to remove trailing punctuation that
                                        # I have noticed sometimes appears
    return input_noun


def filter_verb(input_verb):
    '''
    Parameters: verb (string)
    Returns: verb (string)
    Takes a verb, converts it to infinitive, and lowers it's case.
    '''
    #input_verb = verb.infinitive(input_verb) #<== need en library
    input_verb = input_verb.lower()

    return input_verb

#this is where we would want to add additional scoping pertaining to type of manner,
#definition, or anything beyond verb and frequency.
def create_verb_object(verb):
    '''
    Parameters: verb (string)
    Returns: verb_object (obj)
    Creates verb_object (obj with keys 'verb' 'freq')

    Note: called by insert_verb_object
    '''
    verb_object = {}
    verb_object['freq'] = 1
    verb_object['verb'] = verb

    return verb_object


def insert_verb_object(my_dict, noun, verb):
    '''
    Parameters: my_dict (dict), noun (string), verb (string)
    Returns: my_dict
    Inserts a verb_object into a given my_dict (hash object) at noun (key) in
    the form of a new array object. If my_dict does not have that noun (key), it
    will push the new noun into my_dict and creates an array with verb_object.
    Also handles frequency incrementing.

    Note: Also handles the insertion of nouns (keys), so received keys should
    already be filtered before running this function
    '''
    verb_found = False; #to determine if verb is already present in dict

    if noun in my_dict:
        for verb_object in my_dict[noun]: #checking each verb object within array
            if verb_object['verb'] == verb: #if verb value == verb
                verb_object['freq'] = verb_object['freq'] + 1
                verb_found = True;

        #creating verb_object and inserting into my_dict at key noun
        if not verb_found:
            verb_object = create_verb_object(verb)
            my_dict[noun].append(verb_object)

    else: #if key noun is not in my_dict
        verb_object = create_verb_object(verb)
        my_dict[noun] = [verb_object]

    return my_dict

def insert_corpus_v1(my_dict, corpus_sents):
    '''
    Parameters: my_dict (dict), corpus_sents (array of tokenized POS sentences)
    Inserts tokenized POS sentences into my_dict using version 1 method.
    '''
    for sentence in corpus_sents:
        strip_arr = strip_sentence_v1(sentence)

        if (len(strip_arr) >= 2):
            filtered = filter_noun(strip_arr[0])

        for i in range(1, len(strip_arr)): #checking for the verbs
            insert_verb_object(my_dict, filtered, filter_verb(strip_arr[i]))

    return my_dict

def insert_corpus_v2(my_dict, corpus_sents):
    '''
    Parameters: my_dict (dict), corpus_sents (array of tokenized POS sentences)
    Returns: my_dict
    Inserts tokenized POS sentences into my_dict using version 2 method.
    '''
    for sentence in corpus_sents:
        strip_arr = strip_sentence_v2(sentence)

        length = len(strip_arr)
        if (length % 2 == 1): #cutting off the final verb or noun to make the array even size
            length = length - 1

        for i in range(0, length, 2): #starting at 0 and increasing i by 2
            insert_verb_object(my_dict, filter_noun(strip_arr[i]), filter_verb(strip_arr[i+1]))
            #print(filter_noun(strip_arr[i]))

    return my_dict

def main():
    '''
    #sentence_list = gutenberg.sents('austen-emma.txt')
    #sentence_list = brown.sents('ca01')
    #sentence_list = brown.sents('cl13') #mystery
    #sentence_list = brown.sents('cm01') #sci-fi
    '''

    corpus_sents = brown.tagged_sents(categories=['mystery','romance','ficiton','adventure','lore','science_fiction','religion','humor'])
    corpus_sents2 = tokenizer_test.read_from_file('document.txt')
    print(corpus_sents2)

    my_dict_jen = {}
    my_dict_jen = insert_corpus_v2(my_dict_jen, corpus_sents2)

    # my_dict_v1 = {}
    # my_dict_v2 = {}
    #
    # my_dict_v1 = insert_corpus_v1(my_dict_v1, corpus_sents)
    # my_dict_v2 = insert_corpus_v2(my_dict_v2, corpus_sents)

    # #write dictionary to json file
    # with open('datav1.json', 'w') as outfile:
    #     json.dump(my_dict_v1, outfile)
    #
    # with open('datav2.json', 'w') as outfile:
    #     json.dump(my_dict_v2, outfile)

    with open('mouse.json','w') as outfile:
        json.dump(my_dict_jen, outfile)

if __name__ == "__main__":
    main()
