def solution(weights, head2head):
    n = len(weights)
    # 0: 번호, 1: 몸무게, 2: 승률, 3: 자신보다 무거운 복서 이긴 횟수, 4: 전적없음
    answer = [[0] * 5 for _ in range(n)]

    for i in range(n):
        cnt = 0
        answer[i][0] = i + 1
        answer[i][1] = weights[i]

        for j in range(i + 1, n):
            if head2head[i][j] == 'W':
                answer[i][2] += 1  # 승률 체크
                if weights[i] < weights[j]:
                    answer[i][3] += 1  # 이긴 상대가 본인 보다 더 무거운지 체크
            elif head2head[i][j] == 'L':
                answer[j][2] += 1
                if weights[i] > weights[j]:
                    answer[j][3] += 1
            else:
                answer[i][4] += 1
                answer[j][4] += 1

    for lis in answer:
        if (n - 1 - lis[4]) != 0:
            lis[2] /= (n - 1 - lis[4])
        else:
            lis[2] = 0

    answer.sort(key=lambda x: (-x[2], -x[3], -x[1], x[0]))
    return [lis[0] for lis in answer]