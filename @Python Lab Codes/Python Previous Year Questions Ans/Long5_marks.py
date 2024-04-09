#(Ans Of 2.[A])
import random
import string

# Function to generate a random string of fixed length
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Generate a list of 10 random 5-character strings
random_strings = [random_string(5) for _ in range(10)]

# Print the list of random strings
print(random_strings)

# random_strings = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(10)]
# print(random_strings)


#(Ans Of 2.[B])
def string_lengths(strings):
    return [len(string) for string in strings]

# Example usage:
input_strings = ['apple', 'banana', 'orange', 'kiwi']
result = string_lengths(input_strings)
print(result)  # Output: [5, 6, 6, 4]


#(Ans Of 3.[A])
def extract_vowels(input_string):
    vowels = "aeiouAEIOU"  # Define the set of vowels
    result = "".join(char for char in input_string if char in vowels)
    return result

# Example usage:
input_str = "Hello, World!"
vowel_str = extract_vowels(input_str)
print(f"Vowels in '{input_str}': {vowel_str}")  # Output: "Vowels in 'Hello, World!': eoO"


#(Ans Of 3.[B])
def count_consonants(input_string):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'  # Define a string containing all consonants (both lowercase and uppercase)
    return sum(1 for char in input_string if char in consonants)

# Example usage:
input_string = "hello"
result = count_consonants(input_string)
print(result)  # Output: 3


#(Ans Of 4.[A])
import random
import string
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))
# Test cases
if __name__ == "__main__":
    # Test case 1: Generate a random 5-character string
    print(random_string(5))

    # Test case 2: Generate another random 5-character string
    print(random_string(5))

    # Test case 3: Generate a longer random string (e.g., 10 characters)
    print(random_string(10))

    # Test case 4: Generate an empty string (length = 0)
    print(random_string(0))
    
    
#(Ans Of 4.[B])
def string_lengths(strings):
    return [len(string) for string in strings]

if __name__ == "__main__":
    # Test case 1: Empty list
    assert string_lengths([]) == []
    # Test case 2: List with one string
    assert string_lengths(["apple"]) == [5]
    # Test case 3: List with multiple strings
    assert string_lengths(["banana", "orange", "kiwi"]) == [6, 6, 4]
    # Test case 4: List with an empty string
    assert string_lengths([""]) == [0]
    # Test case 5: List with mixed lengths
    assert string_lengths(["apple", "grape", ""]) == [5, 5, 0]
    print("All test cases passed!") 



