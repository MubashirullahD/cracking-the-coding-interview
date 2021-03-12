"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you 
cannot use additional data structures? 
Hints: #44, #117, #132
What is a bit vector?
"""
string = "hello"

def is_unique1(string):
    """
    O(n^2) implementation
    """
    for i, letter in enumerate(string):
        for remaining_letter in string[i+1:]:
            if letter == remaining_letter:
                print(letter, "is repeated", remaining_letter)
                return
    print("string has all unique characters")

def is_unique2(string):
    """
    O(n)
    """
    from collections import defaultdict
    uniqueHash = defaultdict(int)
    for letter in string:
        if not uniqueHash[letter]:
            uniqueHash[letter] += 1
        else:
            print("String does not have all unique characters", letter)
            return
    print("All unique")

def is_unique3(string):
    """
    O(nlogn)
    """
    new_string = sorted(string)
    for letter, letter2 in zip(new_string, new_string[1:]):
        if letter == letter2:
            print("Not unique", letter)
            return
    print("Unique")

if __name__ == "__main__":
    is_unique1(string)
    is_unique2(string)
    is_unique3(string)
