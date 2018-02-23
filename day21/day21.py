import numpy as np

class Grid:

    def __init__(self, input):
        self.grid = Grid.to_np('.#./..#/###')
        self.rules = {}
        self.__build_rules(input)

    def to_np(s):
        return np.array([[c == '#' for c in l] for l in s.split('/')])

    def __build_rules(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()

        for line in lines:
            k, v = line.strip().split(' => ')
            k, v = Grid.to_np(k), Grid.to_np(v)
            for a in (k, np.fliplr(k)):
                for i in range(4):
                    self.rules[np.rot90(a, i).tobytes()] = v

    def step(self):
        size = len(self.grid)
        by = 2 if size % 2 == 0 else 3
        new_size = size * (by + 1) // by
        new_grid = np.empty((new_size, new_size), dtype=bool)

        squares = range(0, size, by)
        new_squares = range(0, new_size, by + 1)

        for i, ni in zip(squares, new_squares):
            for j, nj in zip(squares, new_squares):
                square = self.grid[i:i + by, j:j + by]
                enhanced = self.rules[square.tobytes()]
                new_grid[ni:ni + by + 1, nj:nj + by + 1] = enhanced
        self.grid = new_grid

    def run(self):
        for _ in range(18):
            self.step()
        print(self.grid.sum())


if __name__ == '__main__':

    grid = Grid('day21.txt')
    grid.run()




