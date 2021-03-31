n=int(input())
string=input()

if len(set(string))==1:
	print(len(string)-1)
else:
	stack=[]
	prev=string[0]
	count=1
	for i in string[1:]:
		if i==prev:
			count+=1
		else:
			stack.append(count)
			prev=i
			count=1
	stack.append(count)
	ans=0
	for val in stack:
		ans+=val-1
	print(ans)




