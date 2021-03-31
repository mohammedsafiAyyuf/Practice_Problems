n=int(input())
array=list(map(int,input().split()))

start=None
end=0
for i in range(n-1):
	if array[i]>array[i+1]:
		end=i+1
		if start==None:
			start=i
	elif start:
		break

if sorted(array)==array:
	print("yes")
	print(1,1)
elif sorted(array)==array[:start]+array[start:end+1][::-1]+array[end+1:]:
	print("yes")
	print(start+1,end+1)
else:
	print("no")
