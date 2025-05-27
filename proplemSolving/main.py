import collections as cl


def deque_simulation():
    d1 = cl.deque([1, 2, 3, 4, 5])
    d2 = cl.deque([1, 2, 3, 4, 5], maxlen=3)
    print(d1, d2, d1[2])


deque_simulation()
