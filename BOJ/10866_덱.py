import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
de = deque()

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front':
        de.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        de.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(de) == 0:
            print(-1)
        else:
            print(de.popleft())
    elif cmd[0] == 'pop_back':
        if len(de) == 0:
            print(-1)
        else:
            print(de.pop())
    elif cmd[0] == 'size':
        print(len(de))
    elif cmd[0] == 'empty':
        if len(de) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(de) == 0:
            print(-1)
        else:
            print(de[0])
    elif cmd[0] == 'back':
        if len(de) == 0:
            print(-1)
        else:
            print(de[-1])