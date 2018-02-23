def read_input(file):
    with open(file, 'r') as f:
        program = [s.strip() for s in f.readlines()]
    return program


class Program:

    def __init__(self, file, id):
        self.registers = {chr(x): 0 for x in range(ord('a'), ord('z') + 1)}
        self.registers['p'] = id
        self.instructions = read_input(file)
        self.pc = 0
        self.halt = False
        self.otherProgram = None
        self.queue = []
        self.deadlock = False
        self.timesSent = 0

    def set_other_program(self, other):
        self.otherProgram = other

    def get_value(self, x):
        if x.lstrip("-").isdigit():
            return int(x)
        else:
            return self.registers[x]

    def snd(self, x):
        self.otherProgram.queue.append(self.get_value(x))
        self.timesSent += 1

    def set(self, x, y):
        self.registers[x] = self.get_value(y)

    def add(self, x, y):
        self.registers[x] += self.get_value(y)

    def mul(self, x, y):
        self.registers[x] *= self.get_value(y)

    def mod(self, x, y):
        self.registers[x] = self.registers[x] % self.get_value(y)

    def rcv(self, x):
        if self.queue:
            self.registers[x] = self.queue.pop(0)
        else:
            self.deadlock = True
            self.pc += -1

    def jgz(self, x, y):
        if self.get_value(x) > 0:
            self.pc += self.get_value(y)
        else:
            self.pc += 1

    def is_deadlock(self):
        return self.deadlock

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
        self.exec_inst(self.instructions[self.pc])


if __name__ == '__main__':
    p0 = Program('day18.txt', 0)
    p1 = Program('day18.txt', 1)
    p0.set_other_program(p1)
    p1.set_other_program(p0)

    while not (p0.is_deadlock() and p1.is_deadlock()):
        p0.run()
        p1.run()

    print(p1.timesSent)
