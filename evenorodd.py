n1=int(input("enter the n1 value"))
even=[]
odd=[]
def evenodd(n1):
    if(n1%2==0):
        even.append(n1)
    else:
        odd.append(n1)
    return n1
print(evenodd(n1))
print(even)
print(odd)