import sys

t = sys.stdin.readline()

for i in range(0, int(t)):
    string = sys.stdin.readline().split()
    for j in range(0, len(string)):
        print(string[j][::-1], end=' ')