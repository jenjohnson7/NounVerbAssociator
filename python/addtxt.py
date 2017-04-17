'''
Add text name to json file and makes sure that it's not already in it.
'''
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python addtxt.py <dir> <file1> <file2> ...')

    else:
        destination = sys.argv[1] + '/list.json'
        with open(destination, 'r') as data_file:
            myList = json.load(data_file)

        for i in range(2, len(sys.argv)):
            if sys.argv[i] not in myList:
                myList.append(sys.argv[i])

        with open(destination, 'w') as outfile:
            json.dump(myList, outfile)

        print('Completed successfully')
