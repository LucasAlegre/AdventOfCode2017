from collections import deque

puzzle = 386
spinlock = deque([0])

for i in range(1, 50000001):
    spinlock.rotate(-puzzle)
    spinlock.append(i)
    
s = list(spinlock)
print(s[s.index(0) + 1])