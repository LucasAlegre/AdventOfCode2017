if __name__ == "__main__":

    l = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]

    configs = set()
    configs.add(tuple(l))

    repeated = False
    count = 0
    while not repeated:

        max = 0
        for i in range(len(l)):
            if l[i] > l[max]:
                max = i

        elements = l[max]
        l[max] = 0

        i = max + 1
        while elements != 0:
            if i == len(l):
                i = 0

            l[i] += 1
            i += 1
            elements -= 1

        if tuple(l) in configs:
            repeated = True
            print(tuple(l))
        else:
            configs.add(tuple(l))
            count += 1

    print(len(configs))
