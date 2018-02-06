import tkinter as tk
import os


def launch():
    button.config(text='START', fg='black')
    try:
        n = int(entry.get())
        speed = entry2.get()
        os.system("python3 graphic-client.py {} {}".format(n, speed))
    except ValueError:
        button.config(text='Error: input must be an integer', fg='red')


root = tk.Tk()
root.title("N-Queens Launcher")
frame = tk.Frame(root)
frame.pack()


text = tk.Label(frame, text="Enter N for N-Queens problem")

entry = tk.Entry(frame)
entry.insert(0, "8")


text2 = tk.Label(frame, text="States / second to show (default is no max)")

entry2 = tk.Entry(frame)
entry2.insert(0, "10")

button = tk.Button(frame,
                   text="START",
                   command=launch)





text.pack(fill=tk.X)
entry.pack(fill=tk.X)
text2.pack(fill=tk.X)
entry2.pack(fill=tk.X)
button.pack(fill=tk.X)

root.mainloop()
