class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None 
        self.right_child = None 
        
na = Node('A')
nb = Node('B')
nc = Node('C')
nd = Node('D')
ne = Node('E')
nf = Node('F')
ng = Node('G')
nh = Node('H')

na.left_child = nb
na.right_child = nc
nb.left_child = nd
nb.right_child = ne
nd.left_child = ng
nd.right_child = nh
nc.right_child = nf


def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)

def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)

def posorder(root_node):
    current = root_node
    if current is None:
        return
    posorder(current.left_child)
    posorder(current.right_child)
    print(current.data)

if __name__ == '__main__':
    posorder(na)