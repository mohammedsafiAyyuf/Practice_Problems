n=int(input())
HashTable={}
Min=float('inf')
Max=-float('inf')
for i in range(n):
	a,b=list(map(int,input().split()))
	HashTable[(a,b)]=i+1
	Min=min(Min,a)
	Max=max(Max,b)
try:
	print(HashTable[(Min,Max)])
except Exception:
	print(-1)
