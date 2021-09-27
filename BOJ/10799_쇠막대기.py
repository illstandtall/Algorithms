import sys

pipe = sys.stdin.readline().rstrip()
result = 0
prev = False
st = []

for i in pipe:
    if i == '(':
        result += 1
        st.append(i)
        prev = True
    else:
        if prev is True:
            st.pop()
            result += (len(st)-1)
        else:
            st.pop()
        prev = False
print(result)