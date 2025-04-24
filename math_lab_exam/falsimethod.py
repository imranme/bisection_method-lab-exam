# def f(x):
#     return x**3 - x - 2  # তুমি চাইলে ফাংশন পাল্টাতে পারো

# def bisection(a, b, tol=1e-4):
#     k = 1
#     while True:
#         x = (a + b) / 2
#         fx = f(x)
#         print(f"Iter {k}: x = {x}, f(x) = {fx}")
#         if abs(fx) <= tol or (b - a)/2 < tol:
#             print(f"Root ≈ {x}")
#             return x
#         if f(a) * fx < 0:
#             b = x
#         else:
#             a = x
#         k += 1

# # উদাহরণ:
# bisection(1, 2)


# output: Iter 1: x = 1.5, f(x) = -0.125
# Iter 2: x = 1.75, f(x) = 1.609375
# Iter 3: x = 1.625, f(x) = 0.666015625
# Iter 4: x = 1.5625, f(x) = 0.252197265625
# Iter 5: x = 1.53125, f(x) = 0.059112548828125
# Iter 6: x = 1.515625, f(x) = -0.034053802490234375
# Iter 7: x = 1.5234375, f(x) = 0.012250423431396484
# Iter 8: x = 1.51953125, f(x) = -0.010971248149871826
# Iter 9: x = 1.521484375, f(x) = 0.0006221756339073181
# Iter 10: x = 1.5205078125, f(x) = -0.005178886465728283
# Iter 11: x = 1.52099609375, f(x) = -0.002279443317092955
# Iter 12: x = 1.521240234375, f(x) = -0.0008289058605441824
# Iter 13: x = 1.5213623046875, f(x) = -0.0001034331235132413
# Iter 14: x = 1.52142333984375, f(x) = 0.0002593542519662151
# Root ≈ 1.52142333984375


# Step-01: Define f(x)
def f(x):
    return x**3 - x - 2

# Step-02 & 03: Read a, b
a = 1  # Lower bound
b = 2  # Upper bound

# Step-04: Set k = 1
k = 1

# Step-05 to Step-12
while True:
    # Step-05: Calculate xk
    xk = (a + b) / 2

    # Step-06: Calculate fk
    fk = f(xk)

    # Step-07: Print k, xk, fk
    print(f"Step-{k+6:02}: k = {k}, xk = {xk}, f(xk) = {fk}")

    # Step-08: Check convergence
    if abs(fk) <= 0.0001:
        # Step-11: Print result
        print(f"Step-11: প্রাপ্ত রুট = {xk}")
        break

    # Step-08 continued: Update bounds
    if f(xk) * f(b) < 0:
        a = xk
    elif f(a) * fk < 0:
        b = xk

    # Step-09: k = k + 1
    k += 1

    # Step-10: Go to Step-05 (loop continues)

# Step-12: Stop (loop ends)


