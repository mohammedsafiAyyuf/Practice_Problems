magNum=input()
idx=0
while idx<len(magNum):
	#print(idx,magNum[idx])
	if magNum[idx]=='4':
		print("NO")
		break
	elif magNum[idx]=='1':
		if idx+1<len(magNum):
			if magNum[idx+1]=='1':
				idx+=1
			elif magNum[idx+1]=='4':
				if idx+2<len(magNum):
					if magNum[idx+2]=='1':
						pass
					elif magNum[idx+2]=='4':
						idx+=1
				idx+=2
			else:
				idx+=1
		else:
			idx+=1
	else:
		print("NO")
		break


else:
	print("YES")