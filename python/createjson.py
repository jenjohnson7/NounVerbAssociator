'''
Creates json files based on the five models by using raw data sets
'''

import sys
import json
import string

import tokenizer_test
# from nltk.corpus import brown
from nltk.corpus import gutenberg
# from nltk.corpus import gutenberg
from nltk import sent_tokenize
from nltk import pos_tag
import operator
from collections import OrderedDict
from nltk.stem.wordnet import WordNetLemmatizer

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
    Parameters: sentence [tokenized and speech tagged sentence (array of tuples)]
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

def strip_sentence_v3(sentence):
    '''
    Parameters: sentence [tokenized and speech tagged sentence (should be
        array of tuples)]
    Return: arrays found_nouns and found_verbs

    Finds all nouns in a tokenized sentence and pairs them with all other verbs
    '''

    found_nouns = []
    found_verbs = []

    for pairs in sentence: #pairs are just word and pos pairs
        #print(pairs)

        #NN=singular noun, NNS=plural noun, NNPS= proper noun plural
        if (pairs[1] == 'NN' or pairs[1] == 'NNS' or pairs[1] == 'NNPS'): #checking for noun
            found_nouns.append(pairs[0])

        elif (pairs[1][0] == 'V'): #checking for verbs
            found_verbs.append(pairs[0])

    return found_nouns, found_verbs

def strip_sentence_v4(sentence):
    '''
    Parameters: sentence [tokenized and speech tagged sentence (should be
        array of tuples)]
    Return: arrays stripped_sent and pos_arr

    Uses the pos_arr for use in the insert_corpus_v4 and insert_corpus_v5 functions

    '''
    pos_arr = []
    stripped_sent = []

    for pairs in sentence: #pairs are just word and pos pairs

        #NN=singular noun, NNS=plural noun, NNPS= proper noun plural
        if (pairs[1] == 'NN' or pairs[1] == 'NNS' or pairs[1] == 'NNPS'): #checking for nouns
            stripped_sent.append(pairs[0])
            pos_arr.append(pairs[1])

        elif (pairs[1][0] == 'V'): #checking for subsequent verbs
            stripped_sent.append(pairs[0])
            pos_arr.append(pairs[1])

    return stripped_sent, pos_arr

def filter_noun(input_noun):
    '''
    Parameters: noun (string)
    Returns: noun (string)
    Takes a noun, makes it singular, removes proper nouns, and lowers it's case.
    '''
    #proper nouns can be ignored if we make sure that the NN tagging is not NNP
    #this would also solve the case for POS because POS would be NNP if not POS

    input_noun = input_noun.replace('_', "")
    input_noun = input_noun.lower()
    input_noun = WordNetLemmatizer().lemmatize(input_noun,'n')

    return input_noun

def filter_verb(input_verb):
    '''
    Parameters: verb (string)
    Returns: verb (string)
    Takes a verb, converts it to infinitive, and lowers its case.
    '''

    input_verb = input_verb.replace('_', "") #textfiles use _ to represent italics
    input_verb = input_verb.lower()

    if (input_verb == "'s"):
        # 'is' is lemmatized as 'be'
        return 'be'

    elif (input_verb == "'ve"):
        return 'have'

    elif (input_verb == "'m"): #We have no idea what this is a contraction for
        return ''

    elif (input_verb == ''): # to exit early and prevent further checking
        return ''

    elif ( '¿' in input_verb): #caused by errors in tokenization/textfiles
        return ''

    elif (input_verb[0] == "'"):
        input_verb = input_verb[1:]

    return WordNetLemmatizer().lemmatize(input_verb,'v')


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

    if not (verb == ''):
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

def insert_corpus_v3(my_dict, corpus_sents):
    '''
    Parameters: my_dict (dict), corpus_sents (array of tokenized POS sentences)
    Returns: my_dict
    Inserts tokenized POS sentences into my_dict using version 3 method.

    All nouns-->All verbs (before and after)
    '''

    for sentence in corpus_sents:
        found_nouns, found_verbs = strip_sentence_v3(sentence)

        for found_noun in found_nouns:
            for found_verb in found_verbs:
                # for all nouns, insert all verbs
                insert_verb_object(my_dict, filter_noun(found_noun), filter_verb(found_verb))

    #print(my_dict)
    return my_dict

