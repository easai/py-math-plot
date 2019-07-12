from scipy import integrate

def f(x):
    return x-1

result, err = integrate.quad(f, 0, 10)

print(f"result: {result}, err: {err}")
