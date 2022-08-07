
"""
A cupcake costs A dollars and B cents. Determine, how many dollars and 
cents should one pay for N cupcakes. A program gets three numbers: A, B,
 N. It should print two numbers: total cost in dollars and cents.


"""
A=int(input())
B=int(input())
N=int(input())
cost=N*(100*A+B)
print(cost//100 ,cost%100)