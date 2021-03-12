"""
Compare strings of hex and binary
"""
def digitToValue(letter):
    HEX = "0123456789ABCDEF"
    hexDic = {hex: i for i, hex in enumerate(HEX)}
    return hexDic[letter]


def convertBase(string: str, base: int) -> int:
    assert(not(base < 2))
    assert(not(base > 10 and base != 16))
    #if base < 2 or (base > 10 and base != 16): return -1
    result = 0
    for power, l in enumerate(reversed(string)):
        digit = digitToValue(l)
        if digit >= base or digit < 0: 
            return -1
        result += pow(base, power) * digit
    return result


def compare_bin_hex(bin, hex):
    bin_to_10 = convertBase(bin, 1)
    hex_to_10 = convertBase(hex, 16)
    if bin_to_10 == hex_to_10:
        print("Equal", "bin is", bin_to_10, "hex is", hex_to_10)
    else:
        print("False", "bin is", bin_to_10, "hex is", hex_to_10) 


if __name__ == "__main__":
    base2  = "1010"
    base16 = "5"
    compare_bin_hex(base2, base16)