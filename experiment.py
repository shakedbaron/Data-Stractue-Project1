import random, math

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

#for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#    t_ordered = AVLTree()
#    new_ordered = ordered(i)
#    total_e = 0
#    total_h = 0
#    for a in new_ordered:
#        x, e, h = t_ordered.finger_insert(a, 'a')
#        total_e+=e
#        total_h+=h
#    print("ordered "+str(i))
#    n = 300*(2**i)
#    print(n*math.log(n, 2))
#    print("e: " + str(total_e))
#    print("h: " + str(total_h))
#print(t.avl_to_array())

#for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#    t_opposite_ordered = AVLTree()
#    new_opposite_ordered = opposite_ordered(i)
#    total_e = 0
#    total_h = 0
#    for a in new_opposite_ordered:
#        x, e, h = t_opposite_ordered.finger_insert(a, 'a')
#        total_e+=e
#        total_h+=h
#    print("opposite ordered "+str(i))
#    print("e: " + str(total_e))
#    print("h: " + str(total_h))

#print(t_opposite_ordered.avl_to_array()[:20])

def average(a):
    sum = 0.0
    for i in range(len(a)):
        sum += a[i]
    return sum / len(a)

#print("random array 10")
#e_array = []
#h_array = []
#for i in range(20):
#    t_random = AVLTree()
#    rew_andom_array = random_array(10)
#    total_e = 0
#    total_h = 0
#    for a in rew_andom_array:
#        x, e, h = t_random.finger_insert(a, 'a')
#        total_e+=e
#        total_h+=h
#    e_array.append(total_e)
#    h_array.append(total_h)
#    #print("random array 5")
#    #print("e: " + str(total_e))
#    #print("h: " + str(total_h))
#print("average e: " + str(average(e_array)))
#print("average h: " + str(average(h_array)))

#print("random close inversions 10")
#e_array = []
#h_array = []
#for i in range(20):
#    t_random_close_inversions = AVLTree()
#    new_random_close_inversions = random_close_inversions(10)
#    total_e = 0
#    total_h = 0
#    for a in new_random_close_inversions:
#        x, e, h = t_random_close_inversions.finger_insert(a, 'a')
#        total_e+=e
#        total_h+=h
#    e_array.append(total_e)
#    h_array.append(total_h)
#    #print("random array 5")
#    #print("e: " + str(total_e))
#    #print("h: " + str(total_h))
#print("average e: " + str(average(e_array)))
#print("average h: " + str(average(h_array)))

print("reverse")
I = [179700, 719400, 2878800, 11517600, 46075200]
n = [300.0*(2**i) for i in [1, 2, 3, 4, 5]]
for i in [1, 2, 3, 4, 5]:
    b = n[i-1]*math.log((I[i-1]/n[i-1]) + 2)
    print(str(i)+": "+ str(b))
    print(str(i) + ": "+str(n[i-1]*math.log(n[i-1], 2)))