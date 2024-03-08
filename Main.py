import tkinter as tk

root = tk.Tk()
root.title("Paint")
root.configure(bg="white")

Tool = ''
left_click = False  # Initialize left_click variable
slider_value = 0

def choosePen():
    global Tool
    print('Pen')
    Tool = 'Pen'
    slider.config(from_=1, to=10)

def chooseEraser():
    global Tool
    print('Eraser')
    Tool = 'Eraser'
    slider.config(from_=10, to=100)

def on_left_click(event):
    global left_click
    left_click = True 
    # Initialize the starting point of the line at the current mouse position
    canvas.coords("current_line", event.x, event.y, event.x, event.y)

def on_left_release(event):
    global left_click
    left_click = False

def motion(event): 
    if left_click and Tool == 'Pen':
        x, y = event.x, event.y
        prev_x, prev_y = canvas.coords("current_line")[-2:]
        canvas.create_rectangle(prev_x, prev_y, x, y, fill="black", width=slider_value, tags="current_line")
        canvas.coords("current_line", event.x, event.y, event.x, event.y)
        
    if left_click and Tool == 'Eraser':
        x, y = event.x, event.y
        prev_x, prev_y = canvas.coords("current_line")[-2:]
        canvas.create_oval(prev_x, prev_y, x, y, fill="white", width=slider_value, tags="current_line")
        canvas.coords("current_line", event.x, event.y, event.x, event.y)


def update_slider(value):
    global slider_value
    slider_value = int(value)


PenButton = tk.Button(root, text="PEN TOOL", command=choosePen, width=10, height=3, relief=tk.RAISED, borderwidth=0)
PenButton.place(x=0, y=844)

EraserButton = tk.Button(root, text="ERASER TOOL", command=chooseEraser, width=10, height=3, relief=tk.RAISED, borderwidth=0)
EraserButton.place(x=110, y=844)

canvas = tk.Canvas(root, bg="white", width=800, height=800)
canvas.pack()

canvas.bind("<Button-1>", on_left_click)
canvas.bind("<ButtonRelease-1>", on_left_release)
canvas.bind("<B1-Motion>", motion)

canvas.create_rectangle(0, 0, 1, 1, fill="black", width=2, tags="current_line")

slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, length=170, command=update_slider)
slider.place(x=10, y=802)
    

root.mainloop()
