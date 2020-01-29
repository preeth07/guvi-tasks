import random

n = int(input("enter number btwn 0 - 9 "))
r = random.randrange(0,9) 
print("Random no",r)
print("Guessed no",n)

if(n == r):
    print("Sucess")
else:
    print("Failed")



              
