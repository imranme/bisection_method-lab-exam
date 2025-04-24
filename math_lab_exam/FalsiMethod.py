# Step-01: Define the function f(x)
def f(x):
    return x**3 - x - 2  # তুমি চাইলে এই ফাংশন বদলাতে পারো

# Step-02 & Step-03: Read lower and upper bounds
a = 1
b = 2

# Step-04: Set k = 1
k = 1

# Step-05 to Step-12
while True:
    # Step-05: Calculate xk using Regula Falsi formula
    xk = (a * f(b) - b * f(a)) / (f(b) - f(a))

    # Step-06: Calculate fk
    fk = f(xk)

    # Step-07: Print current values
    print(f"Step-{k+6:02}: ধাপ {k}, xk = {xk}, f(xk) = {fk}")

    # Step-08: Check for convergence
    if abs(fk) <= 0.0001:
        print(f"\nStep-11: চূড়ান্ত রুট ≈ {xk}")
        break
    elif f(xk) * f(b) < 0:
        a = xk  # Step-08
    elif f(a) * fk < 0:
        b = xk  # Step-08

    # Step-09: Increment k
    k += 1

    # Step-10: Loop continues



#     clen code, def f(x):
#     return x**3 - x - 2  # ফাংশন পরিবর্তন করতে চাইলে এখানে করো

# def regula_falsi(a, b, tol=0.0001):
#     k = 1  # iteration শুরু

#     while True:
#         xk = (a * f(b) - b * f(a)) / (f(b) - f(a))  # সূত্র অনুসারে xk নির্ণয়
#         fk = f(xk)

#         print(f"Iteration {k}: xk = {xk:.6f}, f(xk) = {fk:.6f}")

#         if abs(fk) <= tol:
#             print(f"\nEstimated root: {xk:.6f}")
#             break

#         if f(xk) * f(b) < 0:
#             a = xk
#         else:
#             b = xk

#         k += 1

# # উদাহরণ রান
# regula_falsi(1, 2)

