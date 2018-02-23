def read_input(file):
    with open(file, 'r') as f:
        program = [s.strip() for s in f.readlines()]
    return program


class Program:

    def __init__(self, file):
        self.registers = {chr(x): 0 for x in range(ord('a'), ord('z') + 1)}
        self.program = read_input(file)
        self.pc = 0
        self.lastSound = None
        self.halt = False

    def get_value(self, x):
        if x.lstrip("-").isdigit():
            return int(x)
        else:
            return self.registers[x]

    def snd(self, x):
        self.lastSound = self.get_value(x)

    def set(self, x, y):
        self.registers[x] = self.get_value(y)

    def add(self, x, y):
        self.registers[x] += self.get_value(y)

    def mul(self, x, y):
        self.registers[x] *= self.get_value(y)

    def mod(self, x, y):
        self.registers[x] = self.registers[x] % self.get_value(y)

    def rcv(self, x):
        if self.get_value(x) != 0:
            self.halt = True

    def jgz(self, x, y):
        if self.get_value(x) > 0:
            self.pc += self.get_value(y)
        else:
            self.pc += 1

    def exec_inst(self, inst):
        if inst.startswith('snd'):
            self.snd(inst.split()[1])

        elif inst.startswith('set'):
            self.set(inst.split()[1], inst.split()[2])

        elif inst.startswith('add'):
            self.add(inst.split()[1], inst.split()[2])

        elif inst.startswith('mul'):
            self.mul(inst.split()[1], inst.split()[2])

        elif inst.startswith('mod'):
            self.mod(inst.split()[1], inst.split()[2])

        elif inst.startswith('rcv'):
            self.rcv(inst.split()[1])

        elif inst.startswith('jgz'):
            self.jgz(inst.split()[1], inst.split()[2])

        else:
            print('Inst nof found')

        if not inst.startswith('jgz'):
            self.pc += 1

    def run(self):
        while not self.halt:
            self.exec_inst(self.program[self.pc])


if __name__ == '__main__':
    p = Program('day18.txt')
    p.run()
    print(p.lastSound)