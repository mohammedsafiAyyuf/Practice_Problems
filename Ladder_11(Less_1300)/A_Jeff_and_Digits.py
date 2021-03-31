n=int(input())
array=list(map(int,input().split()))
zeroCount=array.count(0)
fiveCount=array.count(5)
if zeroCount==0:
	print(-1)
else:
	flag=0
	for i in range(fiveCount,0,-1):
		if int("5"*i+"0"*zeroCount)%90==0:
			print(int("5"*i+"0"*zeroCount))
			break
	else:
		print(0)