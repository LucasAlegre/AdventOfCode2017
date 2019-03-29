if __name__ == "__main__":

    c = 0
    with open("day4.txt") as f:
        l = [x.strip() for x in f.readlines()]

    for x in l:
        z = x.split()

        p1 = []
        for i in z:
            p1.append(''.join(sorted(i)))

        p2 = set(p1)
        if len(p1) == len(p2):
            c += 1

    print(c)