def insert_corpus_v4(my_dict, corpus_sents):
    '''
    Parameters: my_dict (dict), corpus_sents (array of tokenized POS sentences)
    Returns: my_dict
    Inserts tokenized POS sentences into my_dict using version 4 method.

    All nouns-->All verbs UNTIL the next noun.
    '''
    for sentence in corpus_sents:
        strip_arr, pos_arr= strip_sentence_v4(sentence)
        #strip_arr contains all nouns and verbs in order of appearance
        #pos_arr is the pos for strip_arr

        for i in range (0, len(pos_arr)):
            if pos_arr[i][0] == "N" and i <len(pos_arr)-1:
                # get all nouns unless it is the last one
                    #the last noun will not have any following verbs
                found_noun = filter_noun(strip_arr[i])
                #print(found_noun)

                current_index = i+1
                current_pos = pos_arr[current_index][0]

                while current_pos == "V" and current_index <len(pos_arr):
                    # get the following verbs until another noun is found
                    found_verb = filter_verb(strip_arr[current_index])
                    #print(found_verb)
                    insert_verb_object(my_dict, found_noun, found_verb)

                    #update steps for the while loop
                    current_index +=1
                    if current_index <len(pos_arr):
                        current_pos = pos_arr[current_index][0]

    return my_dict

def insert_corpus_v5(my_dict, corpus_sents):
    '''
    Parameters: my_dict (dict), corpus_sents (array of tokenized POS sentences)
    Returns: my_dict
    Inserts tokenized POS sentences into my_dict using version 5 method.

    All nouns-->ALL verbs AFTER
    '''

    for sentence in corpus_sents:
        strip_arr, pos_arr = strip_sentence_v4(sentence)
        #strip_arr contains all nouns and verbs in order of appearance
        #pos_arr is the pos for strip_arr
        #uses version 4, but different insertion technique

        for i in range (0, len(pos_arr)):
            if pos_arr[i][0] == "N": #finding each noun
                found_noun = filter_noun(strip_arr[i])
                for j in range (i+1, len(pos_arr)): #finding all following verbs
                    if pos_arr[j][0]=="V":
                        found_verb = filter_verb(strip_arr[j])
                        insert_verb_object(my_dict, found_noun, found_verb)

    return my_dict

def create_json(directory, fileArray, jsonTarget, version):
    '''
    Parameters: name of directory, an array of file names of text files to open and make into corpus;
    a name for the target json file ('something.json'); the model version for the program (integer)
    Creates a json file and saves it at newName.
    '''
    myDict = {}

    for filename in fileArray:
        print("Reading in ", filename)
        corpus_sents = tokenizer_test.read_from_file(directory + '/' + filename) #an array of tokenized data

        if version == 1:
            myDict = insert_corpus_v1(myDict, corpus_sents)
        elif version == 2:
            myDict = insert_corpus_v2(myDict, corpus_sents)
        elif version == 3:
            myDict = insert_corpus_v3(myDict, corpus_sents)
        elif version == 4:
            myDict = insert_corpus_v4(myDict, corpus_sents)
        else: #version ==5
            myDict = insert_corpus_v5(myDict, corpus_sents)

        print('Added ', filename, 'to dict version ', version)

    with open(directory + '/' + jsonTarget, 'w') as outfile:
        json.dump(myDict, outfile)

    print('Wrote to ', jsonTarget, '. Finished Successfully.')


def main():
    '''

    '''
    print('Currently used as module')

    # toConvert = ["bone_assassin.txt", "buckley_old_tales_greece.txt", "dumas_black_tulip.txt", "hunt_young_farmer.txt", "lang_he.txt", "memoir_leonora_christina.txt"]
    #
    # # for i in range(0, 6):
    # #     target = 'test' + str(i) + '.json' # dir/name#.json
    # #     create_json('gutenberg', toConvert, target, i)
    # #     convertForDB.convert('gutenberg/' + target)
    #
    # my_dict_v1 = {}
    # my_dict_v2 = {}
    # my_dict_v3 = {}
    # my_dict_v4 = {}
    # my_dict_v5 = {}
    #
    # for textfile in toConvert:
    #     location = 'gutenberg/' + textfile
    #     my_dict_v1 = insert_corpus_v1(my_dict_v1, tokenizer_test.read_from_file(location))
    #     print(textfile)
    #
    # # with open('defaultgutenbergv1.json', 'w') as outfile:
    # #     json.dump(data_dict, outfile)
    #
    # with open('testing.json', 'w') as outfile:
    #     json.dump(data_dict, outfile)
    # # with open('textdatafolder/1661.json','w') as outfile:
    # #     json.dump(data_dict, outfile)


if __name__ == "__main__":
    main()
