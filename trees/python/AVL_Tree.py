class AVLNode(object):
    def __init__(self, data, balanceFactor=0, left=None, right=None):
        self.data = data
        self.balance = balance
        self.left = left
        self.right = right

    def set_data(self, data):
        self.data = data

    def set_balance(self, balance):
        self.balance = balance

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


class AVLTree(object):
    def __init__(self, root):
        self.root = root

    def insert(self, data):
        [self.root,taller] = insertAVL(self.root, AVLNode(data,0))

    def insertAVL(self, root, new_node):
        if root == None:
            root = new_node #balance factor 0
            taller = True
        elif root.data < new_node.data:
            [root.left,taller] = insertAVL(root.left, new_node)
            if taller:
                if root.balance == 0:
                    root.balance = -1
                elif root.balance == 1:
                    root.balance = 0
                    taller = False
                else:
                    root = left_right_rotate(root)
                    taller = False
        else:
            [root.right,taller] = insertAVL(root.right, new_node)
            if taller:
                if root.balance == 0:
                    root.balance = 1
                elif root.balance == -1:
                    root.balance = 0
                    taller = False
                else:
                    root = right_left_rotate(root)
                    taller = False
            return [root,taller]
    
    def left_rotate(self, root):
        """
        Used when inbalance is Left-Left
        """
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root

    def right_rotate(self, root):
        """
        Used when inbalance is Right-Right
        """
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root

    def left_right_rotate(self, root):
        """
        Used when inbalance is Left-Right 
        (go left, then right)
        To fix, we do a RIGHT rotate, then LEFT rotate (Reversed)
        """
        X = root.left
        if X.balance == -1:
            root.balance = 0
            X.balance = 0
            root = left_rotate(root)
        else:
            #Do some conditional checks here.... what are the cases?
            Y = X.right
            X.balance = -1
            Y.balance = 0
            root.balance = 0
            root.left = right_rotate(X)
            root = left_rotate(root)
        return root

    def right_left_rotate(self, root):
        """
        Used when inbalance is Right-Left
        (go right, then left)
        To fix, we do a LEFT rotate, then RIGHT rotate (Reversed)
        """
        X = root.right
        if X.balance == 1:
            root.balance = 0
            X.balance = 0
            root = right_rotate(root)
        else:
            #Do some conditional checks here....
            Y = X.left
            Y.balance = 0
            root.balance = 0
            root.right = left_rotate(X)
            root = right_rotate(root)
        return root

    def delete(self, node):
        pass
