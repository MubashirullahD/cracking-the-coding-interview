"""
URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string 
has sufficient space at the end to hold the additional characters, and that you are given the "true" 
length of the string. (Note: If implementing in Java, please use a character array so that you can 
perform this operation in place.) 
EXAMPLE 
Input: "Mr John Smith     ", 13 
Output: "Mr%20John%20Smith"

HINT at the bottom.
"""
 
def URLify(string):
    listified = [s for s in string.split()]
    print(listified)
    print("%20".join(listified))

def URLify2(string):
    tmp = string.strip().replace(" ", "%20",)
    print(tmp)


if __name__ == "__main__":
    string = "Mr John Smith     "
    URLify(string)
    URLify2(string)
    


# It's often easiest to modify strings by going from the end of the string to the beginning.
# You might find you need to know the number of spaces. Can you just count them?