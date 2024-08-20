def solution(my_string, overwrite_string, s):
    ans = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    return ans