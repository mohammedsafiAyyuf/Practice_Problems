ans=0
n=int(input())+1
array=sum(list(map(int,input().split())))%n
#print(array,n)
#ans+=1 if array!=1 else 0
for i in range(1,6):
	#print(array,array+i,i)
	if (array+i)%n != 1:
		ans+=1
print(ans)

