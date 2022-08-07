# Given a three-digit number. Find the sum of its digits.
num=int(input())
a=num%10
b=(num//10)%10
c=num//100
print(a+b+c)