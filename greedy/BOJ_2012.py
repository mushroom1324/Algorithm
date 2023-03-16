N=int(input())
a=[0]*N
for i in range(N):
    a[i]=int(input())
a.sort()
d=0
for i in range(N):
    d+=abs(a[i]-i-1)
print(d)