import re


def bfs(graph):
    start = list(graph.keys())[0]
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


if __name__ == '__main__':

    with open('day12.txt') as f:
        input = [s.strip() for s in f.readlines()]

    graph = dict()
    for line in input:
        m = re.match(r'(\d+)\s<->\s([\d+(,?\s?)]+)', line)
        key = int(m.group(1))
        values = [int(x) for x in m.group(2).split(',')]
        graph[key] = set(values)
        for node in values:
            if node in graph.keys():
                graph[node].add(key)
            else:
                graph[node] = set([key])

    counter = 0
    while graph.keys():
        for x in bfs(graph):
            graph.pop(x)
        counter += 1
    print(counter)

