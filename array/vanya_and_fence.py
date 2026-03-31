a,b=map(int,input().split())

man=list(map(int,input().split()))

for i in range(a):
    if(man[i]>b):
        man[i]=2
    else:
        man[i]=1

print(sum(man))
