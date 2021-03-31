x,y=list(map(int,input().split()))
n=int(input())
array=[x,y]
for i in range(2,6):
	array.append(array[-1]-array[-2])
#print(array,array[(n%6)-1],(n%6)-1)
print(array[(n%6)-1]%(10**9+7))