def solution(numbers, target):
    global cnt
    cnt = 0
    
    def calc(val, idx):
        global cnt
        
        if idx >= len(numbers):
            if val == target:
                cnt += 1
            return

        val += numbers[idx]
        calc(val, idx + 1)

        val -= numbers[idx] * 2
        calc(val, idx + 1)

        return

    calc(0, 0)
    
    return cnt