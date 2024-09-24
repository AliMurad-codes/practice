def ispalindrome(str):
    startindex = 0
    endindex = len(str) -1

    for x in range(len(str)):
        if str[startindex] != str[endindex]:
            return False
    return True

print(ispalindrome('rececar'))


