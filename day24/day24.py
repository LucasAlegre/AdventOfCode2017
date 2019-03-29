from collections import deque


def read_input(file):
    with open(file, 'r') as f:
        components = [tuple(map(int, s.strip().split('/'))) for s in f.readlines()]
    return components


if __name__ == '__main__':
    components = set(read_input('day24.txt'))

    max_score = 0
    longest = (0, 0)
    solutions = deque([([], 0, 0)]) # path, current pin, score
    while solutions:
        path, pin, score = solutions.popleft()
        max_score = max(max_score, score)
        if (len(path), score) > longest:
            longest = (len(path), score)
        for c in components:
            if c not in path and pin in c:
                solutions.append((path.copy() + [c], c[c.index(pin)-1], score + sum(c)))
    print(max_score, longest[1])


