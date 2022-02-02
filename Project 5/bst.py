'Creates a Binary Search tree using a class'
class BST:
    'Creates a Binary Search Tree'

    def __init__(self, key = None):
        'Node Constructor'
        self.key = key
        self.count=1
        self.left = None
        self.right = None
        self.root = key

    def is_empty(self, node = None):
        'Returns True if empty, False otherwise'
        if node is None:
            return True
        return False

    def size(self, node = 'filler'):
        'Returns the number of items in the tree'
        if node is None:
            return 0
        elif node =='filler':
            node = self.root
            if node is None:
                return 0
            return self.size(node.left)+ 1 + self.size(node.right)
        else:
            return self.size(node.left)+ 1 + self.size(node.right)

    def height(self, node = 'filler'):
        '''Return the height of the tree,
        which is the length of the path from the root to its deepest leaf'''
        if node is None:
            return 0
        elif node =='filler':
            node = self.root
            if node is None:
                return 0
            left_depth = self.height(node.left)
            right_depth = self.height(node.right)
        else :
            # Find the depth of each subtree
            left_depth = self.height(node.left)
            right_depth = self.height(node.right)

            # Use larger tree
        if left_depth > right_depth:
            return left_depth+1
        else:
            return right_depth+1

    def add(self, node, key):
        'add item to its proper pace in the tree and returns the modified tree'
        #check
        if node is None:
            return BST(key)
        if key==node.key:
            node.count+=1
        #recur down the tree
        elif key < node.key:
            node.left = self.add(node.left, key)
        else:
            node.right = self.add(node.right, key)
        # return the node pointer
        return node

    def remove(self, key, root = 'filler'):
        'Removes Node from BST'
        from main import Pair
        if root == 'filler':
            root = self.root

        root_Pair = Pair(root.key, root.count)

        if root is None:
            return root

        # Recursive calls until find the node to be deleted
        if key.letter < root_Pair.letter:
            root.left = self.remove(key, root.left)
            return root

        elif key.letter > root_Pair.letter:
            root.right = self.remove(key, root.right)
            return root

        #leaf node
        if root.left is None and root.right is None:
            return None

        # If child is empty
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        #both children exist
        succ_parent = root

        # Find Successor
        succ = root.right

        while succ.left is not None:
            succ_parent = succ
            succ = succ.left

        # Delete successor If there is no succ, then assign succ->right to succ_parent->right
        if succ_parent != root:
            succ_parent.left = succ.right
        else:
            succ_parent.right = succ.right

        # Copy Successor Data to root
        root.key = succ.key
        return root

    def find(self, key, node = "filler"):
        'Returns the matched item, if the item isnt in tree raise a valueError'
        if node == 'filler':
            node = self.root
        if node is None:
            raise ValueError
        if key==node.key:
            return node
        #Recur down the tree
        elif key < node.key:
            return self.find(node.left, key)
        else:
            return self.find(node.right, key)

    def inorder(self,root = "filler"):
        'Returns list with the data items in order of inorder traversal'
        from main import Pair
        if root is None:
            return []

        if root == "filler":
            root = self.root

        left_list = self.inorder(root.left)
        right_list = self.inorder(root.right)
        return left_list + [Pair(root.key,root.count)] + right_list

    def preorder(self, root = "filler"):
        'Returns list with the data items in order of preorder traversal'
        from main import Pair
        if root is None:
            return []

        if root == "filler":
            root = self.root

        left_list = self.preorder(root.left)
        right_list = self.preorder(root.right)
        return [Pair(root.key,root.count)] +left_list + right_list

    def postorder(self, root = "filler"):
        'Returns list with the data items in order of postorder traversal'
        from main import Pair
        if root is None:
            return []

        if root == "filler":
            root = self.root

        left_list = self.postorder(root.left)
        right_list = self.postorder(root.right)
        return left_list + right_list + [Pair(root.key,root.count)]

    def rebalance(self):
        'Rebalances the BST'
        pass
        #I Couldn't get it to work and didn't want to worry
        #About pylint getting mad at me so I just commented everthing out 
        #
        # from main import Pair
        # nodes = self.inorder()
        # #nodes = []
        # print(nodes)

        # # for items in lyst:
        # #     nodes.append(items.letter)

        # n_length = len(nodes)

        # def rec_rebalance(nodes, start, end):
        #     #print(nodes)
        #     if start>end:
        #         return None

        #     mid = (start+end)//2

        #     node = nodes[mid]

        #     node.left = rec_rebalance(nodes, start, mid-1)
        #     node.right = rec_rebalance(nodes,mid+1,end)

        #     return node

        # root = rec_rebalance(nodes, 0,n_length-1)
        # return self.preorder(root)
        # #return rec_rebalance(nodes, 0,n-1)
