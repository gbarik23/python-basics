# How to create a linked list from a given array

# Node class to represent each node in the linked list
class Node:
    def __init__(self, data):  # Constructor to initialize object attributes
        self.data = data       # Stores the node's value
        self.next = None       # Points to the next node (initially None)

# This function converts an array into a linked list
def arrayToLinkedList(arr):
    size = len(arr)
    if size == 0:  # If the array is empty, return an empty linked list
        return None

    head = Node(arr[0])    # Create the head node using the first array element
    current = head         # Current pointer starts at the head

    for i in range(1, size):
        current.next = Node(arr[i])  # Create and link each new node
        current = current.next       # Move current pointer to the new node

    return head  # Return the head node (start of the linked list)

# This function prints the linked list
def printLinkedList(head):
    current = head  # Start from the head node
    while current is not None:  # Traverse until the end of the list
        print(f"{current.data} -> ", end="")  # Print current node's data
        current = current.next  # Move to the next node
    print("None")  # Indicate the end of the list

# Entry point: only runs if script is executed directly
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]  # Given array

    head = arrayToLinkedList(arr)  # Convert array to linked list
    printLinkedList(head)          # Print the linked list