import numpy as np
import matplotlib.pyplot as plt

def display_menu():
    print("\nFunction Plotter Menu")
    print("1. Plot a single function")
    print("2. Plot multiple functions on the same graph")
    print("3. Customize plot style")
    print("4. Save plot to file")
    print("5. Exit")

def get_function_input():
    print("\nChoose a predefined function or enter a custom one:")
    print("1. y = np.sin(x)")
    print("2. y = x**2")
    print("3. y = np.exp(x)")
    print("4. y = np.log(x + 1) (Valid for x > -1)")
    print("5. y = piecewise function: x**2 for x < 0, np.sin(x) for x >= 0")
    print("6. Enter your custom function") 

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        return "np.sin(x)"
    elif choice == "2":
        return "x**2"
    elif choice == "3":
        return "np.exp(x)"
    elif choice == "4":
        return "np.log(x + 1)"  # Log is valid for x > -1
    elif choice == "5":
        return "np.piecewise(x, [x < 0, x >= 0], [lambda x: x**2, lambda x: np.sin(x)])"
    elif choice == "6":
        return input("Enter your custom function of x (e.g., np.cos(x), x**3 - 2*x): ")
    else:
        print("Invalid choice! Defaulting to y = np.sin(x).")
        return "np.sin(x)"

def get_plot_range():
    while True:
        try:
            x_min = float(input("Enter the minimum value of x: "))
            x_max = float(input("Enter the maximum value of x: "))
            num_points = int(input("Enter the number of points to plot: "))

            if x_min >= x_max:
                print("Error: x_min must be less than x_max.")
            elif num_points <= 0:
                print("Error: Number of points must be positive.")
            else:
                return x_min, x_max, num_points
        except ValueError:
            print("Error: Please enter valid numbers.")

def plot_functions(functions, x_range, styles):
    x_min, x_max, num_points = x_range
    x = np.linspace(x_min, x_max, num_points)

    plt.figure(figsize=(10, 7))
    for i, (func, style) in enumerate(zip(functions, styles)):
        try:
            y = eval(func, {"x": x, "np": np})  # Safe eval with defined variables
            plt.plot(x, y, style, label=f"y = {func}")
        except Exception as e:
            print(f"Error plotting function '{func}': {e}")

    plt.title("Function Plotter")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

def customize_styles(num_functions):
    styles = []
    for i in range(num_functions):
        print(f"\nCustomize style for function {i+1}:")
        color = input("Enter line color (e.g., 'b' for blue, 'r' for red): ") or "b"
        linestyle = input("Enter line style ('-' for solid, '--' for dashed, etc.): ") or "-"
        marker = input("Enter marker style ('o' for circle, 's' for square, etc.): ") or ""

        style = f"{color}{linestyle}{marker}".strip()
        styles.append(style)
    return styles

def save_plot(functions, x_range, styles, filename):
    x_min, x_max, num_points = x_range
    x = np.linspace(x_min, x_max, num_points)

    plt.figure(figsize=(10, 7))
    for i, (func, style) in enumerate(zip(functions, styles)):
        try:
            y = eval(func, {"x": x, "np": np})  # Safe eval
            plt.plot(x, y, style, label=f"y = {func}")
        except Exception as e:
            print(f"Error plotting function '{func}': {e}")

    plt.title("Function Plotter")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    try:
        plt.savefig(filename)
        print(f"Plot saved as {filename}")
    except Exception as e:
        print(f"Error saving plot: {e}")

def main():
    print("Welcome to the Enhanced Function Plotter!")
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nPlotting a single function:")
            func = get_function_input()
            x_range = get_plot_range()
            plot_functions([func], x_range, ["-"])
        elif choice == "2":
            print("\nPlotting multiple functions:")
            try:
                num_functions = int(input("How many functions would you like to plot? "))
                functions = [get_function_input() for _ in range(num_functions)]
                x_range = get_plot_range()
                styles = customize_styles(num_functions)
                plot_functions(functions, x_range, styles)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == "3":
            print("\nCustomizing plot styles:")
            try:
                num_functions = int(input("How many functions would you like to style? "))
                styles = customize_styles(num_functions)
                print(f"Styles set: {styles}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == "4":
            print("\nSaving plot to file:")
            try:
                num_functions = int(input("How many functions would you like to save? "))
                functions = [get_function_input() for _ in range(num_functions)]
                x_range = get_plot_range()
                styles = customize_styles(num_functions)
                filename = input("Enter the filename to save the plot (e.g., 'plot.png'): ")
                save_plot(functions, x_range, styles, filename)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()


while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == "quit":
        break  # Exits the loop
    print("You entered:", user_input)
