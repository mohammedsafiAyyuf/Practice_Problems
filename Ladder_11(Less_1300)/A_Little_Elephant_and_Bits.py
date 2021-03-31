x=int(input())
x=str(x)
ans=""
flag=0
for idx,val in enumerate(x):
	if val!='0':
		ans+=val
	else:
		flag=1
		break
if flag==1:
	print(ans,end="")
	print(x[idx+1:])

else:
	print(x[:-1])
