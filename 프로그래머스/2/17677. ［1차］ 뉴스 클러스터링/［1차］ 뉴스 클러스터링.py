def solution(str1, str2):
    s1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    
#   교집합
    s1_c = s1.copy()
    s2_c = s2.copy()
    uni = []
    for i in s1_c:
        if i in s2_c:
            s2_c.remove(i)
            uni.append(i)
            
#   합집합
    inter = s1[:] + s2[:]
    for i in uni:
        if i in inter:
            inter.remove(i)
    
    if not inter:
        return 65536
    return int(len(uni) / len(inter) * 65536)