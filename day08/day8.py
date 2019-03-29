import re

if __name__ == "__main__":

    with open('day8.txt') as f:
        input = [s.strip() for s in f.readlines()]

    registers = dict()
    answer = 0

    for line in input:
        m = re.match(r'(\w+)\s(\w+)\s(-?\d+)\s(if)\s(\w+)\s([<>!=]+)\s(-?\d+)', line)
        reg = m.group(1)
        if reg not in registers:
            registers[reg] = 0
        reg2 = m.group(5)
        if reg2 not in registers:
            registers[reg2] = 0
        if eval(str(registers[reg2])+m.group(6)+m.group(7)):
            if m.group(2) == 'inc':
                registers[reg] += int(m.group(3))
            else:
                registers[reg] -= int(m.group(3))
        x = max(list(registers.values()))
        if x > answer:
            answer = x

    print(answer)
