#5
a=int(input("fresh loaves"))
b=int(input("day old leaves"))
print("Regular prce : Rs.185.00")
fresh_amount = 185*float(a)
old_amount = (185*0.4)*float(b)
Total = fresh_amount+old_amount
print("Amount of new loaves:Rs ",fresh_amount)
print("Amount of day old loaves:Rs ",old_amount)
print("Total amount: Rs",Total)
