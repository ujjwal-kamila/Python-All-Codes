massage = "What do you like?"
response = 'spam'
print(massage)
print(response)
print(len(response))
print(response.upper())
print(massage.lower())
print(massage.capitalize())
print(massage + response)
print(5 * response)
print(massage[0])

def welcome():
    print("you are welcome")
#print(__name__) 
if __name__ == "__main__":    
    welcome()