n=int(input())
array=list(input())
left=sorted(array[:len(array)//2])
right=sorted(array[len(array)//2:])
check=""
flag=0
if int(left[0])>int(right[0]) :
	check="LeftBig" 
elif int(left[0])<int(right[0]):
	check="LeftSmall"
else:
	flag=1

if not flag:
	for i in range(len(array)//2):
		x=left[i]
		y=right[i]
		temp=""
		if x>y:
			temp="LeftBig"
		elif x<y:
			temp="LeftSmall"
		else:
			flag=1
			#print("its me")
			break
		if check!=temp:
			#print("Naaah")
			flag=1
			break

if flag:
	print("NO")
else:
	print("YES")