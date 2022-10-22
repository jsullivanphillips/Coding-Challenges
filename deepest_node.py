class Node:
    def __init__(self, v, parent=None, height = 0):
        self.parent = parent
        self.left = None
        self.right = None
        self.v = v
        self.height = height

class BinaryTree:
    def __init__(self, node):
        self.height = 0
        self.root = node

    def insert(self, parent_node, insert_node, curr_height):
        # Left side, less than
        if(insert_node.v < parent_node.v):
            if(parent_node.left != None):
                self.insert(parent_node.left, insert_node, curr_height + 1)
            else:
                parent_node.left = insert_node
                insert_node.parent = parent_node
                insert_node.height = curr_height
                if(curr_height > self.height):
                    self.height = curr_height
                return
        # Right side, Greater than
        elif(insert_node.v > parent_node.v):
            if(parent_node.right != None):
                self.insert(parent_node.right, insert_node, curr_height + 1)
            else:
                parent_node.right = insert_node
                insert_node.parent = parent_node
                insert_node.height = curr_height
                if(curr_height > self.height):
                    self.height = curr_height
                return
        # Equal to
        else:
            return

    def lowest_node(self, node):
        if(node != None):
            if(node.height == self.height):
                print(node.v)
            self.lowest_node(node.left)
            self.lowest_node(node.right)

#    def lowest_node(self):
node1 = Node(10)
node2 = Node(7)
node3 = Node(15)
node4 = Node(5)
node5 = Node(3)
node6 = Node(1)


tree = BinaryTree(node1)
tree.insert(tree.root, node2, 1)
tree.insert(tree.root, node3, 1)
tree.insert(tree.root, node4, 1)
tree.insert(tree.root, node5, 1)
tree.insert(tree.root, node6, 1)

print(tree.height)
tree.lowest_node(tree.root)
