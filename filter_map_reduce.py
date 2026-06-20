from functools import reduce
l=[55,22,7,88,4,6,105,889]
l_even=list(filter(lambda n:n%2==0,l))
print(l_even)

l_map=list(map(lambda n:n+5,l_even))
print(l_map)

re=reduce(lambda a,b:a+b,l_map)
print(re)

