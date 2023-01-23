def checkPalindrome(inString):
    inString = inString.replace(" ","")
    inString = inString.replace("-", "")
    inString = inString.lower()
    revString = inString[::-1]
    if inString == revString:
        return True
    else:
        return False

checkInput = input('enter a string:')
isPali = checkPalindrome(checkInput)
print(isPali)