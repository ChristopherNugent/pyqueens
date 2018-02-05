import tkinter as tk
import os

root = tk.Tk()
root.title("N-Queens Launcher")
frame = tk.Frame(root)
frame.pack()


text = tk.Label(root, text="Enter N for N-Queens problem")

entry = tk.Entry(root)
entry.insert(0, "8")


def launch():
    text.config(text='Enter N for N-Queens problem:', fg='black')
    try:
        n = int(entry.get())
        os.system("python3 graphic-client.py {}".format(n))
    except ValueError:
        text.config(text='Error, input must be an integer', fg='red')


button = tk.Button(frame,
                   text="LAUNCH",
                   command=launch)


text.pack(fill=tk.X, side=tk.LEFT)
entry.pack(fill=tk.X, side=tk.LEFT)
button.pack(fill=tk.X, side=tk.LEFT)

root.mainloop()
