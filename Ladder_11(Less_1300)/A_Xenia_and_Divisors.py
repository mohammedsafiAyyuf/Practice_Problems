n=int(input())
array=list(map(int,input().split()))
oneCount=array.count(1)
twoCount=array.count(2)
threeCount=array.count(3)
fourCount=array.count(4)
sixCount=array.count(6)
splitCount=n//3
#print(oneCount,twoCount,threeCount,fourCount,sixCount,splitCount)
if oneCount!=splitCount or threeCount>sixCount or twoCount+threeCount!=fourCount+sixCount or oneCount+twoCount+threeCount+fourCount+sixCount!=n:
	print(-1)
else:
	ans=[]
	for i in range(splitCount):
		if threeCount>0:
			ans.append([1,3,6])
			threeCount-=1
			sixCount-=1
		else:
			if fourCount>0:
				ans.append([1,2,4])
				fourCount-=1
				twoCount-=1
			else:
				ans.append([1,2,6])
				sixCount-=1
				twoCount-=1


	[print(*i) for i in ans]
