v=[]
b=int(input("Number of Elements:"))
for i in range(1,b+1):
    c=int(input(" "))
    v.append(c)
print("Median Element is:",v[int((b-1)/2)])
