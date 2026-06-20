def is_even(n):
    return n%2==0

print(is_even(7))
'''
lambda arguments : expression
'''
f=lambda n:n%2==0
print(f(56))

f2=lambda a,b:a+b
print(f2(55,56))

'''A lambda function in Python is a 
small, anonymous function that is 
defined without a name and contained 
entirely within a single line of code.
 Unlike a standard function defined
  with the def keyword, a lambda 
  function can execute only one 
  single expression and returns
   the resulting value 
   automatically without 
   requiring a return statement.
   
   '''