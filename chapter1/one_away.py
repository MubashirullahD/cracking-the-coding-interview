"""
One Away: There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if they are 
one edit (or zero edits) away. 
EXAMPLE 
pale, ple -> true 
pales. pale -> true 
pale. bale -> true 
pale. bake -> false 
Hints: #23, #97, #130
"""

def one_away(string1, string2):
    count = 0
    remaining_index = 0
    place_holder = dict()
    
    for letter1, letter2 in zip(string1, string2):
        remaining_index += 1
        place_holder[letter1] = True
        place_holder[letter2] = not place_holder[letter1]

    if len(string1) > len(string2):
        for remaining_letter in string1[remaining_index:]:
            place_holder[remaining_letter] = True
    elif(len(string1) > len(string2)):
        for remaining_letter in string2[remaining_index:]:
            place_holder[remaining_letter] = True
    
    for truthy in place_holder.values():
        if truthy:
            count += 1
    
    return True if count <= 1 else False

if __name__ == "__main__":
    word1, word2 = "pale", "bake"#"pale", "bale"#"pales", "pale" #"pale", "ple"
    print(one_away(word1, word2))


