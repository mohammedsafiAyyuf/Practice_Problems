n=int(input())
pattern=[[0],[0,1,0]]
for i in range(2,n+1):
	pattern.append([0]+[i+1 for i in pattern[-1]]+[0])

ans=[]
for i in pattern:
	ans.append(" ".join([" " for _ in range(n-len(i)//2)]+[str(x) for x in i]))
ans=ans+ans[::-1][1:]
for i in ans:
	print(i.rjust(n*2+1-len(i)))
