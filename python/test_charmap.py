'''
Tests the text files listed in list.json to make sure that all characters
are readable
'''
import sys
import json
import string


def test():
    with open('list.json', 'r') as data_file:
        fileArray = json.load(data_file)

    print(fileArray)

    for file_name in fileArray:
        print("Reading ", file_name)
        f = open(file_name, 'rU')
        raw = f.read()

    print("Read all")

if __name__ == "__main__":
    test()
