n=int(input())
array=list(map(int,input().split()))
bestVal=abs(array[0]-array[-1])
bestArr=[n,1]
for i in range(n-1):
	if bestVal>abs(array[i]-array[i+1]):
		bestVal=abs(array[i]-array[i+1])
		bestArr=(i+1,i+2)
print(*bestArr)