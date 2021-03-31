def checkLucky(n):
	n=set(str(n))
	if len(n)==1 and ("4" in n or "7" in n):
		return(True)
	if len(n)==2 and "4" in n and "7" in n:
		return(True)
	return(False)

n=int(input())

for i in range(1,n+1):
	if checkLucky(i) and n%i==0:
		print("YES")
		break
else:
	print("NO")





