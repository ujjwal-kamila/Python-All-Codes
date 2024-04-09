import random
import string

random_strings = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(10)]
print(random_strings)
