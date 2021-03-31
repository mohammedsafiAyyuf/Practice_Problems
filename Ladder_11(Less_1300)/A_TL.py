n,m=list(map(int,input().split()))
correct=list(map(int,input().split()))
wrong=list(map(int,input().split()))
correct.sort()
wrong.sort()
TL=correct[0]
if TL*2>correct[-1]:
	TL=TL*2
else:
	TL=correct[-1]
#print(correct,wrong,TL)
if TL<wrong[0]:
	print(TL)
else:
	print(-1)

