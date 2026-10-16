
import customtkinter as ctk
import sympy as sp
from methods.bisection import bisection

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class NumericalMethodsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Numerical Methods Solver")
        self.geometry("950x700")
        self.minsize(750, 600)

        title = ctk.CTkLabel(
            self,
            text="Numerical Methods Solver",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        ctk.CTkLabel(
            self,
            text="Equation (example: x**2 - 4)"
        ).pack(pady=(10, 5))

        self.equation_entry = ctk.CTkEntry(
            self, width=400, placeholder_text="x**2 - 4"
        )
        self.equation_entry.pack(pady=5)

        # Interval inputs
        inputs = ctk.CTkFrame(self)
        inputs.pack(pady=15)

        self.a_entry = ctk.CTkEntry(
            inputs, width=130, placeholder_text="a = 0"
        )
        self.a_entry.grid(row=0, column=0, padx=8, pady=10)

        self.b_entry = ctk.CTkEntry(
            inputs, width=130, placeholder_text="b = 3"
        )
        self.b_entry.grid(row=0, column=1, padx=8, pady=10)

        self.tol_entry = ctk.CTkEntry(
            inputs, width=150, placeholder_text="Error = 0.0001"
        )
        self.tol_entry.grid(row=0, column=2, padx=8, pady=10)

        ctk.CTkLabel(
            self,
            text="Method: Bisection Method",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        ctk.CTkButton(
            self,
            text="Solve",
            command=self.solve,
            width=180
        ).pack(pady=12)

        self.result_label = ctk.CTkLabel(
            self,
            text="Result will appear here",
            font=("Arial", 16, "bold")
        )
        self.result_label.pack(pady=10)

        ctk.CTkLabel(
            self,
            text="Iteration Table",
            font=("Arial", 18, "bold")
        ).pack(pady=5)

        self.table = ctk.CTkTextbox(
            self, width=850, height=250
        )
        self.table.pack(padx=20, pady=(5, 20), fill="both", expand=True)

    def solve(self):
        try:
            equation = self.equation_entry.get().strip()
            if not equation:
                raise ValueError("Please enter an equation.")

            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            tolerance = float(self.tol_entry.get())

            if tolerance <= 0:
                raise ValueError("Error must be greater than zero.")

            x = sp.Symbol("x")
            expr = sp.sympify(equation)
            f = sp.lambdify(x, expr, modules=["math"])

            root, rows = bisection(
                f, a, b, tolerance=tolerance
            )

            self.result_label.configure(
                text=f"Approximate root: {root:.8f}"
            )

            self.table.delete("1.0", "end")
            self.table.insert(
                "end",
                f"{'Iteration':<12}{'a':<15}{'b':<15}"
                f"{'c':<15}{'f(c)':<15}\n"
            )
            self.table.insert("end", "-" * 70 + "\n")

            for row in rows:
                self.table.insert(
                    "end",
                    f"{row['Iteration']:<12}"
                    f"{row['a']:<15.6f}"
                    f"{row['b']:<15.6f}"
                    f"{row['c']:<15.6f}"
                    f"{row['f(c)']:<15.6f}\n"
                )

        except Exception as error:
            self.result_label.configure(
                text=f"Error: {error}"
            )
            self.table.delete("1.0", "end")


if __name__ == "__main__":
    app = NumericalMethodsApp()
    app.mainloop()
