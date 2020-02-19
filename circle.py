a=int(input('do you want to continue?(0,1)'))
if a==0:
    print("operation cancelled")
elif a==1:
    b = int(input("radius:"))
    if b<0:
        print("radius is negative")
    else:
        print("circumference:",2*b*22/7)
        print("area:",4*22/7*b**2)
while a=1:
    print(a)
    a +=1

