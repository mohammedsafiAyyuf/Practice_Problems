n=int(input())
array=sum(list(map(int,input().split())))
if array%n==0:
	print(n)
else:
	print(n-1)
