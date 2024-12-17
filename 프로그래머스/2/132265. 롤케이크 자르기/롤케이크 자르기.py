from collections import Counter

def solution(topping):
    ans = 0
    cheol = set()
    bro = Counter(topping)
        
    for t in topping:
        cheol.add(t)
        bro[t] -= 1
        
        if bro[t] == 0:
            del bro[t]
        
        if len(cheol) == len(bro):
            ans += 1
            
    return ans