'''
Rudimentary way to count:
characters
words (characters/5, which is how microsoft word and such counts words)
json nouns
json verbs

NOTE: Json verbs is based upon the appearance of the verbs in association with
the nouns, not that the verbs are unique.
'''

import sys
import string
import json

MYDIR = ['1-25', '26-50', '51-100', '101-150']
MYJSON = ['db-merged_v1.json', 'db-merged_v2.json', 'db-merged_v3.json', 'db-merged_v4.json', 'db-merged_v5.json']
#MYJSON = ['convertMoose.json']

if __name__ == "__main__":

    totalChars = 0
    totalWords = 0
    totalJsonN = 0
    totalJsonV = 0

    for mydir in MYDIR:
        words = 0
        chars = 0
        #print("Reading from directory", mydir)

        with open(mydir + '/' + 'list.json', 'r') as data_file:
            fileArray = json.load(data_file)

        for filename in fileArray:
            # print("Reading ", filename)
            f = open(mydir + '/' + filename, 'rU')
            text = f.read()

            chars += len(text)

        words = chars//5
        totalChars += chars
        totalWords += words
        print("Dir", mydir, "characters =", chars, "words =", words)

    words = chars//5

    for jsonfile in MYJSON:
        jsonNouns = 0
        jsonVerbs = 0

        with open(jsonfile, 'r') as data_file:
            myarray = json.load(data_file)

        for pair in myarray: # (noun:cat assoc: [])
            jsonNouns += 1
            for verbs in pair['assoc']: # assoc: [verbs,verbs]
                jsonVerbs += verbs['freq']

        totalJsonV += jsonVerbs
        totalJsonN += jsonNouns
        print(jsonfile, "nouns =", jsonNouns, "verbs =", jsonVerbs)

    print("Total Characters", totalChars)
    print("Total Words", totalWords)
    print("Total Json Nouns", totalJsonN)
    print("Total Json Verbs", totalJsonV)
