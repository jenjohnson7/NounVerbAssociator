import json

def read_verbs(file):
    words = set()
    for line in file:
        word = line.strip()
        words.add(word)
    return words

def read_nouns(file):
    words = []
    for line in file:
        word = line.strip()
        words.append(word)
    return words

def read_file(version):
    file_name = "data" + str(version) + ".json"
    #with open(file_name, 'r') as f:
    with open("defaultbrownv1.json", 'r') as f:
        data = json.load(f)
    return data

def main():
    f = open("textdatafolder/1000commonverbs.txt", "r")
    g = open("textdatafolder/1500commonnouns.txt", "r")

    common_verbs = read_verbs(f)
    common_nouns = read_nouns(g)

    #change here
    version = 5

    data = read_file(version)

    proportion_of_common_verbs = []

    for noun in common_nouns:
        if noun in data:
            output_list = data[noun]
            output_verbs = set()
            for entry in output_list:
                verb = entry['verb']
                output_verbs.add(verb)
            overlap = output_verbs.intersection(common_verbs)

            verbs_in_common = len(overlap)
            verbs_for_this_noun = len(output_list)
            proportion = verbs_in_common/verbs_for_this_noun
            proportion_of_common_verbs.append(proportion)

    average_proportion = sum(proportion_of_common_verbs) / len(proportion_of_common_verbs)
    print(average_proportion)

if __name__ == "__main__":
  main()
