t,Sx,Sy,Ex,Ey=list(map(int,input().split()))
string=input()
x=Ex-Sx
y=Ey-Sy
Moves={}
#print(x,y)
if x>=0:
	Moves["E"]=x
else:
	Moves["W"]=abs(x)

if y>=0:
	Moves["N"]=y
else:
	Moves["S"]=abs(y)

count=0
#print(Moves)
flag=0
for i in string:
	if any(Moves.values()):
		count+=1
		if i in Moves:
			Moves[i]-=1 if Moves[i]>0 else 0

	else:
		break

if any(Moves.values()):
	print(-1)
else:
	print(count)