def solution(msg):
    ans = []
    dict = {chr(64 + i): i for i in range(1, 27)}
    s, e = 0, 1
    
    while e <= len(msg):
        word = msg[s:e]
        
        if word in dict:
            e += 1
        
        else:
            ans.append(dict[word[:-1]])
            dict[word] = len(dict) + 1
            s, e = e - 1, e
            
    ans.append(dict[word])
        
    return ans