def generator(value, factor, multiple):

    while True:
        ok = False
        while not ok:
            value = (value*factor) % 2147483647
            if value % multiple == 0:
                ok = True

        yield value


## Generator A starts with 634
## Generator B starts with 301

if __name__ == '__main__':

    gen_A = generator(634, 16807, 4)
    gen_B = generator(301, 48271, 8)
    count = 0
    for _ in range(5000000):
        if bin(next(gen_A))[-16:] == bin(next(gen_B))[-16:]:
            count += 1

    print(count)
