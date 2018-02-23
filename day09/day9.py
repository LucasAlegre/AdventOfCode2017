import re


def remove_exclamacao(s):
    string = ''
    i = 0
    while i < len(s):
        if s[i] == '!':
            i += 1
        else:
            string += s[i]
        i += 1

    return string


def remove_garbage(s):
    s = re.sub(r'<[^>]*>', '', s)
    return s


def count_garbages(s):
    return len(re.findall(r'<[^>]*>', s))


def points(s):
    score = 0
    counter = 0
    i = 0
    while i < len(s):
        if s[i] == '{':
            counter += 1
        elif s[i] == '}':
            score += counter
            counter -= 1
        i += 1

    return score


if __name__ == '__main__':

    with open('day9.txt') as f:
        input = [s.strip() for s in f.readlines()]

    s = input[0]

    s = remove_exclamacao(s)
    size_before = len(s)
    num_garbages = count_garbages(s)
    s = remove_garbage(s)
    size_after = len(s)

    print(size_before - size_after - (2*num_garbages))

