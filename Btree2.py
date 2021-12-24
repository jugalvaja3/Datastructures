class Node:
    def __init__(self, data, parent):
        self.data=data
        self.parent=parent
        self.left=None
        self.right=None

class BTree:
    def __init__(self):
        self.root=None
        self.no_of_nodes=0
    def insert(self, data):
        if not self.root:
            self.root=Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data<node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left=Node(data, node)
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right=Node(data, node)

    def traversal(self):
        if self.root:
            self.t(self.root)

    def t(self, node):
        if node.left:
            self.t(node.left)
        print(node.data)
        if node.right:
            self.t(node.right)

    def rem(self, data):
        if self.root:
            self.rm(data, self.root)

    def rm(self, data, node):
        if data<node.data:
            if node.left:
                self.rm(data, node.left)
            else:
                print("No value")
        elif data>node.data:
            if node.right:
                self.rm(data, node.right)
            else:
                print("No value")
        else:
            if node.left is None and node.right is None:
                print("Removing a leaf node...😉")
                p=node.parent
                if p is None:
                    self.root=None
                elif p is not None and p.left==node:
                    p.left=None
                elif p is not None and p.right==node:
                    p.right=None
                del node
            elif node.left is None and node.right is not None:
                print("Removing  a node with 1 right child ")
                p=node.parent
                if p is None:
                    self.root=node.right
                else:
                    if p.left==node:
                        p.left=node.right
                    elif p.right==node:
                        p.right=node.right
                node.right.parent=p
                del node
            elif node.right is None and node.left is not None:
                print("Removing a node with 1 left child  ")
                if p is None:
                    self.root=node.left
                else:
                    if p.left==node:
                        p.left=node.left
                    elif p.right==node:
                        p.right=node.left
                node.left.parent=p
                del node
            else:
                print("Removing a node with 2 children...!")
                predecessor=self.get_p(node.left)
                temp=predecessor.data
                predecessor.data=node.data
                node.data=temp
                self.rm(data, predecessor)


    def get_p(self, node):
        if node.right:
            return self.get_p(node.right)
        return node

class comparator:
    def cp(self, node1, node2):
        if not node1 or not node2:
            return node2==node1
        if node1.data!=node2.data:
            return False
        return (self.cp(node1.left, node2.left) and self.cp(node1.right, node2.right))


bst1=BTree()
bst1.insert(6)
bst1.insert(4)
bst1.insert(10)

bst2=BTree()
bst2.insert(10)
bst2.insert(4)
bst2.insert(6)
c=comparator()
print(c.cp(bst1.root, bst2.root))































