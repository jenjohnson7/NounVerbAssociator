import json

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

    with open(toConvert, 'r') as data_file:
        myDict = json.load(data_file)

    for key in myDict:
        converted.append(newObject(key, myDict[key]))

    with open(toConvert, 'w') as outfile:
        json.dump(converted, outfile)

    print('Successfully converted ', toConvert, ' into db json file')

if __name__ == "__main__":
    print('please use as module')
