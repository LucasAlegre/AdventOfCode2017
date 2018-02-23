from functools import reduce

if __name__ == '__main__':

    with open('day10.txt') as f:
        input = [x.strip() for x in f.readlines()][0]

    lenghts = []
    for c in input:
        lenghts.append(ord(c))
    lenghts.extend([17, 31, 73, 47, 23])

    l = list(range(256))
    skip = 0
    t_rotations = 0
    for _ in range(64):
        for lenght in lenghts:
            l[0:lenght] = reversed(l[0:lenght])
            x = (skip + lenght) % len(l)
            t_rotations += x
            l = l[x:] + l[:x]
            skip += 1

    for _ in range(t_rotations % len(l)):
        l.insert(0, l.pop(len(l)-1))

    r = []
    ind = 0
    for _ in range(16):
        r.append(reduce(lambda x, y: x ^ y, l[ind:ind+16]))
        ind += 16

    hash_string = ''
    for x in r:
        hash_string += format(x, 'x')

    print(hash_string)
