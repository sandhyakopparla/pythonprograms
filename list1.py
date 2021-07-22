n1=int(input("enter the n1"))
n2=int(input("enter the n2"))
large=[]
small=[]
def compare(n1,n2):
    if(n1>n2):
        large.append(n1)
        small.append(n2)
    else:
        small.append(n2)
        large.append(n1)
    return small,large
print(compare(n1,n2))
