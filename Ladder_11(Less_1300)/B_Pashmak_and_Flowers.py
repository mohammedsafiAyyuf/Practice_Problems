import math
n=int(input())
flower=list(map(int,input().split()))
flower.sort()
minCount=flower.count(flower[0])
maxCount=flower.count(flower[-1])
print(flower[-1]-flower[0],end=" ")
if flower[0]!=flower[-1]:
	print(minCount*maxCount)
else:
	print(n*(n-1)//2)




