import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("260x360+100+100")
window.resizable(False, False)

display = tk.Entry(window, justify="right", font=(
    "Consolas", 18), bd=8, relief="sunken")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=6, pady=6)

for r in range(1, 6):
    window.grid_rowconfigure(r, weight=1)
for c in range(4):
    window.grid_columnconfigure(c, weight=1)


def click(key):
    if key == "C":
        display.delete(0, tk.END)
    elif key == "=":
        try:
            text = display.get()
            result = eval(text)
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, key)


def add_btn(text, row, col, rowspan=1, colspan=1):
    tk.Button(
        window,
        text=text,
        font=("Consolas", 14),
        command=lambda: click(text),
    ).grid(
        row=row,
        column=col,
        rowspan=rowspan,
        columnspan=colspan,
        sticky="nsew",
        padx=1,
        pady=1,
    )


add_btn("C", 1, 0)
add_btn("/", 1, 1)
add_btn("*", 1, 2)
add_btn("-", 1, 3)

add_btn("7", 2, 0)
add_btn("8", 2, 1)
add_btn("9", 2, 2)
add_btn("+", 2, 3, rowspan=2)

add_btn("4", 3, 0)
add_btn("5", 3, 1)
add_btn("6", 3, 2)

add_btn("1", 4, 0)
add_btn("2", 4, 1)
add_btn("3", 4, 2)
add_btn("=", 4, 3, rowspan=2)

add_btn("0", 5, 0, colspan=2)
add_btn(".", 5, 2)

window.mainloop()
