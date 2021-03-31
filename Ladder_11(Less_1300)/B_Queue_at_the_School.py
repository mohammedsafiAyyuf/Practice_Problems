def awakwardFinder(queue):
	awakwardIndex=[]
	for i in range(len(queue)-1):
		if queue[i]=="B" and queue[i+1]=="G":
			awakwardIndex.append([i,i+1])
	return(awakwardIndex)

n,t=list(map(int,input().split()))
queue=[i for i in input()]
while t:
	awakwardIndex=awakwardFinder(queue)
	for i in awakwardIndex:
		queue[i[0]],queue[i[1]]=queue[i[1]],queue[i[0]]
	t-=1
print("".join(queue))