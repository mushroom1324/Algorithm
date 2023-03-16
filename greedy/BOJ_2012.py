N=int(input())
L=list(int(input())for _ in range(N))
L.sort()
d=0
for i in range(N):
    d+=abs(L[i]-i-1)
print(d)

"""
what the shit is this .. ? 

_,*l=map(int,open(0))
print(sum(abs(x-i-1)for i,x in enumerate(sorted(l))))

"""


