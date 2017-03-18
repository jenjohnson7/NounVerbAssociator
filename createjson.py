import sys
import json
import string

from nltk.corpus import brown
from nltk.corpus import gutenberg
#from nltk.corpus import gutenberg
from nltk import sent_tokenize
from nltk import pos_tag
import operator
from collections import OrderedDict

def find_next_verb(noun_index, sentence, singular_noun, all_nouns):
    current_pos = "NN"
    for next_word in range (noun_index+1, len(sentence)):
        #starting from the next index, get pos
        word = sentence[next_word]
        text = [word]
        #must call pos_tag on a list, otherwise it will pos_tag each letter
        word_and_pos = pos_tag(text)
        current_pos = word_and_pos[0][1]
        if current_pos[0] == "V":
            #if pos is verb of any tense
            lower_cased_verb = word.lower()
            key = lower_cased_verb #en #edited
            #convert the verb into infinitive and lower cased form to insert into dictionary

            default_temp_dict = dict()
            default = default_temp_dict
            #if the noun form has changed and is not in the dictionary.
            #exception catcher: Atlanta's vs Atlanta
            temp_dict = all_nouns.setdefault(singular_noun, default)

            if key in temp_dict:
                #add/update its frequency in the dictionary
                temp_dict[key]+=1
            else:
                temp_dict[key]=1
            all_nouns[singular_noun] = temp_dict
            break
            #only get the next verb after the noun, not all verbs in sentence

def strip_sentence_v1(sentence):
    '''
    Parameters: sentence [tokenized and speech tagged sentence (should be
        array of tuples)]
    Return: array with noun in a[0] and verbs following it.
    '''
    found = False #if noun has been found, don't find other nouns
    stripped_sent = []

    for pairs in sentence: #pairs are just word and pos pairs
        #print(pairs)

        if (pairs[1] == 'NN') and (not found): #checking for noun
            stripped_sent.append(pairs[0])
            found = True

        elif (pairs[1] == 'VBD') and (found): #checking for subsequent verbs
            stripped_sent.append(pairs[0])

    return stripped_sent

def filter_noun(noun):
    '''
    Parameters: noun (string)
    Returns: noun (string)
    Takes a noun, makes it singular, removes proper nouns, and lowers it's case.
    '''
    #proper nouns can be ignored if we make sure that the NN tagging is not NNP
    #this would also solve the case for POS because POS would be NNP if not POS

    #noun = noun.singular(noun) <== need en library
    noun = noun.lower()
    #noun = noun.strip(string.punctuation) #to remove trailing punctuation that
                                        # I have noticed sometimes appears
    return noun


def filter_verb(verb):
    '''
    Parameters: verb (string)
    Returns: verb (string)
    Takes a verb, converts it to infinitive, and lowers it's case.
    '''
    #verb = verb.infinitive(lower_cased_verb) <== need en library
    verb = verb.lower()

    return verb

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

def temp_insert_corpus(my_dict, corpus_sents):
    '''
    Parameters: my_dict (dict), corpus_sents (array of tokenized POS sentences)
    Noel's temporary corpus inserting function
    '''
    for sentence in corpus_sents:
        strip_arr = strip_sentence_v1(sentence)

        if (len(strip_arr) >= 2):
            filtered = filter_noun(strip_arr[0])

        for i in range(1, len(strip_arr)):
            insert_verb_object(my_dict, filtered, filter_verb(strip_arr[i]))

    return my_dict

def main():
    '''
    #sentence_list = gutenberg.sents('austen-emma.txt')
    #sentence_list = brown.sents('ca01')
    #sentence_list = brown.sents('cl13') #mystery
    #sentence_list = brown.sents('cm01') #sci-fi
    '''


    ##test = brown.tagged_sents(categories='mystery')
    # print(test[0])
    # print('This is my break \n \n')
    # print(test[0][0])
    # print('\n \n')
    # print(test[0][0][0])
    #
    # print('\n\n')

    #corpus_sents = brown.tagged_sents('cl13') #mystery
    #corpus_sents = brown.tagged_sents(categories='mystery')
    # mystery = brown.tagged_sents(categories='mystery')
    # romance = brown.tagged_sents(categories='romance')
    # fiction = brown.tagged_sents(categories='ficiton')
    # adventure = brown.tagged_sents(categories='adventure')
    # lore = brown.tagged_sents(categories='lore')
    # science_fiction = brown.tagged_sents(categories='science_fiction')
    # religion = brown.tagged_sents(categories='religion')
    corpus_sents = brown.tagged_sents(categories=['mystery','romance','ficiton','adventure','lore','science_fiction','religion','humor'])

    my_dict = {}
    my_dict = temp_insert_corpus(my_dict, corpus_sents)

    # for sentence in corpus_sents:
    #     strip_arr = strip_sentence_v1(sentence)
    #     print('mylooptest')
    #     print(sentence)
    #     print(strip_arr)
    #     print(strip_arr[0])
    #     break

    # for sentence in corpus_sents:
    #     strip_arr = strip_sentence_v1(sentence)
    #
    #     if (len(strip_arr) >= 2):
    #         filtered = filter_noun(strip_arr[0])
    #
    #     for i in range(1, len(strip_arr)):
    #         insert_verb_object(my_dict, filtered, filter_verb(strip_arr[i]))
    #
    # print(my_dict)


    #write dictionary to json file
    with open('newdata.json', 'w') as outfile:
        json.dump(my_dict, outfile)

if __name__ == "__main__":
    main()
