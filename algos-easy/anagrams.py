# Anagrams

# Write a function, anagrams, that takes in two strings as arguments.
# The function should return a boolean indicating whether or not the strings are anagrams.
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
    # Check lenght and equality of lists
    if len(s1) != len(s2):
        print(False)
    else:
      print(sorted(s1) == sorted(s2))


# TEST CASES
anagrams('restful', 'fluster')  # -> True
anagrams('cats', 'tocs') # -> False
anagrams('monkeyswrite', 'newyorktimes') # -> True
anagrams('paper', 'reapa') # -> False
anagrams('elbow', 'below') # -> True
anagrams('tax', 'taxi') # -> False
anagrams('taxi', 'tax') # -> False
anagrams('night', 'thing') # -> True
anagrams('po', 'popp') # -> False
anagrams('pp', 'oo') # -> False
