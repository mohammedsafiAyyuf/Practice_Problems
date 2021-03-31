n=int(input())
array=list(map(int,input().split()))
array.sort()
moves=0
for i in range(1,n+1):
	moves+=abs(i-array[i-1])
print(moves)

