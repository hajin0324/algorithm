def solution(elements):
    n = len(elements)
    elements = elements * 2
    ans = []

    for i in range(n):
        for j in range(n):
            ans.append(sum(elements[j:j + i + 1]))
                       
    return len(list(set(ans)))