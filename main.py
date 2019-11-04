import matplotlib.pyplot as plt


def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().lower()
    return content


def get_letters_frequency(content: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequency_dictionary = {}
    for letter in alphabet:
        frequency_dictionary[letter] = content.count(letter)
    return frequency_dictionary


def sum_frequency_dictionaries(list_of_frequency_dictionaries: list):
    combined_dictionary = {}
    for frequency_dictionary in list_of_frequency_dictionaries:
        for key, value in frequency_dictionary.items():
            if key in combined_dictionary.keys():
                combined_dictionary[key] += value
            else:
                combined_dictionary[key] = value
    return combined_dictionary


def main():
    path_to_files = "files\\"
    bible_file_name = "bible.txt"
    world192_file_name = "world192.txt"
    # e_coli_file_name = "E.txt"
    bible_file = read_file(path_to_files + bible_file_name)
    bible_frequency = get_letters_frequency(bible_file)
    world192_file = read_file(path_to_files + world192_file_name)
    world192_frequency = get_letters_frequency(world192_file)
    # e_cole_file = read_file(e_coli_file_name)
    # e_cole_frequency = get_letters_frequency(e_cole_file)

    combined = sum_frequency_dictionaries([bible_frequency, world192_frequency])

    plt.bar(list(bible_frequency.keys()), list(bible_frequency.values()))
    plt.legend(['bible_text'])

    plt.show()
    plt.bar(list(world192_frequency.keys()),list(world192_frequency.values()), color='r')
    plt.legend(['world_text'])
    plt.show()

    plt.bar(list(bible_frequency.keys()), list(bible_frequency.values()))
    plt.bar(list(world192_frequency.keys()),list(world192_frequency.values()), color='r')
    plt.legend(['bible_text', 'world_text'])
    plt.show()

    plt.bar(combined.keys(), combined.values())
    plt.title("Combined results")
    plt.yticks()
    plt.show()


if __name__ == "__main__":
    main()
