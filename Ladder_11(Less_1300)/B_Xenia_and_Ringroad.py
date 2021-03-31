n,m=list(map(int,input().split()))
curHouse=1
moves=0
for i in list(map(int,input().split())):
	if i>=curHouse:
		moves+=i-curHouse
	else:
		moves+=n-curHouse+i
	#print(i,curHouse,moves)
	curHouse=i
print(moves)
