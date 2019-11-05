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



def letter_Fi(overall: int, content:str):
    overall_frequency = {}
    for key,value in content.items():
        overall_frequency[key] = (value / overall)*100
    return overall_frequency

def main():
    path_to_files = "files\\"
    bible_file_name = "bible.txt"
    world192_file_name = "world192.txt"
    #e_coli_file_name = "E.txt"
    bible_file = read_file(path_to_files + bible_file_name)
    bible_frequency = get_letters_frequency(bible_file)
    world192_file = read_file(path_to_files + world192_file_name)
    world192_frequency = get_letters_frequency(world192_file)
    #e_cole_file = read_file(e_coli_file_name)
    #e_cole_frequency = get_letters_frequency(e_cole_file)
        
    bible_overall = sum(bible_frequency.values())
  
    world_overall = sum(world192_frequency.values())
    
    bible_Fi = letter_Fi(bible_overall , bible_frequency)
    
    world_Fi = letter_Fi(world_overall , bible_frequency)
    
    combined = sum_frequency_dictionaries([bible_frequency, world192_frequency])
    
    combined_overall = bible_overall+world_overall
    
    combined_Fi = letter_Fi(combined_overall, combined)
    
    #create wiki's dictionary
    wiki_frequency =[ 8.16 , 1.49, 2.78, 4.25, 12.7, 2.22, 2.01, 6.09, 6.96, 0.15, 0.77,4.02,2.4,6.74,7.5,1.92,0.09,5.98,6.32,9.05,2.75,0.97,2.36,0.15,1.97,0.07]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    wiki_letter_frequency={}
    i=0
    for letter, in alphabet:
        wiki_letter_frequency[letter] = wiki_frequency[i]
        i +=1
        
        
    f,(ax1,ax2) = plt.subplots(1,2,sharey = 'row', figsize = [10,5])
    ax1.bar(list(bible_frequency.keys()), list(bible_frequency.values()))
    ax1.set_title("Bible")
    ax2.bar(list(world192_frequency.keys()),list(world192_frequency.values()), color='r')
    ax2.set_title("World")
    
    f,(ax1,ax2) = plt.subplots(1,2,sharey = 'col', figsize = [10,5])
    ax1.bar(list(bible_Fi.keys()), list(bible_Fi.values()))
    ax1.set_title("Bible")
    ax2.bar(list(world_Fi.keys()),list(world_Fi.values()), color='r')
    ax2.set_title("World")
    
    f,axs = plt.subplots(2,2, sharey = 'col' , figsize =[15,10])
    
    axs[0,0].bar(list(alphabet), list(bible_Fi.values()))
    axs[0,0].set_title("Bible")
    
    axs[0,1].bar(list(alphabet),list(world_Fi.values()), color='r')
    axs[0,1].set_title("World")
    
    axs[1,0].bar(list(alphabet), list(combined_Fi.values()), color= 'g')
    axs[1,0].set_title("Combined")
    
    axs[1,1].bar(list(alphabet),list(wiki_letter_frequency.values()), color='gray')
    axs[1,1].set_title("WIKI's")
    
    
    


if __name__ == "__main__":
    main()
    