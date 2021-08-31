def solution(n, words):
    prev = set()

    prev.add(words[0])
    for i in range(1, len(words)):
        if words[i] in prev or words[i - 1][-1] != words[i][0]:
            return [(i % n) + 1, (i // n) + 1]
            break
        prev.add(words[i])
    else:
        return [0, 0]