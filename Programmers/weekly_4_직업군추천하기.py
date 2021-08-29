def solution(table, languages, preference):
    answer = ('Z', -1)
    lang_pref = {l: p for l, p in zip(languages, preference)}

    for tab in table:
        table_dict = dict()
        score = 0

        t = tab.split()
        table_dict = {t[1]: 5, t[2]: 4, t[3]: 3, t[4]: 2, t[5]: 1}

        for lang in lang_pref:
            if lang in table_dict:
                score += (lang_pref[lang] * table_dict[lang])

        if answer[1] < score or (answer[1] == score and answer[0] > t[0]):
            answer = (t[0], score)

    return answer[0]