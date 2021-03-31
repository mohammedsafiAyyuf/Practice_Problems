import math
n,m=list(map(int,input().split()))
childrens=[math.ceil(i/m) for i in list(map(int,input().split()))]
maxVal=max(childrens)
#print(childrens)
idx=(childrens[::-1]).index(maxVal)
print(n-idx)