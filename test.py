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
#print("ok")
T.join(tree2, 30, "30")
print(T.root.key)