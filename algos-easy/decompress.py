# Decompress

# Write a function, decompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an decompressed version of the string where each 'char' of a group 
# is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def decompress(s):
    
    new_string = ''
    multiplier = ''
    sub_string = ''
    
    for char in s:
        if char.isnumeric():
            multiplier+=char
        else:
            char.isalpha()
            sub_string= (char)*int(multiplier)
            new_string += sub_string
            multiplier = ''
            
    print(new_string)
            

# TEST CASES
decompress("2c3a1t") # -> 'ccaaat'
decompress("4s2b") # -> 'ssssbb'
decompress("2p1o5p") # -> 'ppoppppp'
decompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
decompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
