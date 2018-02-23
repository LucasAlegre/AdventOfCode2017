from functools import reduce


class Node():

    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
        self.neighbours = []

    def find_neighbours(self, grid):
        if self.data:
            for coord in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                try:
                    x = self.x + coord[0]
                    y = self.y + coord[1]
                    if x >= 0 and y >= 0:
                        node = grid[x][y]
                        if node.data:
                            self.neighbours.append(node)
                except IndexError:
                    continue

    def get_region(self, region=None):
        if not region:
            region = [self] if self.data else []

        if self.data:
            for neigh in self.neighbours:
                if neigh not in region:
                    region.append(neigh)
                    neigh.get_region(region)
        return region


def knot_hash(s):

    lenghts = [ord(c) for c in s]
    lenghts.extend([17, 31, 73, 47, 23])

    l = list(range(256))
    skip = 0
    t_rotations = 0
    for _ in range(64):
        for lenght in lenghts:
            l[0:lenght] = reversed(l[0:lenght])
            x = (skip + lenght) % len(l)
            t_rotations += x
            l = l[x:] + l[:x]
            skip += 1

    for _ in range(t_rotations % len(l)):
        l.insert(0, l.pop(len(l) - 1))

    r = []
    ind = 0
    for _ in range(16):
        r.append(reduce(lambda x, y: x ^ y, l[ind:ind + 16]))
        ind += 16

    hash_string = ''.join(map('{:02x}'.format, r))

    return hash_string


if __name__ == "__main__":

    myinput = 'ugkiagan'

    grid = [[0]*128 for _ in range(128)]
    nodes = []

    for i in range(128):
        s = knot_hash(myinput + '-' + str(i))
        bin_hash = ''
        for c in s:
            bin_hash += '{:04b}'.format(int(c, 16))
        for j, c in enumerate(bin_hash):
            if c == '1':
                node = Node(i, j, 1)
            else:
                node = Node(i, j, 0)
            nodes.append(node)
            grid[i][j] = node

    for node in nodes:
        node.find_neighbours(grid)

    regions = []
    num_of_regions = 0
    for node in nodes:
        if node not in regions:
            region = node.get_region()
            if region:
                regions.extend(region)
                num_of_regions += 1

    print(num_of_regions)