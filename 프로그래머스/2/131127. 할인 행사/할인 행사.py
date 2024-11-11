def solution(want, number, discount):
    ans = 0
    prod = {}
    for i in want:
        prod[i] = 0
        
        
    for i in range(len(discount)):
        if discount[i] in prod:
            prod[discount[i]] += 1
            
        if i >= 10 and discount[i - 10] in prod:
            prod[discount[i - 10]] -= 1

        can = True
        for j in range(len(want)):
            if prod[want[j]] != number[j]:
                can = False
            
        if can:
            ans += 1

    return ans