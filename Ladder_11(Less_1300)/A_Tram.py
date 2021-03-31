n=int(input())
curPeopleInsideTrain=0
maxPeropleInsideTrain=0

for idx in range(n):
	exit,entry=list(map(int,input().split()))
	curPeopleInsideTrain+=entry-exit
	maxPeropleInsideTrain=max(maxPeropleInsideTrain,curPeopleInsideTrain)
print(maxPeropleInsideTrain)