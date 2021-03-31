n=int(input())
performance=list(map(int,input().split()))
overAllLow=performance[0]
overAllHigh=performance[0]
goodCount=0
for i in performance[1:]:
	if i>overAllHigh:
		overAllHigh=i
		goodCount+=1
	elif i<overAllLow:
		overAllLow=i
		goodCount+=1
print(goodCount)