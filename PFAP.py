n=int(input("enter :"))
j=[int(x) for x in str(n)]
k,l,m=0,1,[]
for i in j:#Armstrong number
    k+=i*i*i
for i in range(2,n):#Perfect number
    if(n%i==0):
        l+=i
for i in range(1,n+1):#Factors of a number
    if(n%i==0):
        m.append(i)
for i in range(2,n):#Prime number
    if(n%i==0):
        print("not prime")
        break
else:
    print("prime")
if True:
    print("Factors of number of:",m)
if(n==k):
    print("armstrong number is:",n)
if(n==l):
    print("perfect number is :",n)
if(n!=k):
    print("Given number is not armstrong number:",n)
if(n!=l):
    print("Given number is not Perfect number:",n)
    
    


          
    
        




