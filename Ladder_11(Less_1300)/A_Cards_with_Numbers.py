#Fast IO Libraries
import os
import sys
from io import BytesIO, IOBase

#Library for our use
# import math
# from collections import Counter
# from collections import defaultdict
# from collections import deque
# from bisect import bisect_left as bl, bisect_right as br
# from itertools import accumulate,permutations as perm,combinations as comb
# import heapq
# from functools import reduce
# from fractions import Fraction
# import sys


def main():
	"""
	inp= open('input.txt', 'r')
	out=open('output.txt', 'w')
	n=int(inp.readline())
	a=inp.readline().split()
	dic={}
	s=[]
	for i in range(1, 2*n+1):
	    e=int(a[i-1])
	    if not e in dic:
	        dic[e]=i
	    else:
	        s.append(str(dic[e]) +' '+str(i))
	        del(dic[e])
	if len(dic)==0:
	    out.write('\n'.join(s))
	else:
	    out.write('-1')
	out.close()
	"""
	inputFile=open("input.txt",'r')
	outputFile=open("output.txt",'w')

	n=int(inputFile.readline())
	hashTable={}
	array=inputFile.readline().split()
	ans=[]
	for idx in range(2*n):
		val=array[idx]
		if val in hashTable:
			ans.append(str(hashTable[val])+" "+str(idx+1))
			del hashTable[val]
		else:
			hashTable[val]=idx+1

	if len(hashTable)==0:
		outputFile.write("\n".join(ans))
	else:
		outputFile.write("-1")

	inputFile.close()
	outputFile.close()



# shortcut for functions
def I(): return input()

def Iint(): return int(input())

def Ilist(): return list(map(int, input().split()))   # int list

def Imap(): return map(int, input().split())   # int map

def Plist(li, s=' '): print(s.join(map(str, li)))   # non string list



# Region fastio functions

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()