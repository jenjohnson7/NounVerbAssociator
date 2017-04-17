import sys
import json
import string
import createjson
import convertForDB


if __name__ == '__main__':
    if not len(sys.argv) == 4:
        print("Usage: python associate.py 'directory of text files' 'name of new json file' 'version#'")

    else:
        version = int(sys.argv[3])

        with open(sys.argv[1] + '/list.json', 'r') as data_file:
            fileArray = json.load(data_file)

        print(fileArray)

        if (version) == 0: #if 0 given, do all versions
            for i in range(1, 6):
                target = sys.argv[2] + str(i) + '.json' # name#.json
                createjson.create_json(sys.argv[1], fileArray, target, i)
                convertForDB.convert(sys.argv[1] + '/'+ target)

        else:
            target = sys.argv[2] + sys.argv[3] + '.json'
            createjson.create_json(sys.argv[1], fileArray, target, version)
            convertForDB.convert(sys.argv[1] + '/'+ target)
