def isValid(s):
    balance=0
    for ch in s:
        if ch == '(':
            balance+=1
        elif ch == ')':
            if balance==0:
                return False
            balance-=1
    return balance==0  


def invalidParantheseisremoval(s):
    result = set()
    visited = set()

    def dfs(curr):
        if curr in visited:
            return
        visited.add(curr)

        if isValid(curr):
            result.add(curr)
            return

        for i in range(len(curr)):
            if curr[i] not in '()':
                continue
            dfs(curr[:i] + curr[i+1:])

    dfs(s)

    min_len = -1
    for x in result:
        min_len = max(min_len, len(x))

    new_result=[]        
    for x in result:
        if len(x) == min_len:
            new_result.append(x)

    return new_result


# s = "()())()"
#s="(a)())()"
#s="()"
# s="abc"
s="((("
print(invalidParantheseisremoval(s))
