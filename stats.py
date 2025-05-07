# function for counting words
def get_num_words(text):
    words = text.split()
    count = len(words)
    return count

# function for counting characters
def get_num_characters(text):
    # empty dictionary for storing the counts
    letter_nums = {}

    # loop through each character in the text and add or increment them    
    for character in text:
        character = character.lower()
        if character in letter_nums:
            letter_nums[character] += 1
        else:
            letter_nums[character] = 1
        
    return letter_nums


# function that sorts a dictionary
def chars_dict_to_sorted_list(char_dict):
    # empty list to store dictionaries
    chars_list = []

    # loop through dictionary to append each value pair to the list
    for char, count in char_dict.items():
        char_info = {"char": char, "num": count}
        chars_list.append(char_info)

    # function for returning the num value from a dictionary
    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
