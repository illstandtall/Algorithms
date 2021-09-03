def solution(numbers, target):
    from collections import deque
    que = deque()
    que.append(0)

    for i in range(len(numbers)):
        lenth = len(que)
        for j in range(lenth):
            x = que.popleft()
            que.append(x + numbers[i])
            que.append(x - numbers[i])

    answer = 0
    for x in que:
        if x == target: answer += 1
    return answer