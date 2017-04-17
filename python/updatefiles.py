import tokenizer_test
from createjson import insert_corpus_v1, insert_corpus_v2, insert_corpus_v3, insert_corpus_v4, insert_corpus_v5
import json

def merge_dictionaries(global_dict, single_text_dict):
    """ merges dictionaries directly instead of via re-reading them from a json file as in mergejson.py """

    for key in single_text_dict:
        if key in global_dict:

            entries_to_add = single_text_dict[key]
            existing_entries = global_dict[key]

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
                    global_dict[key].append(entry_to_add)
        else: #if noun has not been found yet
            global_dict[key]=single_text_dict[key]

    return global_dict

def update_data_version(text_files_array, version):

    global_dict = {}

    for text_file in text_files_array:
        filename = "textdatafolder/" + text_file
        corpus_sents = tokenizer_test.read_from_file(filename)

        single_text_dict = {}
        if version == 1:
            single_text_dict = insert_corpus_v1(single_text_dict, corpus_sents)
        elif version == 2:
            single_text_dict = insert_corpus_v2(single_text_dict, corpus_sents)
        elif version == 3:
            single_text_dict = insert_corpus_v3(single_text_dict, corpus_sents)
        elif version == 4:
            single_text_dict = insert_corpus_v4(single_text_dict, corpus_sents)
        else: #version ==5
            single_text_dict = insert_corpus_v5(single_text_dict, corpus_sents)

        global_dict = merge_dictionaries(global_dict, single_text_dict)

    file_string = "data" + str(version) + ".json"
    with open(file_string,'w') as outfile:
        json.dump(global_dict, outfile)

def main():

    #add here
    text_files_array = ["45.txt", "55.txt", "120.txt", "174.txt", "236.txt", "521.txt", "730.txt", "1661.txt", "2148.txt"]
    version = 5

    update_data_version(text_files_array, version)

if __name__ == "__main__":
    main()
