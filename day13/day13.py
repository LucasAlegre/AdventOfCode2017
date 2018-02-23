from collections import deque
import re


def rotate_all(l, direction):
    for j, d in enumerate(l):
        if d:
            if d[-1]:
                direction[j] = -1
            elif d[0]:
                direction[j] = 1
        d.rotate(direction[j])


if __name__ == "__main__":

    l = [deque() for _ in range(99)]

    with open('day13.txt') as f:
        inp = [s.strip() for s in f.readlines()]

    for line in inp:
        m = re.match(r'(\d+):\s(\d+)', line)
        key = int(m.group(1))
        value = int(m.group(2))

        l[key].append(True)
        for _ in range(value-1):
            l[key].append(False)

    delay = 0
    ok = False
    while not ok:
        c = False
        for i, d in enumerate(l):
            if d:
                if ((i + delay) % (2*(len(d) - 1))) == 0:
                    c = True
        if not c:
            ok = True
        else:
            delay += 1

    print(delay)

    cost = 0
    direction = {key: 1 for key in range(len(l))}
    for i in range(len(l)):
        if l[i]:
            if l[i][0]:
                cost += i * len(l[i])
        rotate_all(l, direction)

    print(cost)
