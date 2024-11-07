def solution(people, limit):
    ans = 0
    s, e = 0, len(people) - 1
    people.sort()
    
    while (s <= e):
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
        else:
            e -= 1
        ans += 1
        
    return ans