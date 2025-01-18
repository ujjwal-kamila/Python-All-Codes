""" Singly Linked List Code """

# Node class to represent each element in the list
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

# Singly Linked List class 
class SLL:
    def __init__(self, start=None):
        self.start = start

    # Check if the linked list is empty
    def is_empty(self):
        return self.start is None

    # Insert a new node at the beginning of the list
    def insert_at_first(self, data):
        n = Node(data, self.start)  # Create a new node 
        self.start = n  #  new node -> new head 

    # Insert a new node at the end of the list
    def insert_at_last(self, data):
        n = Node(data, None)  # Create a new node with 'None' as the last node
        if not self.is_empty():  # If the list is not empty
            temp = self.start
            while temp.next is not None:  # Traverse to the last node
                temp = temp.next
            temp.next = n  #  last node point to the new node
        else:
            self.start = n  # If empty, the new node ->> head

    # Search for a node by its data
    def search(self, data):
        temp = self.start
        while temp is not None:  # Traverse through the list
            if temp.item == data:  # If the data is found
                return temp  # Return the node
            temp = temp.next
        return None  # Return None if not found

    # Insert a node after a specific node
    def insert_after(self, temp, data):
        if temp is not None:  # If the node exists
            n = Node(data, temp.next)  # Create a new node 
            temp.next = n  # Link given node to ->>new node

    # Print all elements in the list
    def print_list(self):
        temp = self.start
        while temp is not None:  #  print each node's data
            print(temp.item, end=' ')
            temp = temp.next
        print()

    # Delete the first node in the list
    def delete_first(self):
        if self.start is not None:  # If not empty
            self.start = self.start.next  # second node ->>>new head

    # Delete the last node in the list
    def delete_last(self):
        if self.start is None:
            return
        elif self.start.next is None:  # I one node,remove it
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:  # Traverse to the second-last node
                temp = temp.next
            temp.next = None  # Remove the reference to last node

    # Delete a node by its data
    def delete_item(self, data):
        if self.start is None:  # If the list is empty, do nothing
            return
        elif self.start.next is None:  # If the list has only one node
            if self.start.item == data:  # Check if the node to delete is the head
                self.start = None
        else:
            temp = self.start
            if temp.item == data:  # If the node to delete is the head
                self.start = temp.next  # Update head
            else:
                while temp.next is not None:  # Traverse to find the node
                    if temp.next.item == data:  # If the next node contains the data
                        temp.next = temp.next.next  # Bypass the node to be deleted
                        break
                    temp = temp.next

    # Make the list iterable
    def __iter__(self):
        return SLL_Iterator(self.start)

# Iterator class for the linked list
class SLL_Iterator:
    def __init__(self, start):
        self.current = start  

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current: 
            raise StopIteration
        data = self.current.item  
        self.current = self.current.next  
        return data

# Driver Code to test the operations
mylist = SLL()
mylist.insert_at_first(20)  # Insert 20 at the start
mylist.insert_at_first(500)  # Insert 10 at the start
mylist.insert_at_last(30)   # Insert 30 at the end
mylist.insert_after(mylist.search(20), 25)  # Insert 25 after the node with data 20

# Print the current list
mylist.print_list()  #  500 20 25 30

# Delete the node with value 30
mylist.delete_item(30)

# Print the updated list using the iterator
for x in mylist:
    print(x, end=' ')  #  500 20 25
print()
