def solution(scores):
    import heapq
    answer = ''

    stu_scores = list(map(list, zip(*scores)))
    for i in range(len(stu_scores)):
        stu_scores[i].sort()
        if stu_scores[i][0] == scores[i][i] and stu_scores[i][0] != stu_scores[i][1]:
            stu_scores[i] = stu_scores[i][1:]
        elif stu_scores[i][-1] == scores[i][i] and stu_scores[i][-1] != stu_scores[i][-2]:
            stu_scores[i] = stu_scores[i][:-1]

        score = sum(stu_scores[i]) / len(stu_scores[i])

        if score >= 90: answer += 'A'
        elif score >= 80: answer += 'B'
        elif score >= 70: answer += 'C'
        elif score >= 50: answer += 'D'
        else: answer += 'F'

    return answer