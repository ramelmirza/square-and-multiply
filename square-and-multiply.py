"""
Author: Ramel Mirza
Date: 09-19-2024
Description: This script was created for the students at Mohawk College who are taking Discrete Mathematics and Statistics from Mrs. Stojanovska-Pocuca. It acts as a guide to help aid students when studying the square and multiply algorithm.
Version: 1.01
"""
import math
import tkinter as tk  # tkinter
from tkinter import ttk  # themed tkinter

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
        steps_style.configure("Sixth.TLabel", font=("Comic Sans MS", 10, "bold"))
        self.output = ttk.Label(self,
                                text="Output: ")  # will be updated as square and multiply computes
        self.output.pack(anchor="center", pady=50)

        # error label
        error_style = ttk.Style()
        error_style.configure("Seventh.TLabel", font=("Comic Sans MS", 10, "bold"))
        self.error = ttk.Label(self, text="")

    def square_and_multiply(self):
        """
        This function computes a large power of a positive base integer down to its non-zero equivalent in certain modulo (including the actual output of the answer)
        """
        b = int(self.base.get())
        e = int(self.exponent.get())
        m = int(self.modulo.get())

        ###################################

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

        binary_str_rev = reversed(binary_str)  # only to print it in the output label

        # step 1.5: find powers of 2 that sum to b (effectively just finding 1's)
        powers_of_2_and_indices = {}
        for digit in range(0, len(binary_str)):
            if binary_str[digit] == '1':
                powers_of_2_and_indices[(int(math.pow(2, int(digit))))] = digit

        # mapped it to a dictionary such that I get the value and the index which also happens to be the power the base is being raised to

        # now I know that 2^max_power will be the limit, I can square the numbers up until the comparison equals the math.pow() of 2 and the value max_power - which is obviously the max value of the keys of the dictionary
        max_power = max(list(powers_of_2_and_indices.keys()))
        list_of_values = list(powers_of_2_and_indices.values())

        # step 2: solve the squares
        steps_to_complete = len(binary_str) - 1
        i = 1
        list_of_completed_squares = []
        for j in range(1, max_power + 1, int(math.pow(2, i))):
            if i == steps_to_complete:
                break
            post = int(math.pow(b, 2))
            if post >= m:
                post = post % m
            if i in list_of_values:
                list_of_completed_squares.append(post)
            i += 1

        # step 3: product the values that sum to the exponent
        list_of_products = []
        for i in list_of_completed_squares:
            for j in list_of_completed_squares:
                if i * j >= m:
                    list_of_products.append((i * j) % m)
                else:
                    list_of_products.append(i * j)



    ###################################

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