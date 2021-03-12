"""
String Compression: Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the 
"compressed" string would not become smaller than the original string, your method should return 
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
Hints: #92, # 110
"""
def compress(string):
    index = 0
    compressed_string = []
    while(index < len(string)):
        count = 1
        letter = string[index]
        compressed_string.append(letter)
        index += 1
        for l in string[index:]:
            if letter == l:
                count += 1
                index += 1
            else:
                break
        compressed_string.append(str(count))
    return "".join(compressed_string)

if __name__ == "__main__":
    print(compress("aabcccccaaa"))
        
        

        