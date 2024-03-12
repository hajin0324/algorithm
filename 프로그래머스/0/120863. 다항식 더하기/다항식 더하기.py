def solution(polynomial):
    x_num, const = 0, 0
    
    for i in polynomial.split(' + '):
        if i.isdigit():
            const += int(i)
        else:
            x_num += 1 if i == 'x' else int(i[:-1])
            
    if x_num == 0:
        return f"{const}"
    elif x_num == 1:
        return 'x' if const == 0 else f"x + {const}"
    else:
        return f"{x_num}x" if const == 0 else f"{x_num}x + {const}"