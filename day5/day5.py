def step(l, pc, count):

    if l[pc] >= 3:
        l[pc] += -1
        pc += l[pc] + 1

    else:
        l[pc] += 1
        pc += l[pc] - 1

    count += 1

    return pc, count


if __name__ == "__main__":

    with open('day5.txt') as f:
        l = f.readlines()

    l = [x.strip() for x in l]
    l = [int(x) for x in l]

    end = len(l)
    pc = 0
    count = 0

    while pc < end:
        pc, count = step(l, pc, count)

    print(count)
