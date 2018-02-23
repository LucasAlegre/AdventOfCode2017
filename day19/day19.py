def read_input(file):
    with open(file, 'r') as f:
        return f.read().splitlines(True)

class Network:

    coords = {'down': (1, 0), 'up': (-1, 0), 'left': (0, -1), 'right': (0, 1)}

    def __init__(self, file):
        self.grid = read_input(file)
        self.diagram = {}
        x = y = None
        for ir, row in enumerate(self.grid):
            for ic, column in enumerate(row):
                if column.strip():
                    if not any([x, y]):
                        x = ir
                        y = ic
                    self.diagram.update({(ir, ic): column})
        self.direction = 'down'
        self.coord = (0, self.grid[0].index('|'))
        self.path = ['|']
        self.seen = set()
        self.seen.add(self.coord)
        self.halt = False

    def step(self):
        x = self.coord[0] + Network.coords[self.direction][0]
        y = self.coord[1] + Network.coords[self.direction][1]
        char = self.diagram.get((x, y))
        if char:
            self.path.append(char)
            self.coord = (x, y)
            self.seen.add(self.coord)
            if char == '+':
                self.compute_next_direction()
        else:
            self.halt = True

    def compute_next_direction(self):
        for d, c in Network.coords.items():
            x = self.coord[0] + c[0]
            y = self.coord[1] + c[1]
            if self.diagram.get((x, y)) and (x, y) not in self.seen:
                self.direction = d
                break

    def run(self):
        while not self.halt:
            self.step()
        print(self.get_letters())
        print(len(self.path))
            
    def get_letters(self):
        return list(filter(lambda x: x.isalpha(), self.path))

if __name__ == '__main__':

    n = Network('day19.txt')
    n.run()
