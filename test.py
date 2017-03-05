import sys
from nltk.corpus import brown, gutenberg
from nltk import sent_tokenize, word_tokenize, pos_tag

sentence_list = gutenberg.sents('austen-emma.txt')
filtered_list = []

noun = "boy"
#this is a comment
for sentence in sentence_list:
    for word in sentence:
            if word == noun:
                #print(sentence)
                filtered_list.append(sentence)

print(len(filtered_list))

nouns_and_verbs = []

for filtered_sentence in filtered_list:
    text = filtered_sentence

    tagged_tokens = pos_tag(text)

    for sentence in tagged_tokens:
        if sentence[1] == "NN":
            nouns_and_verbs.append(sentence[0])
        elif sentence[1] == "VB":
            nouns_and_verbs.append(sentence[0])

print(len(nouns_and_verbs))
print nouns_and_verbs
