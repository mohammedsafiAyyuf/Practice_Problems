"""def primeSieve(n):

	sieve=[True for i in range(1299900)]
	sieve[0]=False
	sieve[1]=False
	p=2
	while p*p<=1299900:
		if sieve[p]==True:
			for i in range(p*p,1299900,p):
				sieve[i]=False
		p+=1
	prime=[idx for idx,val in enumerate(sieve) if val]
	return(prime[:n])

"""

n=int(input())
print(*[(10**6)+i for i in range(n)])