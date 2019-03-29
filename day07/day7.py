import re


def tower_weight(k, d, w):
    if not d[k]:
        return w[k]
    else:
        return w[k] + sum([tower_weight(x, d, w) for x in d[k]])


def check(d, w):
    for x in d:
        l = []
        for y in d[x]:
            l.append((tower_weight(y, d, w), y))
            if not all(x[0] == l[0][0] for x in l):
                print(l)


if __name__ == "__main__":

    with open('day7.txt') as f:
        input = f.readlines()
        input = [s.strip() for s in input]

    d = dict()
    weight = dict()

    for line in input:
        m = re.match(r'(\w+)\s(\(\d+\))', line)
        key = m.group(1)
        size = int(m.group(2)[1:-1])
        childs = []
        try:
            childs = line[re.search(r'(\s->\s)', line).end():]
            childs = childs.split(', ')
        except:
            childs = []

        weight[key] = size

        d[key] = tuple(childs)

    check(d, weight)
    print(weight['gozhrsf'])
