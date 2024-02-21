n=int(input())
k=0
for i in range(3,n+1,2):
    k=k+(1/i)
    print(i,k)
print(k)

