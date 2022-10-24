# This problem was asked by Facebook.

# Write a function that rotates a list by k elements.
# For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
# Try solving this without creating a copy of the list. How many swap or move operations do you need?

class List:
    def __init__(self, head):
        self.head = head

    def append(self, node):
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = node

    def print_list(self):
        temp = self.head
        while (temp != None):
            print(temp.value)
            temp = temp.next
        print()

    #Coding challenge method
    def rotate_list(self, k):
        temp = self.head
        for i in range(0,k):
            self.append(Node(temp.value))
            temp = temp.next
        self.head = temp


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)


list = List(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(n5)

list.print_list()
list.rotate_list(2)
list.print_list()
