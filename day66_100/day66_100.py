import tkinter as tk

window = tk.Tk()
window.title("Hello world")
window.geometry("400x400")

label = 0


def updateLabel():
  global label
  number = text.get("1.0", "end")
  number = int(number)
  label += number
  hello["text"] = label

hello = tk.Label(text=label)
hello.grid(row=0,column=1)

text = tk.Text(window, height = 1, width = 25)
text.grid(row=1,column=1)

button = tk.Button(text="Click me!",
command=updateLabel).grid(row=2, column=0)

button2 = tk.Button(text="Another Button",
command=updateLabel).grid(row=2, column=1)

button3 = tk.Button(text="Last one",
command=updateLabel).grid(row=2, column=2)

tk.mainloop()
