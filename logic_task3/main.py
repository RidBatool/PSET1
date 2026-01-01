def balanced_performance(scoreA, scoreB):
    n1= len(scoreA)
    n2=len(scoreB)
    total= n1+n2

    i=j=0
    prev=0
    curr=0

    for _ in range(total//2+1):
        prev= curr
        if i<n1 and (j>=n2 or scoreA[i]<=scoreB[j]):
            curr= scoreA[i]
            i+=1
        else:
            curr= scoreB[j]
            j+=1

    if total%2==0:
        return (prev+curr)/2
    else:
        return float(curr)
scoresA = [1, 2]
scoresB = [3,4]
print(balanced_performance(scoresA, scoresB))
