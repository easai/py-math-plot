prod = 1
sum = 0
for i in range(0,110):
    if 0<i:
        prod *= i
    PiB = 90**i/prod
    sum += PiB
    ans = PiB / sum
    if 90<i:
        print(f"{i}: {ans}")
