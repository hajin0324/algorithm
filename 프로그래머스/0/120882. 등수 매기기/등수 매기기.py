def solution(score):
    avg = [(e[0] + e[1]) / 2 for e in score]
    avg_sort = sorted(avg, reverse=True)
    
    return [avg_sort.index(a) + 1 for a in avg]