input = "abccba"

def is_palindrome(string):    
    for index in range(len(string)):
        if string[index] != string[len(string) - index - 1]:
            return False
        return True

print(is_palindrome(input))