"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the 
other.
"""
from collections import Counter

def check_perm1(string1, string2):
    if len(string1) != len(string2):
        print("Not a permutation, length are different")
        return

    perm1 = Counter(string1)
    for letter in string2:
        if letter in perm1.keys():
            perm1[letter] -= 1
        else:
            print("Not a permutation")
            return
    
    for value in perm1.values():
        if value:
            print("Not a permutation", perm1)
    
    print(string1, "is a permutation of", string2)

def check_perm2(string1, string2):
    tmp1 = sorted(string1)
    tmp2 = sorted(string2)

    if tmp1 == tmp2:
        print(string1, "is a permutation of", string2)
    else:
        print("Not a permutation")

if __name__ == "__main__":
    string1 = "apple"
    string2 = "peapl3"
    check_perm1(string1, string2)
    check_perm2(string1, string2)





    