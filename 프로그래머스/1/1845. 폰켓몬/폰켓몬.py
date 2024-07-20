def solution(nums):
    monster = len(set(nums))
    
    if monster >= len(nums) / 2:
        return len(nums) / 2
    else:
        return monster