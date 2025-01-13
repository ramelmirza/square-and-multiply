"""
Author: Ramel Mirza
Date: 09-19-2024
Description: This script was created for the students at Mohawk College who are taking Discrete Mathematics and Statistics from Mrs. Stojanovska-Pocuca. It acts as a guide to help aid students when studying the square and multiply algorithm.
Version: 1.00
"""
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
        bem_style.configure("Fourth.TLabel", font=("Comic Sans MS", 16, "bold"))

        # base
        self.base_label = ttk.Label(self, text="Base! ", style="Fourth.TLabel")
        self.base_label.pack(anchor="center")
        self.base = ttk.Entry(self)
        self.base.configure()
        self.base.pack(anchor="center")

        # exponent
        self.exponent_label = ttk.Label(self, text="Exponent! ", style="Fourth.TLabel")
        self.exponent_label.pack(anchor="center")
        self.exponent = ttk.Entry(self)
        self.exponent.pack(anchor="center")

        # modulo
        self.modulo_label = ttk.Label(self, text="Modulo! ", style="Fourth.TLabel")
        self.modulo_label.pack(anchor="center")
        self.modulo = ttk.Entry()
        self.modulo.pack(anchor="center")

        # calculate button
        button_style = ttk.Style()
        button_style.configure("Fifth.TButton", font=("Comic Sans MS", 13, "bold"))
        self.button = ttk.Button(self, text="Compute it!", command=self.square_and_multiply, style="Fifth.TButton")
        self.button.configure(padding=10)
        self.button.place(x=650, y=735)

        # steps
        self.output = ttk.Label(self)
        self.output.pack()

    def square_and_multiply(self):
        """
        This function computes a large power of a positive base integer down to its non-zero equivalent in certain modulo (including the actual output of the answer)
        """
        pass


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
