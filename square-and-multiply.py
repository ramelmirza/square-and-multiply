"""
Author: Ramel Mirza
Date: 09-19-2024
Description: This script was created for the students at Mohawk College who are taking Discrete Mathematics and Statistics from Mrs. Stojanovska-Pocuca. It acts as a guide to help aid students when studying the square and multiply algorithm.
Version: 1.01
"""
import math
import tkinter as tk
from tkinter import ttk


class GUIApplication(tk.Tk):
    """
    This class creates the widgets and also manages the event handling
    """

    def __init__(self):
        """
        Constructor for the widgets (mainly to avoid reference errors)
        """
        super().__init__()
        # placeholders
        self.header = None
        self.header_2 = None
        self.header_3 = None
        self.base_label = None
        self.exponent_label = None
        self.modulo_label = None
        self.base = None
        self.exponent = None
        self.modulo = None
        self.button = None
        self.output = None
        self.error = None
        self.title("The Square and Multiply Algorithm Calculator")
        self.create_widgets()
        # disabling maximization
        self.resizable(width=False, height=False)

    def create_widgets(self):
        """
        This function creates the calculate button, base, exponent, and modulo text areas, and an output box to hold the steps for completing the square and multiply algorithm
        """

        # style 1 for the title
        style_1 = ttk.Style()
        style_1.configure("First.TLabel", font=("Comic Sans MS", 18, "underline", "bold"))

        # style 2 for the creds
        style_2 = ttk.Style()
        style_2.configure("Second.TLabel", font=("Comic Sans MS", 10, "italic", "bold"))

        # style 3 for the info
        style_3 = ttk.Style()
        style_3.configure("Third.TLabel", font=("Comic Sans MS", 10, "italic", "bold"))

        # creating a 'banner'
        canvas = tk.Canvas(self, width=800, height=100)  # 1/8 of the page
        canvas.pack()
        canvas.create_rectangle(0, 0, 800, 100, outline="black", fill="black")

        # header styling and placement
        self.header = ttk.Label(self, text="Square and Multiply Calculator", style="First.TLabel", foreground="#660033",
                                background="black")
        self.header.place(x=220, y=2)

        bullet_point = '\u2022'

        self.header_2 = ttk.Label(self,
                                  text=f"{bullet_point}You can use this as a study helper; input the base, exponent, and modulo - it will solve the steps for you!",
                                  style="Second.TLabel", foreground="#990033", background="black")
        self.header_2.place(x=50, y=40)

        self.header_3 = ttk.Label(self,
                                  text=f"{bullet_point}Curated for Mrs. Stojanovska-Pocuca and her lovely students. ",
                                  style="Third.TLabel", foreground="#ff9933", background="black")
        self.header_3.place(x=210, y=65)

        bem_style = ttk.Style()
        bem_style.configure("Fourth.TLabel", font=("Comic Sans MS", 14, "bold", "italic"))
        # base
        self.base_label = ttk.Label(self, text="Base", style="Fourth.TLabel")
        self.base_label.pack(anchor="center")

        self.base = ttk.Entry(self, width=5)
        self.base.pack(anchor="center")
        self.base.focus()

        # exponent
        self.exponent_label = ttk.Label(self, text="Exponent", style="Fourth.TLabel")
        self.exponent_label.pack(anchor="center")
        self.exponent = ttk.Entry(self, width=5)
        self.exponent.pack(anchor="center")

        # modulo
        self.modulo_label = ttk.Label(self, text="Modulo", style="Fourth.TLabel")
        self.modulo_label.pack(anchor="center")
        self.modulo = ttk.Entry(self, width=5)
        self.modulo.pack(anchor="center")

        # calculate button
        button_style = ttk.Style()
        button_style.configure("Fifth.TButton", font=("Comic Sans MS", 13, "bold"))
        self.button = ttk.Button(self, text="Compute it!", command=self.square_and_multiply, style="Fifth.TButton")
        self.button.configure(padding=10)
        self.button.place(x=650, y=735)

        # exit button
        button_style = ttk.Style()
        button_style.configure("Fifth.TButton", font=("Comic Sans MS", 13, "bold"))
        self.button = ttk.Button(self, text="I'm done!", command=self.exit_out, style="Fifth.TButton")
        self.button.configure(padding=10)
        self.button.place(x=12, y=735)

        # steps
        steps_style = ttk.Style()
        steps_style.configure("Sixth.TLabel", font=("Comic Sans MS", 11, "bold"))
        self.output = ttk.Label(self, font = ("Comic Sans MS", 11, "bold"))
        self.output.pack(anchor="center", pady=50)

        # error label
        error_style = ttk.Style()
        error_style.configure("Seventh.TLabel", font=("Comic Sans MS", 10, "bold"))
        self.error = ttk.Label(self, text="")

    def square_and_multiply(self):
        """
        This function computes a large power of a positive base integer down to its non-zero equivalent in certain modulo (including the actual output of the answer)
        """

        try:
            b = int(self.base.get())
            e = int(self.exponent.get())
            e_print = e
            m = int(self.modulo.get())

            self.output.config(text="")

            # step 1: convert exponent to binary
            binary_str = ""
            while e > 1:

                if e % 2 == 0:
                    binary_str += '0'
                    e = e // 2
                else:
                    binary_str += '1'
                    e = e // 2

            if e == 1:
                binary_str += '1'

            binary_str_rev = binary_str[::-1]  # only to print it in the output label
            self.output.config(text = self.output.cget('text') + f"STEP 1: Convert the exponent from DNS(\u2081\u2080): {e_print} to BINARY(\u2082): {binary_str_rev}\n")

            # step 1.5: find powers of 2 that sum to b (effectively just finding 1's)
            powers_of_2_and_indices = {}
            for digit in range(0, len(binary_str)):
                if binary_str[digit] == '1':
                    powers_of_2_and_indices[int(math.pow(2, digit))] = digit
            # mapped it to a dictionary such that I get the value and the index which also happens to be the power the base is being raised to

            # now I know that 2^max_power will be the limit, I can square the numbers up until the comparison equals the math.pow() of 2 and the value max_power - which is obviously the max value of the keys of the dictionary
            max_power = max(list(powers_of_2_and_indices.keys()))
            list_of_values = list(powers_of_2_and_indices.values())
            use_powers = list(powers_of_2_and_indices.keys())

            power_expressions = [f"{b}^{key}" for key in powers_of_2_and_indices.keys()]
            self.output.config(text=self.output.cget('text') + "    " + " x ".join(power_expressions) + "\n\n")

            # step 2: solve the squares
            self.output.config(text=self.output.cget(
                'text') + f"STEP 2: Square both sides and if you can, reduce further by modulo: \n")

            list_of_completed_squares = []
            i = 0
            post = b
            post_previous = b
            self.output.config(text=self.output.cget('text') + f"    {b}^{1} mod {m} \u2261 {post}\n")
            if 1 in use_powers:
                list_of_completed_squares.append(b)
                i = 2
            else:
                i = 2
            while i <= max_power:
                post = int(math.pow(post, 2))
                post_print = post
                if post >= m:
                    post = post % m

                    self.output.config(text=self.output.cget('text') + f"    {b}^{i} \u2261 {post_previous}\u00B2 \u2261 {post_print} mod {m} \u2261 {post}\n")

                post_previous = post

                if i in use_powers:
                    list_of_completed_squares.append(post)

                i *= 2

            # step 3: product the values that sum to the exponent
            self.output.config(text=self.output.cget(
                'text') + f"\nSTEP 3: Relate the powers you found in step 1 to step 2. Product and divide by modulo: \n")
            list_of_products = list_of_completed_squares.copy()
            final_result = 1

            product_expression2 = " x ".join(str(value) for value in list_of_products)
            self.output.config(text=self.output.cget('text') + f"   ({product_expression2}) mod {m} \u2261 ")
            for value in list_of_products:
                final_result = (final_result * value) % m
                value_print = value

            if final_result >= m:
                final_result = final_result % m

            self.output.config(text=self.output.cget('text') + f"{final_result} mod ({m})")

        except ValueError as ve:
            self.output.config(text=f"Not allowed!")
        except TypeError as e:
            self.output.config(text=f"Integers only!")

    def exit_out(self):
        """
        This function exits the program
        """
        self.destroy()


def main():
    """
    Instantiates an instance of the 'GUIApplication' class and starts the GUI
    """
    app = GUIApplication()
    app.geometry("800x800")
    app.mainloop()


"""
checks if the script is being run directly or if this script is imported in another script (if it is, this main() function will not run automatically)
"""
if __name__ == "__main__":
    main()