from collections import Counter
k=int(input())
string=Counter(input())
ans=""
for i in string:
	if string[i]%k==0:
		ans+=i*(string[i]//k)
	else:
		print(-1)
		break
else:
	print(ans*k)