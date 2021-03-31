from collections import defaultdict
n,k=list(map(int,input().split()))
resultTable=defaultdict(list)
for _ in range(n):
	probCount,penalty=list(map(int,input().split()))
	resultTable[probCount].append(penalty)
for i in resultTable:
	resultTable[i].sort()
ans=[]
#idx=1
for i in sorted(resultTable,reverse=True):
	#print(idx," -> ",i,resultTable[i])
	#idx+=1
	[ans.append([i,resultTable[i][j]]) for j in range(len(resultTable[i]))]
#print(ans)
print(resultTable[ans[k-1][0]].count(ans[k-1][1]))

