n=int(input())
array=list(map(int,input().split()))
maxOnes=sum(array)
newArray=[]
for i in array:
	newArray.append(1 if i==0 else -1)

curMaxSum=0
totalMaxSum=0
for i in newArray:
	curMaxSum=max(0,curMaxSum+i)
	totalMaxSum=max(totalMaxSum,curMaxSum)

print(maxOnes+totalMaxSum if maxOnes!=n else n-1)

