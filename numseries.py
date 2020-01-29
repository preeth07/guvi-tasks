num = int(input("enter a range"))

def even(x):
    return x%2 == 0
def odd(x):
    return x%2 != 0

n = filter(even,(list(range(num))))
m = filter(odd,(list(range(num))))

print("even no",list(n))
print("odd no",list(m))

   

