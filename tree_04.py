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
        if not self.root:
            return False
        
        if not self.root.left_child and self.root.right_child:
            return True

        left_height = self.depth(self.root.left_child)
        right_height = self.depth(self.root.right_child)

        b_factor = abs(left_height - right_height)

        return (b_factor == 0)

    def is_complete(self):

        if not self.root:
            return False
        else:
            fila = [(self.root, 0)]
            indice = 0
            while fila:
                no, pos = fila.pop(0)
                if no is not None:
                    if pos != indice:
                        return False
                    fila.append((no.left_child, 2 * pos + 1))
                    fila.append((no.right_child, 2 * pos + 2))
                    indice += 1
            return True

    def is_regular(self, root):
        if not root:
            return False

        zero_or_two_children = (root.left_child is None) == (root.right_child is None)
        if root.right_child:
            zero_or_two_children = zero_or_two_children and self.is_regular(root.right_child)
        if root.left_child:
            zero_or_two_children = zero_or_two_children and self.is_regular(root.left_child)

        return zero_or_two_children

    def is_balanced(self):
        left_height = self.depth(self.root.left_child)
        right_height = self.depth(self.root.right_child)

        b_factor = abs(left_height - right_height)

        return b_factor < 2

    def is_unbalanced(self):
        return not self.is_balanced()


if __name__ == '__main__':
    ArvoreBinaria = BinaryTree()
    entrada = input("Digite os valores separados por espaço: ").strip()
    itens = deque(entrada.split())
    raiz = ArvoreBinaria.insert_level_order(itens)
    

    # print("\n\nNIVEL ORDEM")
    # print(ArvoreBinaria.levelorder())
    # print("\n\nPOS ORDEM")
    # ArvoreBinaria.posorder(raiz)
    # print("\n\nPRE ORDEM")
    # ArvoreBinaria.preorder(raiz)
    # print("\n\nEM ORDEM")
    # ArvoreBinaria.inorder(raiz)


    # if (ArvoreBinaria.is_perfect()):
    #     print("Perfeita")
    # else:
    #     print("man...")

    
    # if (ArvoreBinaria.is_complete()):
    #     print("Completa")
    # else:
    #     print("man...")

    
    # if (ArvoreBinaria.is_regular(ArvoreBinaria.root)):
    #     print("Regular")
    # else:
    #     print("man...")

    
    # if (ArvoreBinaria.is_balanced()):
    #     print("Balanceada")
    # else:
    #     print("man...")

    
    ABA = BinaryTree()
    ABA.root = Node(13)
    ABA.root.left_child = Node(9)
    ABA.root.left_child.left_child = Node(8)
    ABA.root.left_child.left_child.left_child = Node(2)
    ABA.root.right_child = Node(11)
    ABA.root.right_child.left_child = Node(10)
    ABA.root.right_child.right_child = Node(4)

    print("######### ARVORE A) #########")

    print("\n\nEM ORDEM")
    ABA.inorder(ABA.root)
    print("\n\nPOS ORDEM")
    ABA.posorder(ABA.root)
    print("\n\nPRE ORDEM")
    ABA.preorder(ABA.root)



    
    ABB = BinaryTree()
    ABB.root = Node(13)
    ABB.root.left_child = Node(9)
    ABB.root.left_child.left_child = Node(8)
    ABB.root.left_child.left_child.left_child = Node(2)
    ABB.root.right_child = Node(11)
    ABB.root.right_child.left_child = Node(10)
    ABB.root.right_child.right_child = Node(4)

    print("######### ARVORE B) #########")

    print("\n\nEM ORDEM")
    ABB.inorder(ABB.root)
    print("\n\nPOS ORDEM")
    ABB.posorder(ABB.root)
    print("\n\nPRE ORDEM")
    ABB.preorder(ABB.root)



    
    ABC = BinaryTree()
    ABC.root = Node(13)
    ABC.root.left_child = Node(9)
    ABC.root.left_child.left_child = Node(8)
    ABC.root.left_child.left_child.left_child = Node(2)
    ABC.root.right_child = Node(11)
    ABC.root.right_child.left_child = Node(10)
    ABC.root.right_child.right_child = Node(4)

    print("######### ARVORE C) #########")

    print("\n\nEM ORDEM")
    ABC.inorder(ABC.root)
    print("\n\nPOS ORDEM")
    ABC.posorder(ABC.root)
    print("\n\nPRE ORDEM")
    ABC.preorder(ABC.root)



    
    ABD = BinaryTree()
    ABD.root = Node(13)
    ABD.root.left_child = Node(9)
    ABD.root.left_child.left_child = Node(8)
    ABD.root.left_child.left_child.left_child = Node(2)
    ABD.root.right_child = Node(11)
    ABD.root.right_child.left_child = Node(10)
    ABD.root.right_child.right_child = Node(4)

    print("######### ARVORE D) #########")

    print("\n\nEM ORDEM")
    ABD.inorder(ABD.root)
    print("\n\nPOS ORDEM")
    ABD.posorder(ABD.root)
    print("\n\nPRE ORDEM")
    ABD.preorder(ABD.root)



