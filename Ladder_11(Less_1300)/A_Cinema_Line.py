n=int(input())
ticket=list(map(int,input().split()))
money_25=0
money_50=0
for i in ticket:
	if i==25:
		money_25+=1
	elif i==50:
		if money_25>0:
			money_25-=1
			money_50+=1
		else:
			print("NO")
			break

	elif i==100:
		if money_50>0 and money_25>0:
			money_50-=1
			money_25-=1
		elif money_25>=3:
			money_25-=3
		else:
			print("NO")
			break
else:
	print("YES")