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
		self.height = -1
		

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return False


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


	"""searches for a node in the dictionary corresponding to the key (starting at the root)
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def search(self, key):
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
		node=self.root
		steps=0
		while node.right is not None:
			node=node.right
			steps+=1
		max_node=node
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
		return node.height if node is not None else -1
	
	def update_height(self, node):
		node.height=1+max(self.height(node.left),self.height(node.right))

	def balance_factor(self, node):
		return self.height(node.left)-self.height(node.right)
	
	def rotate_left(self,z):
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
		self.treeSize+=1
		new_node=AVLNode(key,val)
		new_node.is_real_node = True
		if self.root is None:
			self.root = new_node
			return new_node, 0, 0
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
		self.treeSize+=1
		steps = 0
		node_max=self.root
		while node_max.right is not None:
			node_max=node_max.right 
			steps+=1
		new_node=AVLNode(key,val)
		if key>node_max.key:
			node_max.right=new_node
			new_node.parent=node_max
			steps+=1
			promotes=self.balance_tree(node_max, is_insert=True)
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
		middle_node = AVLNode(key, val)
		middle_node.is_real_node = True
		self_height = self.root.height
		tree2_height = tree2.root.height
		if tree2.root.key < middle_node.key < self.root.key:
			if tree2_height <= self_height:
				middle_node.left = tree2.root
				tree2.root.parent = middle_node
				connecting_node = self.root
				while connecting_node.height > tree2_height:
					connecting_node = connecting_node.left
				middle_node.parent = connecting_node.parent
				connecting_node.parent.left = middle_node
				middle_node.right = connecting_node
				connecting_node.parent = middle_node
				p = self.balance_tree(middle_node)
			if self_height < tree2_height:
				middle_node.right = self.root
				self.root.parent = middle_node
				connecting_node = tree2.root
				while connecting_node.height > self_height:
					connecting_node = connecting_node.right
				middle_node.parent = connecting_node.parent
				connecting_node.parent.right = middle_node
				middle_node.left = connecting_node
				connecting_node.parent = middle_node
				p = tree2.balance_tree(middle_node)
				self.root = tree2.root
		if self.root.key < middle_node.key < tree2.root.key:
			if self_height <= tree2_height:
				middle_node.left = self.root
				self.root.parent = middle_node
				connecting_node = tree2.root
				while connecting_node.height > self_height:
					connecting_node = connecting_node.left
				middle_node.parent = connecting_node.parent
				connecting_node.parent.left = middle_node
				middle_node.right = connecting_node
				connecting_node.parent = middle_node
				p = tree2.balance_tree(connecting_node)
				self.root = tree2.root
			if tree2_height < self_height:
				middle_node.right = tree2.root
				tree2.root.parent = middle_node
				connecting_node = self.root
				while connecting_node.height > tree2_height:
					connecting_node = connecting_node.right
				middle_node.parent = connecting_node.parent
				connecting_node.parent.right = middle_node
				middle_node.left = connecting_node
				connecting_node.parent = middle_node
				p = self.balance_tree(middle_node)
		self.treeSize+=tree2.treeSize + 1
		return #O(abs(log(self.height) - tree2.height))


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
		small_tree = AVLTree()
		small_tree.root = node.left
		big_tree = AVLTree()
		big_tree.root = node.right
		tmp_node = node
		while tmp_node.parent != None:
			new_tree = AVLTree()
			parent = tmp_node.parent
			if parent.right.key == tmp_node.key:
				new_tree.root = parent.left
				small_tree.join(new_tree, parent.key, parent.value)
			else:
				new_tree.root = parent.right
				big_tree.join(new_tree, parent.key, parent.value)
		return small_tree, big_tree #O(logn)

	
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		array = []
		def in_order(node):
			if node is None:
				return
			in_order(node.left)
			array.append((node.key, node.value))
			in_order(node.right)
		in_order(self.root)
		return array #O(n)


	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
	"""
	def max_node(self):
		tmp_node = self.root
		if tmp_node == None:
			return None
		while tmp_node.right != None:
			tmp_node = tmp_node.right
		return tmp_node #O(logn)

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.treeSize #O(1)


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root #O(1)
