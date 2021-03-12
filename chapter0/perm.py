"""
Example: Design an algorithm to print all permutations of a string. 
For simplicity, assume all characters are unique.
abcd
abdc
acbd
acdb
adbc
adcb

"""
def fac(iteration):
    if iteration <= 1:
        return 1
    else:
        return iteration * fac(iteration-1)


def perm(remainder, parsed):

    if not remainder:
        print(parsed)
        return

    for letter in remainder:
        newRemainder = "".join(l for l in remainder if l != letter)
        perm(newRemainder, parsed+letter)


if __name__ == "__main__":
    string = "abcd"
    perm(string, "")







