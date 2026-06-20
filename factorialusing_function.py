def fact(n):
    if n==0:
        return 1
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
        return f

a=int(input("Enter First Number"))
result=fact(a)
print(result)
