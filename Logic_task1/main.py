def contribution(list_):
    impact=[1]*len(list_)

    pre_product=1
    for i in range(len(list_)):
        impact[i]*=pre_product
        pre_product*=list_[i]
    pos_product=1
    for j in range(len(list_)-1, -1, -1):
        impact[j]*=pos_product
        pos_product*=list_[j]
    return impact
print("Output 1:")
print(contribution([1, 2, 3, 4])) 
print("Output 2:")
print(contribution([-1,1, 0, -3, 3]))
