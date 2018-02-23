from collections import Counter

if __name__ == '__main__':

    with open('day11.txt') as f:
        input = [x for x in f.readlines()[0].strip().split(',')]

    directions = Counter()
    maior = 0
    for x in input:
        directions[x] += 1
        x = (directions['ne'] + directions['se']) - (directions['nw'] + directions['sw'])
        y = (directions['n']  + directions['nw']) - (directions['s']  + directions['se'])
        z = (directions['s']  + directions['sw']) - (directions['n']  + directions['ne'])
        if max(x, y, z) > maior:
            maior = max(x, y, z)

    print(maior)
