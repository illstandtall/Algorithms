import sys

n = int(sys.stdin.readline())
st = []

for i in range(n):
    inst = sys.stdin.readline().split()
    if inst[0] == 'push':
        st.append(int(inst[1]))
    elif inst[0] == 'pop':
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])
            st.pop()
    elif inst[0] == 'size':
        print(len(st))
    elif inst[0] == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif inst[0] == 'top':
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])