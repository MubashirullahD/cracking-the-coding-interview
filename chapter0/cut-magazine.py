"""
Example: A ransom note can be formed by cutting words out of a magazine to form a new 
sentence. How would you figure out if a ransom note (represented as a string) can be formed 
from a given magazine (string)?
"""
from collections import Counter

ransomNote = "Give us the money"
magazine = "Example: A ransom note can be formed by cutting words out of a magazine to form a new \
sentence. How would you figure out if a ransom note (represented as a string) can be formed \
from a given magazine (string)?"

magDict1 = Counter(magazine)
formable = True

for l in ransomNote:
    if not magDict1.get(l, 0):
        print("Can not be formed")
        print("Letter", l, "missing")
        formable = False
        break
    magDict1[l] -= 1

if formable:
    print("Can be formed")

