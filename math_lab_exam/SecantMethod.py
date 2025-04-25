def f(x):
    # Define the function f(x) = x^3 - x - 2
    return x**3 - x - 2

def secant_method(x1, x0, tol=0.0001):
    k = 1  # Iteration counter
    xk = x1  # Current estimate of the root
    f_xk = f(xk)
    f_x1 = f(x1)
    f_x0 = f(x0)

    # Start the loop for the Secant method
    while abs(xk - x1) > tol:
        # Apply the Secant method formula
        xk = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        f_xk = f(xk)

        # Print the current iteration results
        print(f"Iteration {k}: xk = {xk}, f(xk) = {f_xk}")

        # Update values for the next iteration
        x0 = x1
        x1 = xk
        f_x0 = f_x1
        f_x1 = f_xk

        # Increment the iteration counter
        k += 1

    # After convergence
    print(f"The required root is: {xk}")
    return xk

# Example usage with initial guesses x1 = 1, x0 = 2
x1 = 1
x0 = 2
secant_method(x1, x0)


# newtonsForwardInterpolation.js
def divided_difference(x, y):
    n = len(x)
    D = [[0 for _ in range(n)] for _ in range(n)]

    # First column is y values
    for i in range(n):
        D[i][0] = y[i]

    # Compute divided differences
    for j in range(1, n):
        for i in range(n - j):
            D[i][j] = (D[i + 1][j - 1] - D[i][j - 1]) / (x[i + j] - x[i])

    return D

def newtons_forward_interpolation(x, y, xp):
    n = len(x)
    D = divided_difference(x, y)

    h = x[1] - x[0]  # Step size (assuming equal spacing)
    p = (xp - x[0]) / h  # Scaled difference

    sum_interp = y[0]  # Start with the first function value
    prod = 1  # Product term

    # Calculate interpolation using Newton's forward formula
    for i in range(1, n):
        prod *= (p - (i - 1))
        sum_interp += prod * D[0][i]

    return sum_interp

# Example data
x = [0, 1, 2, 3, 4]
y = [1, 2, 4, 8, 16]
xp = 2.5

# Interpolate and print result
result = newtons_forward_interpolation(x, y, xp)
print(f"The interpolated value at x = {xp} is: {result}")

# newtonRaphsonMethod
def f(x):
    # Define the function f(x) = x^3 - x - 2
    return x**3 - x - 2

def df(x):
    # Derivative of the function: f'(x) = 3x^2 - 1
    return 3 * x**2 - 1

def newton_raphson_method(x0, tol=0.0001, max_iter=100):
    k = 1  # Iteration counter
    xk = x0
    fxk = f(xk)
    dfxk = df(xk)

    # Start the loop for Newton-Raphson method
    while abs(fxk) > tol and k <= max_iter:
        xk = xk - fxk / dfxk
        fxk = f(xk)
        dfxk = df(xk)

        # Print the current iteration results
        print(f"Iteration {k}: xk = {xk}, f(xk) = {fxk}")
        k += 1

    # After convergence or max iterations
    if abs(fxk) <= tol:
        print(f"The required root is: {xk}")
    else:
        print("The method did not converge within the maximum iterations.")

    return xk

# Example usage with initial guess x0 = 1.5
x0 = 1.5
newton_raphson_method(x0)
