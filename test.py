import sys
from nltk.corpus import brown, gutenberg
from nltk import sent_tokenize, word_tokenize, pos_tag

#get sentences from a single text stored as a list
sentence_list = gutenberg.sents('austen-emma.txt')
filtered_list = []

#hardcoded for now
noun = "boy"

for sentence in sentence_list:
    for word in sentence:
        #if sentence contains noun, add to filtered_list
        if word == noun:
            filtered_list.append(sentence)

verb_dictionary = dict()

for filtered_sentence in filtered_list:
    for word in range (0, len(filtered_sentence)):
        if filtered_sentence[word]==noun:
            #get the index of the noun
            current_pos = "NN"
            for next_word in range (word+1, len(filtered_sentence)):
                #starting from the next index, get pos
                key = filtered_sentence[next_word]
                text = [filtered_sentence[next_word]]
                #must call pos_tag on a list, otherwise it will pos_tag each letter
                word_and_pos = pos_tag(text)
                current_pos = word_and_pos[0][1]
                if current_pos[0] == "V":
                    #if pos is verb of any tense
                    if verb_dictionary.has_key(key):
                        #add/update its frequency in the dictionary
                        verb_dictionary[key]+=1
                    else:
                        verb_dictionary[key]=1
                    break
                    #only get the next verb after the noun, not all verbs in sentence

#sort the dictionary by values into a list
sorted_verbs = sorted(verb_dictionary, key=verb_dictionary.get)

print(sorted_verbs)
#in the dictionary/list all strings are unicode and have u'' format when printed

for i in range (0, len(sorted_verbs)):
    print(sorted_verbs[i])
    #when you print the element, they are normal strings w/o u prefix
