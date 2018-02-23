if __name__ == "__main__":

    g = {}

    n = 1
    x = 0
    y = 0
    g[n] = (x, y)

    ladoSize = 3

    for i in range(1000):
        x += 1
        y += -1

        for j in range(ladoSize - 1):
            n += 1
            y += 1
            g[n] = (x, y)

        for j in range(ladoSize - 1):
            n += 1
            x += -1
            g[n] = (x, y)

        for j in range(ladoSize - 1):
            n += 1
            y += -1
            g[n] = (x, y)

        for j in range(ladoSize - 1):
            n += 1
            x += 1
            g[n] = (x, y)

        ladoSize += 2

    print(g[265149])




