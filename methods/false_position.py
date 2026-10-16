
def false_position(f, a, b, tolerance=0.0001, max_iterations=100):
    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a, []

    if fb == 0:
        return b, []

    if fa * fb > 0:
        raise ValueError(
            "The function must have opposite signs at a and b."
        )

    table = []
    root = None

    for iteration in range(1, max_iterations + 1):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        table.append({
            "Iteration": iteration,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc
        })

        root = c

        if abs(fc) < tolerance:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return root, table
