def solution(participant, completion):
# participant.sort()
#     completion.sort()

#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[-1]


def solution(participant, completion):
    dic = {}
    for key in participant:
        dic[key] = dic.get(key, 0) + 1
    for k in completion:
        dic[k] -= 1
    answer = [i for i in dic if dic[i] > 0]

    return answer[0]