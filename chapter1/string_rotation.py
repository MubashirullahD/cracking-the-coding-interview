"""
String Rotation: Assume you have a method isSubstring which checks if one word is a substring 
of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one 
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). 
Hints: #34, #88, #104
"""
from collections import Counter
import re

def string_rotation(s1: str, s2: str)-> bool:
    """
    Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one 
    call to isSubstring.
    """
    # Find partition point
    # Find unique word that we can find partition on
    length_of_s1 = len(s1)
    # Check length cases
    mystr = s1[:length_of_s1//2]
    print(mystr)
    decrease_count = 0

    while(mystr):
        loc = s2.find(mystr)
        if loc == -1:
            decrease_count += 1
            mystr = s1[:length_of_s1//2-decrease_count]
            print(mystr)
        else:
            break
    if not mystr:
        print("mystr = ", mystr)
        return False
    rotated_s2 = s2[loc:] + s2[:loc]
    print(rotated_s2)
    if s1 == rotated_s2:
        return True
    else:
        return False

if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(string_rotation(s1,s2))

    
    
            


