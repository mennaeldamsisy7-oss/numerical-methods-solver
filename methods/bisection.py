
def bisection(f, a, b, tolerance=0.0001, max_iterations=100):
    """
    Find a root of f(x) using the Bisection Method.
    Returns the approximate root and an iteration table.
    """

    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a, [{"Iteration": 0, "a": a, "b": b, "c": a, "f(c)": 0.0}]

    if fb == 0:
        return b, [{"Iteration": 0, "a": a, "b": b, "c": b, "f(c)": 0.0}]

    if fa * fb > 0:
        raise ValueError(
            "The function must have opposite signs at a and b."
        )

    table = []
    root = None

    for iteration in range(1, max_iterations + 1):
        c = (a + b) / 2
        fc = f(c)

        table.append({
            "Iteration": iteration,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc
        })

        root = c

        if abs(fc) < tolerance or (b - a) / 2 < tolerance:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return root, table
