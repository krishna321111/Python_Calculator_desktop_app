import tkinter as tk


class Win(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("410x450")
        self.title("Calculator")
        self.entry_textvar = tk.StringVar()
        self.resizable(False, False)
        self.configure(background = "dark orange")
        

        digits_entry = tk.Entry(self, textvariable=self.entry_textvar, font=("comicsans 15 bold"), relief="sunken")
        digits_entry.pack(fill="x", ipady=10, pady=10)


        frame1 = tk.Frame(self, bg="dark orange", height=50, width=301)
        frame1.pack(side="top", fill="x")

        frame2 = tk.Frame(self, bg="dark orange", height=50, width=50)
        frame2.pack(side="top", fill="x")

        frame3 = tk.Frame(self, bg="dark orange", height=50, width=50)
        frame3.pack(side="top", fill="x")

        frame4 = tk.Frame(self, bg="darkorange1", height=50, width=50)
        frame4.pack(side="top", fill="x")

        def click(event):

            value = event.widget.cget("text")
            # print(value)
            if value == "×":
                value = "*"
            if value == "÷":
                value = "/"

            self.entry_textvar.set(self.entry_textvar.get()+str(value))
            self.update()


        for i in range(7, 10):
            button_set_1 = tk.Button(frame1, text=i, padx=30, borderwidth=2, pady=30, font=("comicsans 15 bold")
                                     )
            button_set_1.pack(side="left")
            i += 1
            button_set_1.bind("<Button-1>", click)

        d = tk.Button(frame1, text="÷", padx=30, borderwidth=2, pady=30, font=("comicsans 15 bold")
                      )
        d.pack(side="left")
        d.bind("<Button-1>", click)

        def clear(event):
            self.entry_textvar.set("")
            self.update()

        C_button = tk.Button(frame1, text="C", padx=28, pady=30, borderwidth=3, font=("comicsans 13 bold"),
                             bg="green", activebackground="green3", fg="white", activeforeground="white"
                             )
        C_button.pack(side="left")
        C_button.bind("<Button-1>", clear)

        for i in range(4, 7):
            button_set_2 = tk.Button(frame2, text=i, padx=30, borderwidth=2, pady=30, font=("comicsans 15 bold")
                                     )
            button_set_2.pack(side="left")
            i += 1
            button_set_2.bind("<Button-1>", click)

        a = tk.Button(frame2, text="×", padx=30, borderwidth=2, pady=30, font=("comicsans 15 bold")
                      )
        a.pack(side="left")
        a.bind("<Button-1>", click)

        for i in range(1, 4):
            button_set_3 = tk.Button(frame3, text=i, padx=30, pady=30, borderwidth=2, font=("comicsans 15 bold")
                                     )
            button_set_3.pack(side="left")
            i += 1
            button_set_3.bind("<Button-1>", click)

        b = tk.Button(frame3, text="-", padx=34, borderwidth=2, pady=30, font=("comicsans 15 bold")
                      )
        b.pack(side="left")
        b.bind("<Button-1>", click)

        for i in [".", 0, "+"]:
            button_set_4 = tk.Button(frame4, text=i, padx=30, pady=30, borderwidth=3, font=("comicsans 15 bold")
                                     )
            button_set_4.pack(side="left")
            button_set_4.bind("<Button-1>", click)

        def calculate(event):
            try:
                calc = eval(self.entry_textvar.get())
                # print(calc)
                self.entry_textvar.set(calc)
                self.update()

            except Exception as e:
                # print("Try Again")
                self.entry_textvar.set("ERROR!")


        c = tk.Button(frame4,text="=", padx=28, pady=31, borderwidth=3, font=("comicsans 13 bold"),
                      bg="navy", activebackground="medium blue", fg="white", activeforeground="white"
                      )
        c.pack(side="left")
        c.bind("<Button-1>", calculate)

        # operants = ["÷","×","-","+","="]
        # for i in operants:
        #     tk.Button(frame1, text=i, padx=40, pady=40, font=("comicsans 15 bold")
        #               ).pack(side="top")


window = Win()
window.mainloop()
