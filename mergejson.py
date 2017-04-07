import sys
import json
import os

def merge(file_name_array):
    merged = {}
    for filename in file_name_array:
        #for each file, open it into a dictionary called data
        with open(filename, 'r') as f:
            data = json.load(f)

            for key in data:
                if key in merged:

                    entries_to_add = data[key]
                    existing_entries = merged[key]

                    existing_verbs = []
                    for existing_entry in existing_entries:
                        existing_verb = existing_entry['verb']
                        existing_verbs.append(existing_verb)

                    for entry_to_add in entries_to_add:
                        verb_to_add = entry_to_add['verb']

                        #compare the verbs of the entries
                        if verb_to_add in existing_verbs:
                            #if the noun and verb combo has been found and needs to be updated
                            updated_freq = existing_entry['freq'] + entry_to_add['freq']
                            existing_entry['freq'] = updated_freq

                        else: #if noun has been found, but a verb has not been found yet
                            merged[key].append(entry_to_add)
                else: #if noun has not been found yet
                    merged[key]=data[key]

    return merged

def main():
    file_name_array = []
    #add files here
    file_name_array.append("mouse.json")
    file_name_array.append("moose.json")

    # file_name_array.append("textdatafolder/55.json")
    # file_name_array.append("textdatafolder/120.json")
    # file_name_array.append("textdatafolder/174.json")
    # file_name_array.append("textdatafolder/236.json")
    # file_name_array.append("textdatafolder/521.json")
    # file_name_array.append("textdatafolder/730.json")
    # file_name_array.append("textdatafolder/1661.json")
    # file_name_array.append("textdatafolder/2148.json")

    final_data = merge(file_name_array)

    with open('merged.json','w') as outfile:
        json.dump(final_data, outfile)

if __name__ == "__main__":
    main()
