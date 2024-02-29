#ex 1
def ounces(x):
    print( x * 28.3495231)


a = float(input())
ounces(a)

#ex 2
def Celcium(x):
    c = (5 / 9) * (x - 32)
    print(c)

x = int(input())
Celcium(x)

#ex3
def solve(num_heads, num_legs):
  chickens = (2 * num_legs - 4 * num_heads) // 2
  rabbits = num_heads - chickens

  if chickens >= 0 and rabbits >= 0:
    return chickens, rabbits
  else:
    return None

num_heads = int(input())
num_legs = int(input())

solution = solve(num_heads, num_legs)

if solution is None:
  print("No solution found.")
else:
  chickens, rabbits = solution
  print(f"Number of chickens: {chickens}")
  print(f"Number of rabbits: {rabbits}")

#ex4

def is_prime(n):
    if n > 1:
        for i in range(2 , int(n/2) + 1):
            if (n % i) == 0:
                return False
        else: return True
    else: return False

x = (1,3,4,5,16,34,13,19,5,31,70)
l = int(len(x))
for i in range(l):
    if(is_prime(x[i])):
        print(x[i])
        
#ex5
from itertools import permutations 

s = str(input())
perm = permutations(s)

for i in list(perm):
  print(i)

#ex6

def rev(s):
  rev_s = s[::-1]
  print(rev_s)


s = str(input())
rev(s)

#ex7
import math

def vol(r):
  v = 4/3*(math.pi)*(r**3)
  print(v)
  
r = int(input())
vol(r)
  
#ex8
def isPalindrome(s):
  if s == s[::-1]:
    return True
  return False
    
s = str(input())
if isPalindrome(s):
  print("Yes")
else: 
  print("No")
  
#ex9
def histogram(x):
  for i in range(len(x)):
    print("*" * x[i])
    
x = ([4,9,7])
histogram(x)

#ex10
import random
print(random.randrange(1,20))
  