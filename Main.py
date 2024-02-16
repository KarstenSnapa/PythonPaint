import tkinter as tk

root = tk.Tk()
root.title("Paint")
root.configure(bg="white")

Tool = ''
left_click = False  # Initialize left_click variable

def choosePen():
    global Tool
    print('Pen')
    Tool = 'Pen'

def chooseEraser():
    global Tool
    print('Eraser')
    Tool = 'Eraser'

def on_left_click(event):
    global left_click
    left_click = True 
    # Initialize the starting point of the line at the current mouse position
    canvas.coords("current_line", event.x, event.y, event.x, event.y)

def on_left_release(event):
    global left_click
    left_click = False

def motion(event): 
    if left_click:
        x, y = event.x, event.y
        prev_x, prev_y = canvas.coords("current_line")[-2:]
        canvas.create_line(prev_x, prev_y, x, y, fill="black", width=2, tags="current_line")

PenButton = tk.Button(root, text="PEN TOOL", command=choosePen, width=10, height=3, relief=tk.RAISED, borderwidth=0)
PenButton.place(x=0, y=844)

EraserButton = tk.Button(root, text="ERASER TOOL", command=chooseEraser, width=10, height=3, relief=tk.RAISED, borderwidth=0)
EraserButton.place(x=110, y=844)

canvas = tk.Canvas(root, bg="white", width=800, height=800)
canvas.pack()

canvas.bind("<Button-1>", on_left_click)
canvas.bind("<ButtonRelease-1>", on_left_release)
canvas.bind("<B1-Motion>", motion)
canvas.create_line(0, 0, 0, 0, fill="black", width=2, tags="current_line")

root.mainloop()
