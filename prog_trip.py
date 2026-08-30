k=int(input("enter amount"))
p=int(input("enter people"))
t=int(input("enter ticket price"))
r=int(input("enter room price"))
d=int(input("enter days"))
f=int(input("enter food amount"))
extra=int(input("enter expenses"))
exp=(p*(k+t)+f)
stay=r*d
trip=stay+exp
print("total spending is",trip)
