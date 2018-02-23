def read_input(file):
    with open(file, 'r') as f:
        program = [s.strip() for s in f.readlines()]
    return program


class Program:

    def __init__(self, file):
        self.registers = {chr(x): 0 for x in range(ord('a'), ord('z') + 1)}
        self.registers['a'] = 1
        self.program = read_input(file)
        self.pc = 0
        self.mul_count = 0
        self.halt = False

    def get_value(self, x):
        if x.lstrip("-").isdigit():
            return int(x)
        else:
            return self.registers[x]

    def set(self, x, y):
        self.registers[x] = self.get_value(y)

    def sub(self, x, y):
        self.registers[x] -= self.get_value(y)

    def add(self, x, y):
        self.registers[x] += self.get_value(y)

    def mul(self, x, y):
        self.registers[x] *= self.get_value(y)
        self.mul_count += 1

    def jnz(self, x, y):
        if self.get_value(x) != 0:
            self.pc += self.get_value(y)
        else:
            self.pc += 1

    def exec_inst(self, inst):
        if inst.startswith('set'):
            self.set(inst.split()[1], inst.split()[2])

        elif inst.startswith('sub'):
            self.sub(inst.split()[1], inst.split()[2])

        elif inst.startswith('mul'):
            self.mul(inst.split()[1], inst.split()[2])

        elif inst.startswith('jnz'):
            self.jnz(inst.split()[1], inst.split()[2])

        else:
            print('Inst not found')

        if not inst.startswith('jnz'):
            self.pc += 1

    def run(self):
        while not self.halt:
            if self.pc < 0 or self.pc >= len(self.program):
                self.halt = True
            else:
                self.exec_inst(self.program[self.pc])

        print(self.registers['h'])


if __name__ == '__main__':
    p = Program('day23.txt')
    p.run()