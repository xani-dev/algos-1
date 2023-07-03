# Decompress

# Write a function, decompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an decompressed version of the string where each 'char' of a group 
# is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def decompress(s):
    #Convert word to list, using Unpack Method(*)
    word_to_list = [*s]
    print(word_to_list)
    
    #Find Numbers in list and convert them to Integers
    for c in word_to_list: 
       if c.isdigit():
           repeat_by = (int(c))
        #    print(repeat_by)
       else:
           final_string = ''
           final_string = ''.join((final_string , (c*repeat_by)))
           print(final_string)
       
            




# TEST CASES
decompress("2c3a1t") # -> 'ccaaat'
# decompress("4s2b") # -> 'ssssbb'
# decompress("2p1o5p") # -> 'ppoppppp'
# decompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
# decompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
