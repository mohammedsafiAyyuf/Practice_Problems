from itertools import permutations

def caculate(array):
	ans=0
	#Round1
	ans+=g[array[0]][array[1]]+g[array[1]][array[0]]
	ans+=g[array[2]][array[3]]+g[array[3]][array[2]]	

	#Round2
	ans+=g[array[1]][array[2]]+g[array[2]][array[1]]
	ans+=g[array[3]][array[4]]+g[array[4]][array[3]]	

	#Round2
	ans+=g[array[2]][array[3]]+g[array[3]][array[2]]

	#Round4
	ans+=g[array[3]][array[4]]+g[array[4]][array[3]]	
	return(ans)


g=[list(map(int,input().split())) for i in range(5)] 
result=0
for i in permutations([0,1,2,3,4]):
	result=max(result,caculate(i))
print(result)
