import math
def fiboToNumber(fib):
    if fib<=0:
        return(0)
    n = 2.078087 * math.log(fib) + 1.672276
    return round(n)

def numberToFibo(n):
	if n<=0:
		return(0)
	PHI = (1 + math.sqrt(5)) / 2
	return int(PHI ** n / math.sqrt(5) + 0.5)

fib=int(input())
n=fiboToNumber(fib)
print(*(0,numberToFibo(n-1),numberToFibo(n-2)))