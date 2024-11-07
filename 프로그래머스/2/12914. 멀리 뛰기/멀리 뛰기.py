def solution(n):
    cnt = [0, 1, 2]
    for i in range(3, n + 1):
        cnt.append(cnt[i - 1] + cnt[i - 2])
        
    return cnt[n] % 1234567