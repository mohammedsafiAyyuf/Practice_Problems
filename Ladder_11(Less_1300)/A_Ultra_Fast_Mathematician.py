num1=input()
num2=input()
ans=""
for idx in range(len(num1)):
	ans+=str(int(num1[idx])^int(num2[idx]))
print(ans)