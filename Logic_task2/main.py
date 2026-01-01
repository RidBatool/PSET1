from collections import Counter

def window(log, pattern):
    if not log or not pattern:
        return ""
    freq= Counter(pattern)
    window={}
    count=0
    want=  len(freq)
    left=0
    result=""
    min_=float("inf")

    for right in range(len(log)):
        char = log[right]
        window[char]= window.get(char, 0)+1
        if char in freq and window[char]== freq[char]:
            count+=1

        while count== want:
            if right-left+1 < min_:
                min_ = right-left+1
                result=log[left:right+1]
                min_= right-left+1
            window[log[left]]-=1
            if log[left] in freq and window[log[left]]< freq[log[left]]:
                count-=1
            left+=1
    return result

log = "a"
pattern = "aa"
print(window(log, pattern))  