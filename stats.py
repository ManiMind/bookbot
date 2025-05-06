def get_num_words(text):
    words = text.split()
    count = len(words)
    return count

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