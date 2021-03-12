"""
Example: Given a smaller string a and a bigger string b, design an algorithm to find all permutations 
of the shorter string within the longer one. Print the location of each permutation.
"""
from collections import Counter
sstring = 'abbc'
lstring = "cbabadcbbabbcbabaabccbabc" 

ssCounter = Counter(sstring)


for i in range(len((lstring))):
    tmpCounter = Counter()
    sub_lstring_of_size_sstring = lstring[i:i+len(sstring)]

    if len(sub_lstring_of_size_sstring) != len(sstring): 
        #print("reached the end with", sub_lstring_of_size_sstring)
        break
    
    for ll in sub_lstring_of_size_sstring:
        if ll in sstring:
            tmpCounter[ll] += 1
        else:
            break

    if not ssCounter - tmpCounter:
        print(sub_lstring_of_size_sstring, "location", i)

