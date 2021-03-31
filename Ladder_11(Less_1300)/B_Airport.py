import heapq
n,m=list(map(int,input().split()))
array=list(map(int,input().split()))

minHeap=array
heapq.heapify(minHeap)

maxHeap=[-1*i for i in array]
heapq.heapify(maxHeap)

minProfit=0
maxProfit=0
#print(minHeap,maxHeap)
for i in range(n):
	minTicket=heapq.heappop(minHeap)
	minProfit+=minTicket
	minTicket-=1
	if minTicket!=0:
		heapq.heappush(minHeap,minTicket)

	maxTicket=-1*heapq.heappop(maxHeap)
	maxProfit+=maxTicket
	maxTicket-=1
	if maxTicket!=0:
		heapq.heappush(maxHeap,-1*maxTicket)
	#print("min->",minHeap,minTicket,minProfit)
	#print("max->",maxHeap,maxTicket,maxProfit)
print(maxProfit,minProfit)