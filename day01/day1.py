from itertools import tee


if __name__ == "__main__":

    l = [int(x) for x in input()]
    tam = len(l)
    c = 0
    t = 0

    for i in range(tam):
        if(l[i] == l[(i + int(tam/2)) % tam]):
            t += l[i]
    print(t)
