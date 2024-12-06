def solution(s):
    s = s[2 : -2].split('},{')
    s.sort(key = len)
    
    ans = []
    for i in s:
        sp = i.split(',')
        for j in sp:
            if int(j) not in ans:
                ans.append(int(j))
                
    return ans