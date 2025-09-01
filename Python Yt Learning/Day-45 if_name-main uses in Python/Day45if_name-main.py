#Day-45 if_name-main uses in Python
# create ujjwal.py and call welcome fun
import ujjwal

ujjwal.welcome()


#the function contains code that should be run when the script run directly

# def main():
#     # Code to be run when the script is run directly
#     print("Running script directly")

# if __name__ == "__main__":
#     main()

#If you import it as a module into another script and call the main function from the imported module, it will not output anything
'''
def main():
    print("Running script directly")
if __name__ == "__main__":
    main()'''