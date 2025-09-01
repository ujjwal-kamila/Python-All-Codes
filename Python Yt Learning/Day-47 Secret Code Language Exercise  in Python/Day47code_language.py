# Day-47 Secret Code Language Exercise  in Python

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

st = input("Enter  your message : ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding : ")
coding = True if (coding=="1") else False
print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      r1 = "dsf"
      r2 = "jkr"
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

#for decoding
else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1] 
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))


# # Same ans using Function ->
# # Function to translate a message into secret code language based on specific rules
# # Rules:
# # - For words with 3 or more characters: Remove the first letter, append it at the end, and add three random characters at the start and end
# # - For words with less than 3 characters: Simply reverse the string
# def secret_code_translation(st, coding):
#     # Split the input message into words
#     words = st.split(" ")
    
#     # Check if encoding or decoding is requested
#     if coding:
#         nwords = []
#         # Encoding process
#         for word in words:
#             if len(word) >= 3:
#                 # Generate random characters for encoding
#                 r1 = "dsf"
#                 r2 = "jkr"
#                 # Apply encoding rules for words with 3 or more characters
#                 stnew = r1 + word[1:] + word[0] + r2
#                 nwords.append(stnew)
#             else:
#                 # For words with less than 3 characters, reverse the word
#                 nwords.append(word[::-1])
#         print(" ".join(nwords))
#     else:
#         # Decoding process
#         nwords = []
#         for word in words:
#             if len(word) >= 3:
#                 # Apply decoding rules for words with 3 or more characters
#                 stnew = word[3:-3]
#                 stnew = stnew[-1] + stnew[:-1]
#                 nwords.append(stnew)
#             else:
#                 # For words with less than 3 characters, reverse the word
#                 nwords.append(word[::-1])
#         print(" ".join(nwords))

# # Get user input for the message and whether to encode or decode
# st = input("Enter your message: ")
# coding = input("1 for Coding or 0 for Decoding: ")
# # Convert input to boolean for encoding or decoding
# coding = True if (coding == "1") else False

# # Call the function for secret code translation based on user input
# secret_code_translation(st, coding)

