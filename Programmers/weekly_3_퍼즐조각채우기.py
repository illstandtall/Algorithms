def make_block(frag):
    cnt = 0
    w_max, w_min = max([f[0] for f in frag]), min([f[0] for f in frag])
    h_max, h_min = max([f[1] for f in frag]), min([f[1] for f in frag])
    block = [[0] * (h_max - h_min + 1) for _ in range(w_max - w_min + 1)]
    for f in frag:
        block[f[0]-w_min][f[1]-h_min] = 1
        cnt += 1
    return block, cnt


def find_frag(board, flag):
    from collections import deque
    n = len(board)+2
    que, blocks = deque(), dict()
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상, 하, 좌, 우
    dummy = [[-1] * n]
    board = dummy + [[-1] + b + [-1] for b in board] + dummy # 인덱스 계산 쉽게 더미 생성
    for i in range(n):
        for j in range(n):
            frag = list()
            if board[i][j] == flag: # table에서는 1인 것만, game_board에서는 0인 것만 찾기
                board[i][j] = -1
                que.append((i, j)), frag.append((i, j)) # que: bfs, frag: block 찾기
                while que:
                    x, y = que.pop()
                    for k in range(4):
                        if board[x + dx[k]][y + dy[k]] == flag: # 상, 하, 좌, 우
                            board[x + dx[k]][y + dy[k]] = -1
                            que.append((x + dx[k], y + dy[k])), frag.append((x + dx[k], y + dy[k]))
                block, cnt = make_block(frag)   # fragment를 block으로 만들기
                if blocks.get(cnt): blocks[cnt].append(block)
                else: blocks[cnt] = [block]
    return blocks


def rotate(block):
    return [list(b) for b in zip(*block[::-1])]


def puzzle(g_blocks, t_blocks):
    cnt = 0
    for i, blocks in t_blocks.items():
        for block in blocks:
            if i in g_blocks:
                for j in range(4):
                    if block in g_blocks[i]:
                        g_blocks[i].remove(block)
                        cnt += i
                        break
                    block = rotate(block)
    return cnt


def solution(game_board, table):
    table_blocks = find_frag(table, 1)     # 테이블 블록을 찾기
    game_board_blocks = find_frag(game_board, 0)     # 게임보드 빈칸 찾기
    return puzzle(game_board_blocks, table_blocks) # 몇 칸을 채울 수 있는지 찾기