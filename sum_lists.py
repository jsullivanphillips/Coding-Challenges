# 1 -> 2 -> 3 -> 4 -> 5
# is the number 54321.

# given two lists in this format, return their sum

# 9 -> 9
# 5 -> 2
# return (99 + 25) so 124
# 4 -> 2 -> 1
# Data Structures
class List:
    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        temp = self.head
        if(temp == None):
            self.head = node
        else:
            while(temp.next != None):
                temp = temp.next
            temp.next = node

    def print_list(self):
        temp = self.head
        while (temp != None):
            print(str(temp.value), end='')
            if(temp.next != None):
                print(" -> ", end='')
            temp = temp.next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Coding Challenge
def create_num_list(num):
    num_str = str(num)
    num_list = List()
    for char in reversed(num_str):
        num_list.append(Node(int(char)))
    return num_list

def read_num_list(list):
    cur = list.head
    num = 0
    n = 0
    while (cur != None):
        num += cur.value * (10 ** n)
        n += 1
        cur = cur.next
    return num

def add_lists(list1, list2):
    num1 = read_num_list(list1)
    num2 = read_num_list(list2)
    return num1 + num2


# Main
num_list0 = create_num_list(99)
num_list1 = create_num_list(25)
num_list0.print_list()
print()
num_list1.print_list()
print()
print(add_lists(num_list0,num_list1))
