n,m=list(map(int,input().split()))
array=list(map(int,input().split()))
temp=set()
suffix=[]
for i in range(n-1,-1,-1):
	temp.add(array[i])
	suffix.append(len(temp))
suffix=suffix[::-1]

for i in range(m):
	print(suffix[int(input())-1])