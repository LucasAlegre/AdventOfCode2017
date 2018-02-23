from collections import defaultdict


class TuringMachine:

    def __init__(self):
        self.pc = 0
        self.tape = []
        self.cur_state = self.state_A

    def check_index(f):
        def wrapper(*args):
            if args[0].pc < 0:
                args[0].tape.insert(0, 0)
                args[0].pc = 0
            elif args[0].pc == len(args[0].tape):
                args[0].tape.append(0)
            return f(*args)
        return wrapper

    @check_index
    def state_A(self):
        if self.tape[self.pc]:
            self.tape[self.pc] = 0
            self.pc -= 1
            return self.state_E
        else:
            self.tape[self.pc] = 1
            self.pc += 1
            return self.state_B

    @check_index
    def state_B(self):
        if self.tape[self.pc]:
            self.tape[self.pc] = 0
            self.pc += 1
            return self.state_A
        else:
            self.tape[self.pc] = 1
            self.pc -= 1
            return self.state_C

    @check_index
    def state_C(self):
        if self.tape[self.pc]:
            self.tape[self.pc] = 0
            self.pc += 1
            return self.state_C
        else:
            self.tape[self.pc] = 1
            self.pc -= 1
            return self.state_D

    @check_index
    def state_D(self):
        if self.tape[self.pc]:
            self.tape[self.pc] = 0
            self.pc -= 1
            return self.state_F
        else:
            self.tape[self.pc] = 1
            self.pc -= 1
            return self.state_E

    @check_index
    def state_E(self):
        if self.tape[self.pc]:
            self.tape[self.pc] = 1
            self.pc -= 1
            return self.state_C
        else:
            self.tape[self.pc] = 1
            self.pc -= 1
            return self.state_A

    @check_index
    def state_F(self):
        if self.tape[self.pc]:
            self.tape[self.pc] = 1
            self.pc += 1
            return self.state_A
        else:
            self.tape[self.pc] = 1
            self.pc -= 1
        return self.state_E

    def run(self):
        for _ in range(12208951):
            self.cur_state = self.cur_state()
            print(_, 12208951, flush=True)
        print(sum(self.tape))


if __name__ == '__main__':
    t = TuringMachine()
    t.run()

    '''
    steps = 12667664
    states = {
        'A': ((1,  1, 'B'), (0, -1, 'C')),
        'B': ((1, -1, 'A'), (1,  1, 'D')),
        'C': ((0, -1, 'B'), (0, -1, 'E')),
        'D': ((1,  1, 'A'), (0,  1, 'B')),
        'E': ((1, -1, 'F'), (1, -1, 'C')),
        'F': ((1,  1, 'D'), (1,  1, 'A')),
    }
    tape = defaultdict(int)
    position = 0
    state = 'A'

    for _ in range(steps):
        value = tape[position]
        write, move, state = states[state][value]
        tape[position] = write
        position += move
        print(_, 12208951, flush=True)

    print(sum(tape.values()))
    '''
