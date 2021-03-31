from math import ceil
n,k=list(map(int,input().split()))

array=list(map(int,input().split()))
array.sort()
val=array[k-1]
count=0
if val>0:
	for i in array:
		if i>=val:
			count+=1
	print(count)
else:
	print(0)
