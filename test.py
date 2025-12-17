from AVLTree import AVLTree

T = AVLTree()

T.insert(10, "10")
T.insert(5, "5")
T.insert(15, "15")

tree2 = AVLTree()
tree2.insert(40, "40")
tree2.insert(50, "50")
tree2.insert(60, "60")
tree2.insert(80, "80")
tree2.insert(90, "90")
#print(tree2.maxNode.key)
#print("ok")
T.join(tree2, 30, "30")
print(T.maxNode.key)


node, e = T.search(15)
t1, t2 = T.split(node) #there is a problem here
#print(t1.root.key)
print(t1.avl_to_array())
print(t2.avl_to_array())
#print(t1.root.left.key)
#print(t1.size())
#print(t2.root.key)

t1 = AVLTree()
t1.insert(15, "15")

t2 = AVLTree()
t2.insert(40, "40")
t1.join(t2, 30, "30")

#print(t1.root.key)
#print(t1.root.right.key)