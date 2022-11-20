def solution(s):
    right = 0
    left = 0
    for i in list(s) :
        if i == "(":
            right += 1
        else :
            left += 1
        if right == 0 and left == 1 :
            return False
        if 0 < right == left > 0:
            right = 0
            left = 0
    if right == 0 and left == 0 :
        return True
    else :
        return False


a = ["()()", "(())()", ")()(", "(()("]
for i in a:
    solution(i)
