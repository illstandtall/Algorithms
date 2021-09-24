def solution(enter, leave):
    n = len(leave)
    answer = [0] * n
    room = set()
    j = 0

    for i in range(n):
        if leave[i] in room:
            room.remove(leave[i])
            for r in room:
                answer[r - 1] += 1
                answer[leave[i] - 1] += 1
            continue
        while j < n:
            if leave[i] == enter[j]:
                for r in room:
                    answer[r - 1] += 1
                    answer[leave[i] - 1] += 1
                j += 1
                break
            else:
                room.add(enter[j])
            j += 1

    return answer