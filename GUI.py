import tkinter as tk








root = tk.Tk()
root.geometry("800x480")

text = tk.Label(text="Miten arvioisit tämän päivän ruoan?",font=("Arial", 35))
desc = tk.Label(text="Vastaathan vain kerran päivässä. \nArviot eivät mitenkään vaikuta koulun tuleviin ruokavalintoihin.",font=("Arial", 15))

text.place(x=30, y=140)
desc.place(x=120, y=220)
root.mainloop()