b,r=map(int,input("Enter upper limit: ").split(" "))
for a in range(b,r):
    k=0
    for i in range(2,a):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)
