import matplotlib.pyplot as plt


# Function that reads the content of a file specified in the "file_path"
def read_file(file_path):
    # With the "with" statement, python opens a file which you can read, write or update
    # As soon as the program leaves the "with" block, the connection with the file closes.
    # This is very efficient for resource management.
    # 'r' stands for read mode
    with open(file_path, 'r') as file:
        # Read the content of the file and save it all as a string in the variable "content".
        # lower() function turns all uppercase characters into lowercase
        content = file.read().lower()
    return content


def get_letters_frequency(content: str):
    # python strings work as lists of characters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequency_dictionary = {}
    # for each letter in the string alphabet..
    for letter in alphabet:
        # Create a key-value pair in the dictionary where the key is the letter and value is the frequency
        # list.count(x) return the number of times that x appears in the list
        frequency_dictionary[letter] = content.count(letter)
    return frequency_dictionary


# This function sums the number of times each letter appears in multiple files and creates
# a new dictionary with these sums
# list_of_frequency_dictionaries is a list of dictionaries
# e.g. [{"key1_1": "value1_1", "key1_2": "value1_2"}, {"key2_1": "value2_1", "key2_2": "value2_2"}]
# a list with 2 dictionaries
def sum_frequency_dictionaries(list_of_frequency_dictionaries: list):
    combined_dictionary = {}

    # for each dictionary in the list of dictionaries...
    for frequency_dictionary in list_of_frequency_dictionaries:
        # This for loop iterates through the key-value pairs of the given dictionarya
        for key, value in frequency_dictionary.items():
            # If the key already exists in the keys of the combined dictionary
            # just add the value to the sum
            if key in combined_dictionary.keys():
                combined_dictionary[key] += value
            # else create the key in the dictionary and add its first value
            else:
                combined_dictionary[key] = value
    return combined_dictionary


# Main function that runs the program
def main():
    # Defining static string variables at the start of the program increases code readability
    # and development speed. Because if you need to make a change to one of these variables, you will only
    # change it once inside this file and not in multiple locations.
    path_to_files = "files/"
    bible_file_name = "bible.txt"
    world192_file_name = "world192.txt"
    # e_coli_file_name = "E.txt"

    # calling read_file function to read the content of the specified file into bible_file variable
    bible_file = read_file(path_to_files + bible_file_name)

    # calling get_letters_frequency to get all the frequencies of the letters inside the file
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
