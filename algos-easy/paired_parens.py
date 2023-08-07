# Paired Parentheses

# Write a function, paired_parens, that takes in a string as an argument. 
# The function should return a boolean indicating whether or not the string has well-formed parentheses.
# You may assume the string contains only alphabetic characters, '(', or ')'.


def paired_parens(string):
  count = 0
  for char in string:
    if char == '(':
      count += 1
    elif char == ')':
      count -= 1
    if count == -1:
      print(False)
      return
       
  
  if count == 0: print(True)
  else:  print(False)


  
 


# TEST CASES
paired_parens("(david)((abby))") # -> True
paired_parens("()rose(jeff") # -> False
paired_parens(")(") # -> False
paired_parens("()") # -> True
paired_parens("(((potato())))") # -> True
paired_parens("(())(water)()") # -> True
