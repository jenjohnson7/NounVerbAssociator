import sys
import json
from en import verb, noun
from nltk.corpus import brown
#from nltk.corpus import gutenberg
from nltk import sent_tokenize
from nltk import pos_tag

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
            key = verb.infinitive(word)
            #convert the verb into infinitive form to insert into dictionary

            default_temp_dict = dict()
            default = default_temp_dict
            #if the noun form has changed and is not in the dictionary.
            #exception catcher: Atlanta's vs Atlanta
            temp_dict = all_nouns.setdefault(singular_noun, default)

            if temp_dict.has_key(key):
                #add/update its frequency in the dictionary
                temp_dict[key]+=1
            else:
                temp_dict[key]=1
            all_nouns[singular_noun] = temp_dict
            break
            #only get the next verb after the noun, not all verbs in sentence

def main():
    #sentence_list = gutenberg.sents('austen-emma.txt')
    sentence_list = brown.sents('ca01')

    all_nouns = dict()

    for sentence in sentence_list:
        for i in range(0, len(sentence)): #for word in sentence
            word = sentence[i]
            text = [word]
            #must call pos_tag on a list, otherwise it will pos_tag each letter
            word_and_pos = pos_tag(text)
            current_pos = word_and_pos[0][1]

            #all nouns (singular and plural) but not proper
            if current_pos[0] == "N":
                if not current_pos[-1] == "P":
                    singular_noun = noun.singular(word)
                    #only insert the singular form of verb into dictionary
                    if all_nouns.has_key(singular_noun):
                        find_next_verb(i, sentence, singular_noun, all_nouns)
                    else:
                        verb_dictionary = dict()
                        all_nouns[word] = verb_dictionary
                        find_next_verb(i, sentence, singular_noun, all_nouns)

    # #sort all_nouns alphabetically into a list
    # sorted_nouns = sorted(all_nouns, key=all_nouns.get)
    #
    # all_nouns_final = dict()
    #
    # #put the nouns back into a new alphabetically-ordered dictionary
    # for i in range (0, len(sorted_nouns)):
    #     all_nouns_final[sorted_nouns[i]] = all_nouns[sorted_nouns[i]]

    #sort each dictionary in all_nouns by frequency
    for word in all_nouns.keys():
        #for verb in all_nouns[word].keys():
        verbs = all_nouns[word].keys()
        num_verbs = len(all_nouns[word].keys())
        for x in range (0, num_verbs):
            #sorted_verbs = sorted(all_nouns[word])#, key = all_nouns[word][verbs[x]]) ERROR: INT OBJECT NOT CALLABLE.
            #sorted_verbs = sorted(all_nouns[word], key = all_nouns[word].get(verbs[x])) ERROR: INT OBJECT NOT CALLABLE.
            ordered_dict = dict()

            #put the values back into a new dictionary, put it back into all_nouns
            # for i in range (0, len(sorted_verbs)):
            #     ordered_dict[sorted_verbs[i]] = all_nouns[word][sorted_verbs[i]]

    #write dictionary to json file
    with open('data.json', 'w') as outfile:
        json.dump(all_nouns, outfile)

if __name__ == "__main__":
    main()
