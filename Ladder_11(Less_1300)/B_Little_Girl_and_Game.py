from collections import Counter
string=Counter(input())
odd=0
for i in string.values():
	if i%2!=0:
		odd+=1

odd-=1 if odd>0 else 0
if odd%2==0:
	print("First")
else:
	print("Second")