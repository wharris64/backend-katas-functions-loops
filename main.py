def add(x,y):
    n3 = 0
    n3 = x + y
    return n3
add(2, 4)

def multiply(x,y):
  var1 = 0
  for i in range (1, y + 1):
    var1 = add(var1, x)
  return var1
multiply(6,8)
  

def power(x,n):
  prod = x
  for i in range(1, n):
    prod = multiply(prod, x)
  return prod

power(2, 8)


def factorial(x):
  sum = 1
  for i in range(1, x + 1):
    sum = multiply(i, sum)  
  return sum      

factorial(4)


def fibonacci(n):
        a = 0
        b = 1
        if n < 0:
                result = "whaaaaat"
        elif n == 0:
                a = 0
                result = 0
        elif n == 1:
                b = 1
                result = 1
        else:
                for i in range(2,n):
                        c = add(a,b)
                        a = b
                        b = c
        return c



print(add(2,4))
print(multiply(6,8))
print(power(2, 8))
print(factorial(4))
print(fibonacci(8))