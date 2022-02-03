# given a string(s), consisting of all lowercase English letters:
# find and return the first instance of a non-repeating character
# if no such char exists return '_'

def first_non_repeating(s):
    # dictionarywith letters from s as keys and number of times they occur as values
    char_dict = {}
    for char in s:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    # loop through s
    for char in s:
        if char_dict[char] == 1:
            return char
        # else the char has more than 1 occurence
        else:
            continue

    return '_'

print(first_non_repeating("abacabad")) # 'c'
print(first_non_repeating("abacabaabacaba")) # '_'
