# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#


# palindrome challenge

# Enter string to test for palindrome or 'exit':

# same forward and backwards
# breaks with non-palindrome or exit
# removes any characters or spaces


def palindrome(teststr):
    if teststr == teststr[::-1]:
        return True
    return False

run = True

while(run):
    teststr = input("Enter string to test for palindrome or 'exit':")
    if teststr == "exit":
        run = False
        break

    teststr = teststr.lower()

    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x

    print("Palindrome test:", palindrome(newstr))

# print(palindrome("viper"))
# print(palindrome("racecar"))
