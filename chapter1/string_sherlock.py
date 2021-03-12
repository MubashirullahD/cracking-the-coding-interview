def decrypt(string):
    start_index = 0
    end_index = len(string)-1

    while(True):
        if start_index >= end_index:
            return 0

        same_letter = string[start_index]
        if (same_letter == string[start_index] and same_letter == string[end_index]):
            start_index += 1
            end_index -= 1

            for l in string[start_index:end_index]:
                if same_letter== l:
                    start_index += 1
                else:
                    break
            
            for l in reversed(string[start_index:end_index+1]):
                if same_letter == l:
                    end_index -= 1
                else:
                    break
        
        else:
            break
    return len(string[start_index:end_index+1])

if __name__ == "__main__":
    print(decrypt("aaaaaaabcaaaaaa"))

