def solution(s, n):
    ans = ""
    for i in list(s):

        if ord(i) < 91 :
            current_size = "Big"
        else :
            current_size = "small"

        # print(ord(i), n, current_size)

        if i == " " :
            ans += " "
        else :
            if current_size == "Big" :
                if ord(i) + n > 90 :
                    current_str = chr(ord(i) + n - 26)
                else :
                    current_str = chr(ord(i) + n)
            else :
                if ord(i) + n > 122 :
                    current_str = chr(ord(i) + n - 26)
                else :
                    current_str = chr(ord(i) + n)
            ans += current_str

    print(ans)
    # print(sicor)
    return ans


solution("AaZz", 25)