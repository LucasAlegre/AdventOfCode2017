from collections import deque
import re


def read_file(file):
    with open(file, 'r') as f:
        return f.read().strip().split(',')


if __name__ == '__main__':

    inp = read_file('day16.txt')

    programs = deque([chr(i) for i in range(ord('a'), ord('p') + 1)])

    seen = []
    config = None
    for i in range(1000000000):
        p = ''.join(programs)
        if p not in seen:
            for dance in inp:

                spin = re.match(r's(\d+)', dance)
                exchange = re.match(r'x(\d+)/(\d+)', dance)
                partner = re.match(r'p(\w)/(\w)', dance)

                if spin:
                    programs.rotate(int(spin.group(1)))

                elif exchange:
                    i, j = int(exchange.group(1)), int(exchange.group(2))
                    programs[i], programs[j] = programs[j], programs[i]

                elif partner:
                    i, j = programs.index(partner.group(1)), programs.index(partner.group(2))
                    programs[i], programs[j] = programs[j], programs[i]

            seen.append(p)
        else:
            config = seen[1000000000 % i]
            break


    print(config)




