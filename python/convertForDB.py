'''
Converts old json file format to our desired mongo format
'''
import json

MYFILES = ['merged_v1.json', 'merged_v2.json', 'merged_v3.json', 'merged_v4.json', 'merged_v5.json']

def newObject(noun, verbArray):
    temp = {}
    temp['assoc'] = verbArray
    temp['noun'] = noun

    return temp

def convert(toConvert):
    '''
    Takes the name of a json file and converts its contents to our wanted mongoDB json format
    '''

    converted = []
    new_filename = "db-" + toConvert

    with open(toConvert, 'r') as data_file:
        myDict = json.load(data_file)

    print("Converting ", toConvert)
    for key in myDict:
        converted.append(newObject(key, myDict[key]))

    with open(new_filename, 'w') as outfile:
        json.dump(converted, outfile)

    print('Successfully converted ', toConvert, 'into db json file')

if __name__ == "__main__":

    for filename in MYFILES:
        convert(filename)
    print("Finished")
