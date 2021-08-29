import sys


def dfs(i, j, prev_color):
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if visited[i][j] is True:
        return False
    color = picture[i][j]
    if color != prev_color:
        return False
    visited[i][j] = True
    dfs(i+1, j, color), dfs(i, j+1, color)
    dfs(i-1, j, color), dfs(i, j-1, color)
    return True


def solution(cnt, visited):
    for i in range(n):
        for j in range(n):
            if visited[i][j] is False:
                color = picture[i][j]
                chk = dfs(i, j, color)
                if chk and  color == 'R':
                    cnt[0] += 1
                elif chk and color == 'G':
                    cnt[1] += 1
                elif chk and color == 'B':
                    cnt[2] += 1
    return sum(cnt)


sys.setrecursionlimit(200000)
n = int(sys.stdin.readline())
picture = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

cnt = [0, 0, 0]
visited = [[False] * n for _ in range(n)]
res1 = solution(cnt, visited)

for i in range(n):
    picture[i] = ['R' if picture[i][j] == 'G' else picture[i][j] for j in range(n)]
cnt = [0, 0, 0]
visited = [[False] * n for _ in range(n)]
res2 = solution(cnt, visited)

print(res1, res2)