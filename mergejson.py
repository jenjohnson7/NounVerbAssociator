import sys
import json

def merge(file_name_array):
    merged = {}
    for filename in file_name_array:
        #for each file, open it into a dictionary called data
        with open(filename, 'r') as f:
            data = json.load(f)

            for key in data:
                if key in merged:

                    #get the entries

                    verbs_to_add = data[key]
                    existing_verbs = merged[key]

                    for entry_to_add in verbs_to_add:
                        verb_to_add = entry_to_add['verb']
                        for existing_entry in existing_verbs:
                            existing_verb = existing_entry['verb']

                            #compare the verbs of the entries
                            if verb_to_add == existing_verb:
                                #if the noun and verb combo has been found and needs to be updated
                                updated_freq = existing_entry['freq'] + entry_to_add['freq']
                                existing_entry['freq'] = updated_freq
                                break

                            else: #if noun has been found, but a verb has not been found yet
                                merged[key].append(entry_to_add)
                                break
                else: #if noun has not been found yet
                    merged[key]=data[key]

    return merged

def main():
    file_name_array = []
    file_name_array.append("55.json")
    file_name_array.append("120.json")
    file_name_array.append("174.json")
    file_name_array.append("236.json")
    file_name_array.append("521.json")
    file_name_array.append("730.json")
    file_name_array.append("1661.json")
    file_name_array.append("2148.json")
    #add files here
    final_data = merge(file_name_array)

    with open('merged.json','w') as outfile:
        json.dump(final_data, outfile)

if __name__ == "__main__":
    main()
