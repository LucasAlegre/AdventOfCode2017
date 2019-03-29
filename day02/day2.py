from itertools import permutations

if __name__ == "__main__":

    c = 0
    with open("t.txt") as f:
        content = f.readlines()
        content = [x.strip() for x in content]

    for x in content:
        l = [int(i) for i in x.split()]
        for x in permutations(l, 2):
            if x[0] % x[1] == 0:
                c += x[0] / x[1]
                break
            elif x[1] % x[0] == 0:
                c += x[1] / x[0]
                break

    print(c)
