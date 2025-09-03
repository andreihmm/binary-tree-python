from collections import deque 

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None 
        self.right_child = None 
        
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert_level_order(self, data):
        if not data:
            return None
        
        root = Node(data.popleft())
        q = deque([root])
        
        while data:
            node = q.popleft()
            
            if data:
                left_val = data.popleft()
                node.left_child = Node(left_val)
                q.append(node.left_child)
                
            if data:
                right_val = data.popleft()
                node.right_child = Node(right_val)
                q.append(node.right_child)
        
        return root
        
        
    ##################  funções de travessia  ##########################

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
        
    def levelorder(root):
        if root is None:
            return []
    
        # Create an empty queue for level order traversal
        q = []
        res = []
    
        # Enqueue Root
        q.append(root)
        curr_level = 0
    
        while q:
            len_q = len(q)
            res.append([])
    
            for _ in range(len_q):
                # Add front of queue and remove it from queue
                node = q.pop(0)
                res[curr_level].append(node.data)
    
                # Enqueue left child
                if node.left is not None:
                    q.append(node.left)
    
                # Enqueue right child
                if node.right is not None:
                    q.append(node.right)
            curr_level += 1
        return res

if __name__ == '__main__':
    ArvoreBinaria = BinaryTree()
    entrada = input("Digite os valores separados por espaço: ").strip()
    itens = deque(entrada.split())
    raiz = ArvoreBinaria.insert_level_order(itens)
    
    print("Valores inserido (BFS) ", levelorder(raiz))