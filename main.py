import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt


# DDA Algorithm
def dda(x0, y0, x1, y1):
    x, y = x0, y0
    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    
    x_points = []
    y_points = []
    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc
    return x_points, y_points


def plot_line(x_points, y_points):
    plt.plot(x_points, y_points, marker='o')
    plt.title("DDA Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()


def create_gui():
    def on_submit():
        try:
            x0 = int(entry_x0.get())
            x1 = int(entry_x1.get())
            y0 = int(entry_y0.get())
            y1 = int(entry_y1.get())
            
            x_points, y_points = dda(x0, y0, x1, y1)
            plot_line(x_points, y_points)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers")
    
    root = tk.Tk()
    root.title("DDA Line Plotter")
    
    tk.Label(root, text="Initial X:").grid(row=0, column=0)
    tk.Label(root, text="Initial Y:").grid(row=1, column=0)
    tk.Label(root, text="Final X:").grid(row=2, column=0)
    tk.Label(root, text="Final Y:").grid(row=3, column=0)
    
    entry_x0 = tk.Entry(root)
    entry_x0.grid(row=0, column=1)
    entry_x1 = tk.Entry(root)
    entry_x1.grid(row=1, column=1)
    entry_y0 = tk.Entry(root)
    entry_y0.grid(row=2, column=1)
    entry_y1 = tk.Entry(root)
    entry_y1.grid(row=3, column=1)
    
    submit_button = tk.Button(root, text="Plot Line", command=on_submit)
    submit_button.grid(row=4, columnspan=2)
    
    root.mainloop()


create_gui()
