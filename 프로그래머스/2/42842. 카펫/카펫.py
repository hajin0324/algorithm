def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            j = yellow // i
            if 2 * (i + j) + 4 == brown:
                return [j + 2, i + 2]