"""
    Calculate the discriminant and roots of quadratic equations1
"""
import math

# a=.8**2
# b=-(2*.8*400.5+.2*.8*2.33*2.33)
# c=400.5**2

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

d=b*b-4*a*c
x=(-b-math.sqrt(d))/(2*a)
y=(-b+math.sqrt(d))/(2*a)

print(f"{a}x*x + {b}x + {c} = 0")

print(f"Discriminant = {d}")

if 0<d:
    print("0 < D")
elif d==0:
    print("D = 0")
else:
    print("0 < D")

print(f"x = ({x}, {y})")

# print((400.5-.8*x)/math.sqrt(x*.2*.8))
# print((400.5-.8*y)/math.sqrt(y*.2*.8))

# y=475
# print(y)
# print((400.5-.8*y)/math.sqrt(y*.2*.8))
# y=476
# print(y)
# print((400.5-.8*y)/math.sqrt(y*.2*.8))
# y=474
# print(y)
# print((400.5-.8*y)/math.sqrt(y*.2*.8))
