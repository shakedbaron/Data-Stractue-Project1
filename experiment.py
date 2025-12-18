import random

from AVLTree import AVLTree

def ordered(i):
    a = []
    for j in range(300*(2**i)):
        a.append(j)
    return a

def opposite_ordered(i):
    a = []
    for j in range(300*(2**i)):
        a.append(300*(2**i) - j)
    return a

def random_array(i):
    a = []
    for j in range(300*(2**i)):
        a.append(j)
    random.shuffle(a)
    return a

def random_close_inversions(i):
    a = []
    for j in range(300*(2**i)):
        a.append(j)
    for k in range(300*(2**i) - 1):
        if 1 == random.choice((0, 1)):
            a[k + 1], a[k] = a[k], a[k + 1]
    return a

#print(ordered(1)[:20])
#print(opposite_ordered(1)[:20])
#print(random_array(1)[:20])
#print(random_close_inversions(1)[:20])

t_ordered = AVLTree()
ordered = ordered(1)
total_e = 0
total_h = 0
for a in ordered:
    x, e, h = t_ordered.finger_insert(a, 'a')
    total_e+=e
    total_h+=h
#print(total_e)
#print(total_h)
#print(t.avl_to_array())

t_opposite_ordered = AVLTree()
opposite_ordered = opposite_ordered(1)
total_e = 0
total_h = 0
for a in opposite_ordered:
    x, e, h = t_opposite_ordered.finger_insert(a, 'a')
    total_e+=e
    total_h+=h
print(total_e)
print(total_h)
print(t_opposite_ordered.avl_to_array())


