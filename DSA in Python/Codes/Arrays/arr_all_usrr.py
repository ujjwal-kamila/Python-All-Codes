# Array all operations 
import array as arr

# Function to display the array
def display_arr(array):
    print("The array is: ", end=' ')
    for element in array:
        print(element, end=' ')
    print("\n")

# Function to insert an element
def insert_element(array):
    print("\nInsertion Operations:")
    value = int(input("Enter the value to insert: "))
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at specific position")
    choice = int(input("Enter yours choice: "))
    
    if choice == 1:
        array.insert(0, value)
    elif choice == 2:
        array.append(value)
    elif choice == 3:
        pos = int(input("Enter the position: "))
        if 0 <= pos <= len(array):
            array.insert(pos, value)
        else:
            print("Invalid Position!")
    else:
        print("Invalid Choice! Please enter a valid choice (1-3)")

# Function to delete an element
def delete_element(array):
    print("\n Deletion Operations:")
    print("1. Delete from beginning")
    print("2. Delete from end")
    print("3. Delete from specific position")
    choice = int(input("Enter your choice: "))
    
    if len(array) == 0:
        print("Array is empty, cannot delete.")
        return
    
    if choice == 1:
        deleted_element = array.pop(0)
        print(f"Deleted element from the beginning: {deleted_element}")
    elif choice == 2:
        deleted_element = array.pop()
        print(f"Deleted element from the end: {deleted_element}")
    elif choice == 3:
        pos = int(input("Enter the position to delete from: "))
        if 0 <= pos < len(array):
            deleted_element = array.pop(pos)
            print(f"Deleted element from position {pos}: {deleted_element}")
        else:
            print("Invalid Position!")
    else:
        print("Invalid Choice! Please enter a valid choice (1-3)")

# Main Function
def main():
    my_arr = arr.array('i', [1, 2, 3, 4, 5])  # Creating an initial array
    while True:
        print("\nArray Operations Menu:")
        print("1. Display Array")
        print("2. Insert Element")
        print("3. Delete Element")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            display_arr(my_arr)
        elif choice == 2:
            insert_element(my_arr)
        elif choice == 3:
            delete_element(my_arr)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
