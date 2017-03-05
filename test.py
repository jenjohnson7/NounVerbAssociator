import sys
from nltk.corpus import brown, gutenberg
from nltk import sent_tokenize, word_tokenize, pos_tag

sentence_list = gutenberg.sents('austen-emma.txt')
filtered_list = []

noun = "boy"

for sentence in sentence_list:
    for word in sentence:
            if word == noun:
                filtered_list.append(sentence)

print(str(len(filtered_list)) + " sentences containing boy")

verb_dictionary= {}

for filtered_sentence in filtered_list:
    #need_a_verb = True
    for word in range (0, len(filtered_sentence)):
        if filtered_sentence[word]==noun:
            current_pos = "NN"
            for next_word in range (word+1, len(filtered_sentence)):
                text = [filtered_sentence[next_word]]
                word_and_pos = pos_tag(text)
                current_pos = word_and_pos[0][1]
                if current_pos == "VG":
                    verb_dictionary[filtered_sentence[next_word]]=1
print(verb_dictionary)
