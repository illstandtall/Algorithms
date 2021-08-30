def solution(word):
    answer = 0
    aeiou = { "A": 0,"E": 1,"I": 2,"O": 3,"U": 4 }
    for i, w in enumerate(word):
        answer += aeiou[w] * ((5**(5-i)-1)/(5-1)) + 1
    return answer