n=int(input())
array=list(map(int,input().split()))
array.sort(reverse=True)
Total=sum(array)
curSum=0
count=0
for i in array:
	curSum+=i
	count+=1
	if curSum>(Total-curSum):
		print(count)
		break
else:
	print(count)


