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
        self.root = root
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
        
    
    ##################  função auxiliar       ##########################

    def depth(self, root_node):
        if root_node is None:
            return 0
        return 1 + max(self.depth(root_node.left_child), self.depth(root_node.right_child))
    
    ##################  funções de travessia  ##########################

    def preorder(self, root_node):
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)
    
    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)
    
    def posorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.posorder(current.left_child)
        self.posorder(current.right_child)
        print(current.data)
        
    def levelorder(self):
        if self.root is None:
            return []
    
        # Create an empty queue for level order traversal
        q = []
        res = []
    
        # Enqueue Root
        q.append(self.root)
        curr_level = 0
    
        while q:
            len_q = len(q)
            res.append([])
    
            for _ in range(len_q):
                # Add front of queue and remove it from queue
                node = q.pop(0)
                res[curr_level].append(node.data)
    
                # Enqueue left child
                if node.left_child is not None:
                    q.append(node.left_child)
    
                # Enqueue right child
                if node.right_child is not None:
                    q.append(node.right_child)
            curr_level += 1
        return res

    ##################  funções de classificação  #####################

    def is_perfect(self):
        return

    def is_complete(self):
        return

    def is_regular(self):
        return

    def is_balanced(self):
        return

    def is_unbalanced(self):
        return


if __name__ == '__main__':
    ArvoreBinaria = BinaryTree()
    entrada = input("Digite os valores separados por espaço: ").strip()
    itens = deque(entrada.split())
    raiz = ArvoreBinaria.insert_level_order(itens)
    

    print("\n\nNIVEL ORDEM")
    print(ArvoreBinaria.levelorder())
    print("\n\nPOS ORDEM")
    ArvoreBinaria.posorder(raiz)
    print("\n\nPRE ORDEM")
    ArvoreBinaria.preorder(raiz)
    print("\n\nEM ORDEM")
    ArvoreBinaria.inorder(raiz)
    