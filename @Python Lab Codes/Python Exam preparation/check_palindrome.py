def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])


# Test the function
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
