x=[1,3,2,2.5,5,.1]

for theta in x:
    Ln = 1
    for i in x:
        if i<=theta:
            Ln*=(1/theta)
    print(f"{theta}: {Ln}")