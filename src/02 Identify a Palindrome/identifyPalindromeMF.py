import re

def checkPalindrome(inString):
  foreward = ''.join(re.findall(r'[a-z]',inString.lower()))
  backward = foreward[::-1]
  return foreward == backward 

checkInput = input('enter a string:')
isPali = checkPalindrome(checkInput)
print(isPali)