sum = 0
for i in range(1,100000):
    sum+=i*.5*.5**(i-1)
print("k = "+str(sum))

sum = 0
for i in range(1,100000):
    sum+=i*i*.5*.5**(i-1)
print("k*k = "+str(sum))

sum = 0
for i in range(1,10000):
    sum+=i**3*.5*.5**(i-1)
print("k**3 = "+str(sum))
