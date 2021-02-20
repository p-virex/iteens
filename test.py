from collections import deque


def A(ind):
    a = [(1, 1), (2, 2), (3, 3), (4, 4)]
    p = deque(a)
    p.rotate(ind*2)
    print(p)

for I in range(4):
    A(I)