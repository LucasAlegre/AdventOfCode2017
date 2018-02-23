import numpy as np
from collections import deque


class Cluster:

    SIZE = 1001
    state = {'clean': 0, 'weakened': 1, 'infected': 2, 'flagged': 3}

    def __init__(self, file):
        self.grid = np.empty((Cluster.SIZE, Cluster.SIZE))
        self.grid.fill(Cluster.state['clean'])
        self.virus_pos = (Cluster.SIZE // 2, Cluster.SIZE // 2)
        self.__read_input(file)
        self.directions = deque(['w', 'a', 's', 'd'])
        self.infection_count = 0

    def get_direction(self):
        return self.directions[0]

    def __read_input(self, file):
        with open(file, 'r') as f:
            lines = [l.strip() for l in f.readlines()]
            self.grid[self.virus_pos[0] - 12:self.virus_pos[0] + 12 + 1,
                      self.virus_pos[1] - 12:self.virus_pos[1] + 12 + 1] = np.array([[2 if c == '#' else 0 for c in l] for l in lines])

    def __burst(self):
        if self.grid[self.virus_pos[0], self.virus_pos[1]] == Cluster.state['clean']:
            self.directions.rotate(-1)
            self.grid[self.virus_pos[0], self.virus_pos[1]] = Cluster.state['weakened']

        elif self.grid[self.virus_pos[0], self.virus_pos[1]] == Cluster.state['weakened']:
            self.grid[self.virus_pos[0], self.virus_pos[1]] = Cluster.state['infected']
            self.infection_count += 1

        elif self.grid[self.virus_pos[0], self.virus_pos[1]] == Cluster.state['infected']:
            self.directions.rotate(1)
            self.grid[self.virus_pos[0], self.virus_pos[1]] = Cluster.state['flagged']

        elif self.grid[self.virus_pos[0], self.virus_pos[1]] == Cluster.state['flagged']:
            self.directions.rotate(2)  # reverse direction
            self.grid[self.virus_pos[0], self.virus_pos[1]] = Cluster.state['clean']

        self.__update_pos()

    def __update_pos(self):
        if self.get_direction() == 'w':
            self.virus_pos = (self.virus_pos[0]-1, self.virus_pos[1])
        elif self.get_direction() == 'a':
            self.virus_pos = (self.virus_pos[0], self.virus_pos[1]-1)
        elif self.get_direction() == 's':
            self.virus_pos = (self.virus_pos[0]+1, self.virus_pos[1])
        elif self.get_direction() == 'd':
            self.virus_pos = (self.virus_pos[0], self.virus_pos[1]+1)

    def run(self):
        for _ in range(10000000):
            self.__burst()
        print(self.infection_count)


if __name__ == '__main__':
    c = Cluster('day22.txt')
    c.run()


