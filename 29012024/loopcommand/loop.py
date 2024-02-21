#how to use loop
#for i in range(start,end,step): *note: i always start from 0
#example:
#a=int(input())
#for i in range(1,a+1):
    #print(i)
for i in range (1,11):
    print(i)

for i in range(10,0,-1):
    print(i)

for i in range (1,101,2):
    print(i)

for i in range (1,101):
    if i%2==0:
        print(i)

for i in range (1,101):
    if i%3==0:
        print(i)

a=int(input())
for i in range (1,11):
    a=a+a/10
    print(a)
