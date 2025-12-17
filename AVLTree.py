#id1:325047686
#name1:Yair Tilayov
#username1:tilayov
#id2:211381207
#name2:Shaked Baron
#username2:shakedbaron



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
    """Constructor, you are allowed to add more fields. 
    
    @type key: int
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """
    def is_real_node(self):
        return True


"""
A class implementing an AVL tree.
"""

class AVLTree(object):

    """
    Constructor, you are allowed to add more fields.
    """
    def __init__(self):
        self.root = None
        self.treeSize = 0 #every insert and finger insert, increase size by 1, and every delete decrease by 1
        self.maxNode = None #updates every insert / delete


    """searches for a node in the dictionary corresponding to the key (starting at the root)
        
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """
    def search(self, key):
        # Purpose: search for a node with `key` starting from root.
        # Complexity: O(h) where h is tree height (O(log n) on balanced AVL).
        node=self.root
        steps=0
        while node is not None:
            steps+=1
                
            if key==node.key:
                return node, steps+1
            elif key<node.key:
                node=node.left
            else:
                node=node.right

        return None,-1 #O(logn)


    """searches for a node in the dictionary corresponding to the key, starting at the max
        
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """
    def finger_search(self, key):
        # Purpose: finger (max-based) search for `key`.
        # Complexity: O(h) in worst case; O(log n) typically, plus traversal from max.
        #node=self.root
        #while node.right is not None:
        #    node=node.right
        #    steps+=1
        steps=0
        max_node=self.maxNode
        if key>max_node.key:
            return None , -1
        if key==max_node.key:
            return max_node, steps+1
        u=max_node
        while u.parent is not None and u.parent.key>=key:
            u=u.parent
            steps+=1
        current=u
        while current is not None:
            steps+=1

            if key==current.key:
                return current, steps
            if key< current.key:
                current=current.left 
            else:
                current=current.right
        return None, -1


    """inserts a new node into the dictionary with corresponding key and value (starting at the root)

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: (AVLNode,int,int)
    @returns: a 3-tuple (x,e,h) where x is the new node,
    e is the number of edges on the path between the starting node and new node before rebalancing,
    and h is the number of PROMOTE cases during the AVL rebalancing
    """
    #we add functions to support the prompting#
    def height(self, node):
        # Purpose: helper to get node height; virtual nodes have height -1.
        # Complexity: O(1).
        return node.height if node is not None else -1
    
    def update_height(self, node):
        # Purpose: recompute and set `node.height` from its children.
        # Complexity: O(1) since child heights are stored.
        node.height = 1+max(self.height(node.left),self.height(node.right))

    def balance_factor(self, node):
        # Purpose: compute balance factor = height(left) - height(right).
        # Complexity: O(1).
        return self.height(node.left)-self.height(node.right)
    
    def rotate_left(self,z):
        # Purpose: left-rotate around node `z` to restore AVL balance.
        # Complexity: O(1) (constant-time pointer changes and height updates).
        y=z.right
        T2=y.left
        y.left=z
        z.right=T2
        y.parent=z.parent
        z.parent=y
        if T2 is not None:
            T2.parent=z
        if y.parent is None:
            self.root=y
        else:
            if y.parent.left == z:
                y.parent.left=y
            else:
                y.parent.right=y
        self.update_height(z)
        self.update_height(y)

    def rotate_right(self,z):
        # Purpose: right-rotate around node `z` to restore AVL balance.
        # Complexity: O(1).
        y=z.left
        T3=y.right
        y.right=z
        z.left=T3
        y.parent=z.parent
        z.parent=y
        if T3 is not None:
            T3.parent=z
        if y.parent is None:
            self.root=y
        else:
            if y.parent.left == z:
                y.parent.left=y
            else:
                y.parent.right=y
        self.update_height(z)
        self.update_height(y)


    def balance_tree(self, node, is_insert=False):
        # Purpose: walk up from `node`, update heights and rebalance as needed.
        # Returns: number of promote (height increases) operations during rebalancing.
        # Complexity: O(h) where h is number of ancestors visited (O(log n) typically).
        promotes=0
        current=node
        while current is not None:
            old_h=current.height 
            self.update_height(current)
            bf=self.balance_factor(current)
            if current.height == old_h and -1<=bf<=1:
                break
            if current.height>old_h:
                promotes+=1
            if bf>1:
                if self.balance_factor(current.left)<=0:
                    self.rotate_left(current.left)
                self.rotate_right(current)
                if is_insert:
                    break
    
            elif bf<-1:
                if self.balance_factor(current.right)>=0:
                    self.rotate_right(current.right)
                self.rotate_left(current)
                if is_insert:
                    break
                
            current=current.parent
        return promotes


    def insert(self, key, val):
        # Purpose: insert a new key/value into the AVL tree (starting at root).
        # Returns: (new_node, edges_traversed_before_rebalance, promote_count).
        # Complexity: O(h) for search + O(h) for rebalancing -> O(h) total (O(log n) typically).
        self.treeSize+=1
        new_node=AVLNode(key,val)
        new_node.is_real_node = True
        if self.root is None:
            self.root = new_node
            self.maxNode = new_node
            return new_node, 0, 0
        if self.maxNode and key > self.maxNode.key:
            self.maxNode = new_node
        node=self.root 
        steps=0
        parent=None
        while node is not None:
            parent=node 
            steps+=1 
            if node.key>key:
                node=node.left 
            elif node.key<key:
                node=node.right 
        new_node.parent=parent
        if key<parent.key:
            parent.left=new_node
        else:
            parent.right=new_node
        promotes=self.balance_tree(new_node, is_insert=True)
        return new_node,steps,promotes #O(logn)



    """inserts a new node into the dictionary with corresponding key and value, starting at the max

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: (AVLNode,int,int)
    @returns: a 3-tuple (x,e,h) where x is the new node,
    e is the number of edges on the path between the starting node and new node before rebalancing,
    and h is the number of PROMOTE cases during the AVL rebalancing
    """
    def finger_insert(self, key, val):
        # Purpose: insert starting from maximum (finger insertion) to speed inserts near max.
        # Returns: (new_node, edges_traversed_before_rebalance, promote_count).
        # Complexity: O(h) worst-case; O(log n) typically, plus finger traversal.
        new_node=AVLNode(key,val)
        self.treeSize+=1
        steps = 0
        #node_max=self.root
        #while node_max.right is not None:
        #    node_max=node_max.right 
        #    steps+=1
        if self.root is None:
            self.root = new_node
            self.maxNode = new_node
            return new_node, 0, 0
        node_max = self.maxNode
        if node_max and key>node_max.key:
            node_max.right=new_node
            new_node.parent=node_max
            steps+=1
            promotes=self.balance_tree(node_max, is_insert=True)
            self.maxNode = new_node
            return new_node, steps,promotes
        current=node_max
        while current.parent is not None and current.parent.key>key:
            current=current.parent
            steps+=1
        parent=current
        while True:
            if key<parent.key:
                if parent.left is None:
                    parent.left=new_node
                    new_node.parent=parent
                    steps+=1
                    break
                parent=parent.left 
                steps+=1
            else:
                if parent.right is None:
                    parent.right=new_node
                    new_node.parent=parent
                    steps+=1
                    break
                parent=parent.right 
                steps+=1
        promotes=self.balance_tree(parent, is_insert=True)
        return new_node, steps, promotes
    
        


    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    """
    def successor(self,node): 
        # Purpose: find in-order successor of `node` in the BST.
        # Complexity: O(h) worst-case (follow right then left spine), typically O(log n).
        if node.right is not None:
            current=node.right
            while current.left is not None:
                current=current.left
            return current
        current=node
        parent=current.parent
        while parent is not None and current.key==parent.right.key:
            current=parent
            parent=parent.parent
        return parent


            
            
    def delete(self, node):
        # Purpose: delete given `node` from the AVL tree and rebalance.
        # Returns: number of promote operations during rebalancing (if any).
        # Complexity: O(h) for splice + O(h) for rebalancing -> O(h) total (O(log n) typically).
        self.treeSize-=1
        fix_from=node.parent
        if node.left is None and node.right is None:#עלה -ניתוק ישיר
            p=node.parent
            if p is not None:
                if p.left.key is node.key:
                    p.left=None
                else:
                    p.right=None
            return self.root
        if node.left is None or node.right is None: #ילד אחד אז מחברים אותו לסבא
            child=node.left if node.left is not None else node.right
            p=node.parent
            if p is not None:
                if p.left is node:
                    p.left=child
                else:
                    p.right=child
            child.parent=p
            #update max node
            if node.key == self.maxNode.key:
                self.maxNode = p
            return
        succ=self.successor(node) # 2 ילדים -מוצאים יורש ומחליפים 
        node.key , succ.key= succ.key, node.key
        node.value, succ.value= succ.value, node.value
        if succ.left is None and succ.right is None:
            p=succ.parent
            if p.left.key is succ.key:
                p.left=None
            else:
                p.right=None
        else:
            child=succ.left if succ.left is not None else succ.right
            p=succ.parent
            if p.left is succ:
                p.left=child
            else:
                p.right=child
            child.parent=p 
            fix_from=p
            promotes=0
            if fix_from is not None:
                promotes=self.balance_tree(fix_from)
            else:
                promotes=0
            return promotes
        #O(logn)


    """joins self with item and another AVLTree

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: the key separting self and tree2
    @type val: string
    @param val: the value corresponding to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
    or the opposite way
    """
    def join(self, tree2, key, val):
        # Height-aware in-place join. Assumes all keys in self < key < all keys in tree2,
        # or the opposite. Runs in O(|h1-h2|) time.

        if self.root is None and tree2.root is None:
            self.insert(key, val)

        # Handle self > key > tree2
        if (self.root is None and key > tree2.root.key) or (tree2.root is None and self.root.key > key) or (self.root is not None and tree2.root is not None and self.root.key > key > tree2.root.key):
            self.root, tree2.root = tree2.root, self.root
            self.treeSize, tree2.treeSize = tree2.treeSize, self.treeSize

        # Handle empty trees
        if self.root is None:
            self.root = tree2.root
            self.insert(key, val)
            #new_root = AVLNode(key, val)
            #new_root.left = None
            #new_root.right = tree2.root
            #if tree2.root is not None:
            #    tree2.root.parent = new_root
            #self.root = new_root
            #self.treeSize = 1 + tree2.treeSize
            #self.update_height(new_root)
            return
        if tree2.root is None:
            self.insert(key, val)
            #new_root = AVLNode(key, val)
            #new_root.right = None
            #new_root.left = self.root
            #if self.root is not None:
            #    self.root.parent = new_root
            #self.root = new_root
            #self.treeSize = 1 + self.treeSize
            #self.update_height(new_root)
            return

        h1 = self.height(self.root)
        h2 = self.height(tree2.root)
        middle = AVLNode(key, val)
        self.maxNode = tree2.maxNode
        # If heights equal or very close, make middle the root
        if abs(h1 - h2) <= 1:
            middle.left = self.root
            middle.right = tree2.root
            if self.root is not None:
                self.root.parent = middle
            if tree2.root is not None:
                tree2.root.parent = middle
            self.root = middle
            self.treeSize = self.treeSize + tree2.treeSize + 1
            self.update_height(middle)
            self.balance_tree(middle, is_insert=True)
            return

        # If self is taller, splice into self's right spine
        if h1 > h2:
            node = self.root
            while node is not None and self.height(node.right) > h2:
                node = node.right
            middle.left = node.right if node is not None else None
            if middle.left is not None:
                middle.left.parent = middle
            middle.right = tree2.root
            if middle.right is not None:
                middle.right.parent = middle
            node.right = middle
            middle.parent = node
            # update sizes and heights and rebalance upwards
            self.size = self.treeSize + tree2.treeSize + 1
            self.update_height(middle)
            self.balance_tree(middle)
            return

        # If tree2 is taller, symmetric splice into tree2 and set tree2.root as the resulting root
        # We'll attach into tree2 then set self.root to tree2.root
        node = tree2.root
        while node is not None and self.height(node.left) > h1:
            node = node.left
        middle.right = node.left if node is not None else None
        if middle.right is not None:
            middle.right.parent = middle
        middle.left = self.root
        if middle.left is not None:
            middle.left.parent = middle
        node.left = middle
        middle.parent = node
        # ensure resulting root is tree2.root if parent exists, else middle
        if tree2.root is not None and node is not None:
            self.root = tree2.root
        # update sizes and heights and rebalance upwards
        self.size = self.treeSize + tree2.treeSize + 1
        self.update_height(middle)
        self.balance_tree(middle)
        return



    """splits the dictionary at a given node

    @type node: AVLNode
    @pre: node is in self
    @param node: the node in the dictionary to be used for the split
    @rtype: (AVLTree, AVLTree)
    @returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """
    def split(self, node):
        #Purpose: Split an AVL tree into 2 AVL trees according to a certain node,
        #one with smaller keys then the node's key and one with bigger keys then the nodes key.
        #Returns: The smaller tree and the bigger tree.
        #Complexity: O(logn)
        small_tree = AVLTree()
        small_tree.root = node.left
        big_tree = AVLTree()
        big_tree.root = node.right
        small_trees = {}
        big_trees = {}
        tmp_node = node

        while tmp_node.key != self.root.key:
            parent = tmp_node.parent
            new_tree = AVLTree()
            if parent.right is not None and parent.right.key == tmp_node.key:
                new_tree.root = parent.left
                small_trees[parent] = new_tree
            if parent.left is not None and parent.left.key == tmp_node.key:
                new_tree.root = parent.right
                big_trees[parent] = new_tree
            tmp_node = parent
        for parent in small_trees:
            small_tree.join(small_trees[parent], parent.key, parent.value)
        for parent in big_trees:
            big_tree.join(big_trees[parent], parent.key, parent.value)
        return small_tree, big_tree


    
    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """
    def avl_to_array(self):
        #Purpose: Return an in-order list of the (key, value) pairs in the tree,
        #according to the keys' order.
        #Returns: A list of (key, value) tuples
        #Complexity: O(n)
        array = []
        def in_order(node):
            if node is None:
                return
            in_order(node.left)
            array.append((node.key, node.value))
            in_order(node.right)
        in_order(self.root)
        return array


    """returns the node with the maximal key in the dictionary

    @rtype: AVLNode
    @returns: the maximal node, None if the dictionary is empty
    """
    def max_node(self):
        #Purpose: Find the node with the biggest key in the tree, by going all the way to the right.
        #Returns: The node with the biggest key 
        #Complexity: O(logn)
        tmp_node = self.root
        if tmp_node == None:
            return None
        while tmp_node.right != None:
            tmp_node = tmp_node.right
        return tmp_node

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """
    def size(self):
        #Returns: The size of the tree.
        #Complexity: O(1)
        return self.treeSize


    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """
    def get_root(self):
        #Returns: The root of the tree.
        #Complexity: O(1)
        return self.root #O(1)
