def solution(s):
    cnt = 0
    
    for i in range(len(s)):
        s = s[-1] + s[0 : -1]
        stack = []
        
        for p in s:
            if stack:
                if stack[-1] == "(" and p == ")":
                    stack.pop()
                elif stack[-1] == "{" and p == "}":
                    stack.pop()
                elif stack[-1] == "[" and p == "]":
                    stack.pop()
                else:
                    stack.append(p)
            else:
                stack.append(p)
        
        if not stack:
            cnt += 1
            
    return cnt