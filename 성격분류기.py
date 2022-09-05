import pandas as pd
import os


def solution(survey, choice):
    score_obj = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }

    def choice_to_score(rec_survey, rec_choice):
        negative_side = rec_survey[:1]
        positive_side = rec_survey[1:2]
        if rec_choice <= 3:
            score_obj[negative_side] += abs(rec_choice - 4)
        elif rec_choice > 4:
            score_obj[positive_side] += rec_choice - 4

    for i in range(len(survey)) :
        choice_to_score(survey[i], choice[i])

    keys = list(score_obj.keys())
    ans = []
    for i in range(0, 4) :
        first_ident = keys[i*2]
        sec_ident = keys[i*2+1]
        if score_obj[first_ident] < score_obj[sec_ident] :
            ans.append(sec_ident)
        elif score_obj[first_ident] > score_obj[sec_ident] :
            ans.append(first_ident)
        elif score_obj[first_ident] == score_obj[sec_ident]:
            ans.append(sorted([first_ident, sec_ident])[0])

    print("".join(ans))

    answer = "".join(ans)

    return answer


example = [
    ["AN", "CF", "MJ", "RT", "NA"],
    ["TR", "RT", "TR"]
]
choices = [
    [5, 3, 2, 7, 5],
    [7, 1, 3]
]

solution(example[1], choices[1])
