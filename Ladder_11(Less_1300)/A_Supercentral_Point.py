from collections import defaultdict
x_hashTable=defaultdict(list)
y_hashTable=defaultdict(list)
points=[]
for _ in range(int(input())):
	x,y=list(map(int,input().split()))
	points.append([x,y])
	x_hashTable[x].append(y)
	y_hashTable[y].append(x)

for i in x_hashTable:
	minVal=min(x_hashTable[i])
	maxVal=max(x_hashTable[i])
	x_hashTable[i]=[minVal,maxVal]

for i in y_hashTable:
	minVal=min(y_hashTable[i])
	maxVal=max(y_hashTable[i])
	y_hashTable[i]=[minVal,maxVal]



count=0
for val in points:
	flag=0
	dataX=x_hashTable[val[0]]
	if dataX[0]<val[1]<dataX[1]:
		pass
	else:
		flag=1

	dataY=y_hashTable[val[1]]
	if dataY[0]<val[0]<dataY[1]:
		pass
	else:
		flag=1

	if flag==0:
		count+=1
print(count)





