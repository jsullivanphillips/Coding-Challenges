class Node:
    def __init__(self, val, next=None):
        self.val = val;
        self.next = next;

class LinkedList:
    def __init__(self, head):
        self.head = head
    def traverse(self):
        temp = self.head
        while(temp != None):
            print(temp.val)
            temp = temp.next
    def reverse_list(self):
        current_node = self.head
        prev_node = None
        while(current_node != None):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            self.head = prev_node
    def remove_nth_node(self, )

n1 = Node(0, Node(1, Node(6)))
l1 = LinkedList(n1)

#ll.traverse()
assert l1.head != None
assert n1.val == 0
assert n1.next.next.next == None

l1.reverse_list()
l1.traverse()

print()

n2 = Node(1, None)
l2 = LinkedList(n2)

l2.reverse_list()
l2.traverse()

print()

n3 = Node(2, Node(3, None))
l3 = LinkedList(n3)

l3.reverse_list()
l3.traverse()

print()
