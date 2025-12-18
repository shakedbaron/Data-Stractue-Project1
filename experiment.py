import random

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

print(ordered(1)[:20])
print(opposite_ordered(1)[:20])
print(random_array(1)[:20])
print(random_close_inversions(1)[:20])

