"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement 
of letters. The palindrome does not need to be limited to just dictionary words. 
EXAMPLE 
Input: Tact Coa 
Output: True (permutations: "tacocat". "atcocta". etc.)

Q How to separate keys and values from a dictionary
"""
# tt, aa, cc, o
# a
# aa, not ba
# opo, not oop
# baab, abba, not baba
# aaabbbaaa
from collections import Counter

def _make_palindrome(building_blocks:Counter)->(bool, str):
    """
    Given a Counter (type of dictionary), see if you can make a palindrome out of it.
    """
    number_of_values = sum([v for v in building_blocks.values()])
    place_holder = [''] * number_of_values
    

    mid_point = number_of_values // 2
    index_start = 0
    index_end = number_of_values-1

    while(mid_point):
        mid_point -= 1

        delete = []
        for k,v in building_blocks.items():
            
            #print("placeholder before", place_holder)
            #print("building blocks", building_blocks.items())

            if v >= 2:
                place_holder[index_start] = k
                place_holder[index_end] = k
                index_start +=1
                index_end -= 1
                building_blocks[k] -= 2

            #print("placeholder after", place_holder)
            #print("building blocks", building_blocks.items())

            if building_blocks[k] == 0:
                #print('delete this key', k)
                delete.append(k)
        for k in delete:
            del building_blocks[k]
            
    #print("start index", index_start)
    #print("end index", index_end)
    #print("len of building_blocks", len(building_blocks.keys()))
    #print("delete", delete)

    if (index_end == index_start) and len(building_blocks.keys()) == 1:
        for k, v in building_blocks.items():
            place_holder[index_start] = k
        return (True, "".join(place_holder))
    elif (index_end != index_start) and len(building_blocks.keys()) == 0:
        return(True, "".join(place_holder))
    else:
        return(False, "".join(place_holder))

def check_palindrome(string: str) -> bool:
    for forward, backward in zip(string, string[::-1]):
        if forward != backward:
            print("False, check palindrome failed")
            return False
    print("True, check palindrome passed")
    return True

def _make_permutation(string: str) -> list:
    """
    Take a string palindrome and find other palindrome permutations
    """
    perm_list = set()
    def _perm(remainder, parsed):

        if not remainder:
            perm_list.add(parsed)
            return

        for i, letter in enumerate(remainder):
            newRemainder = "".join(l for k, l in enumerate(remainder) if k != i)
            _perm(newRemainder, parsed+letter)

    mid_point = len(string)//2
    half_string = string[:mid_point]
    _perm(half_string, "")
    
    return [half_perm + string[mid_point] + (half_perm[::-1]) for half_perm in perm_list]

def palindrome_perm(string: str) -> (bool, []):
    """
    Given a string, check if it is a palindrome or not
    """
    word_frequency = Counter(string)
    made_palindrome, palindrome = _make_palindrome(word_frequency)
    print("Palindrome as returned by make_palindrome", palindrome, made_palindrome)
    if not made_palindrome:
        print("String not a permutation of a palindrome")
        return (False, [])
    elif check_palindrome(palindrome):
        print("String permuation of a palindrome")
        return(True, _make_permutation(palindrome))



if __name__ == "__main__":
    word = "aaabbbaaa"
    print(word)
    print(palindrome_perm(word))

