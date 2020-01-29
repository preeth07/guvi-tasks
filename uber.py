mydict = {"ramapuram":5,"avadi":2,"kattupakkam":3,"porur":4,"poonamalle":1}
price = 15
source = input("Enter Starting Place")
destination = input("Enter Destination Place")
distance = abs(mydict[source]-mydict[destination])
bill = distance*price
print("Amount is rs.",bill)
