from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculator")
root.geometry("400x400")
root.configure(bg="light green")

def msg():
    messagebox.showinfo("Alert", "Click on OK")
    topwin()

label1 = Label(
    root,
    text="Welcome to Denomination Calculator",
    font=("Arial", 17),
    bg="light green"
)
label1.place(relx=0.5, rely=0.3, anchor=CENTER)

b1 = Button(root, text="Click to start", command=msg)
b1.place(relx=0.5, rely=0.45, anchor=CENTER)

def topwin():
    top = Toplevel(root)
    top.title("Denomination Calculator")
    top.geometry("400x400")
    top.configure(bg="light green")

    Label(top, text="Enter the amount",
          bg="light green", font=("Arial", 18)).place(relx=0.5, rely=0.15, anchor=CENTER)

    e1 = Entry(top)
    e1.place(relx=0.5, rely=0.25, anchor=CENTER)

    Label(top, text="Number of notes are:",
          bg="light green", font=("Arial", 14)).place(relx=0.5, rely=0.35, anchor=CENTER)

    Label(top, text="2000 :", bg="light green").place(relx=0.3, rely=0.45, anchor=CENTER)
    t1 = Entry(top, width=10)
    t1.place(relx=0.6, rely=0.45, anchor=CENTER)

    Label(top, text="500 :", bg="light green").place(relx=0.3, rely=0.55, anchor=CENTER)
    t2 = Entry(top, width=10)
    t2.place(relx=0.6, rely=0.55, anchor=CENTER)

    def cal():
        try:
            amount = int(e1.get())

            note2000 = amount // 2000
            amount %= 2000

            note500 = amount // 500

            t1.delete(0, END)
            t2.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    Button(top, text="Calculate", command=cal).place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
