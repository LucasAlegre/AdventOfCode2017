import re


def read_file(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            m = re.match(r'p=<(-?\d+),(-?\d+),(-?\d+)>,\sv=<(-?\d+),(-?\d+),(-?\d+)>,\sa=<(-?\d+),(-?\d+),(-?\d+)>', line.strip())
            yield (int(m.group(1)), int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)), int(m.group(6))), (int(m.group(7)), int(m.group(8)), int(m.group(9)))


class Particle:

    def __init__(self, p, v, a, id):
        self.p = p
        self.v = v
        self.a = a
        self.id = id

    def __str__(self):
        return self.p.__str__() + self.v.__str__() + self.a.__str__()

    def manhattan_a(self):
        return sum(abs(x) for x in self.a)


if __name__ == '__main__':

    particles = []
    id = 0
    for p, v, a in read_file('day20.txt'):
        particles.append(Particle(p, v, a, id))
        id += 1

    print(sorted(particles, key=lambda x: x.manhattan_a())[0].id)

