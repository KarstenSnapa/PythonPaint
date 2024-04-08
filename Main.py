import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Paint")
root.configure(bg="white")

Tool = ''
Color = 'Black'
left_click = False  # Initialize left_click variable
slider_value = 0


# ------------------------------------------------------------------------- #

def choosePen():
    global Tool
    print('Pen')
    Tool = 'Pen'
    slider.config(from_=1, to=5)


def chooseEraser():
    global Tool
    print('Eraser')
    Tool = 'Eraser'
    slider.config(from_=10, to=100)

# ------------------------------------------------------------------------- #

def chooseBlue():
    global Color
    Color = "Blue"

def chooseRed():
    global Color
    Color = "Red"

def chooseBlack():
    global Color
    Color = "Black"

def chooseYellow():
    global Color
    Color = "Yellow"
# ------------------------------------------------------------------------- #

def on_left_click(event):
    global left_click
    left_click = True 
    # Initialize the starting point of the line at the current mouse position
    canvas.coords("current_line", event.x, event.y, event.x, event.y)

def on_left_release(event):
    global left_click
    left_click = False

# ------------------------------------------------------------------------- #


def motion(event): 
    if left_click and Tool == 'Pen':
        x, y = event.x, event.y
        prev_x, prev_y = canvas.coords("current_line")[-2:]
        canvas.create_line(prev_x, prev_y, x, y, fill=Color, width=slider_value, tags="current_line")
        canvas.coords("current_line", event.x, event.y, event.x, event.y)
        
    if left_click and Tool == 'Eraser':
        x, y = event.x, event.y
        prev_x, prev_y = canvas.coords("current_line")[-2:]
        canvas.create_line(prev_x, prev_y, x, y, fill="white", width=slider_value, tags="current_line")
        canvas.coords("current_line", event.x, event.y, event.x, event.y)


# ------------------------------------------------------------------------- #

def update_slider(value):
    global slider_value
    slider_value = int(value)

# ------------------------------------------------------------------------- #

pen_image = Image.open("pen.png")
pen_image = pen_image.resize((80, 60))  
pen_photo = ImageTk.PhotoImage(pen_image)
PenButton = tk.Button(root, image=pen_photo, command=choosePen, width=80, height=60, relief=tk.RAISED, borderwidth=0)
PenButton.place(x=3, y=833)

# ------------------------------------------------------------------------- #

eraser_image = Image.open("eraser.jpeg")
eraser_image = eraser_image.resize((80, 60))
eraser_photo = ImageTk.PhotoImage(eraser_image)
EraserButton = tk.Button(root, image=eraser_photo, command=chooseEraser, width=80, height=60, relief=tk.RAISED, borderwidth=0)
EraserButton.place(x=89, y=833)

# ------------------------------------------------------------------------- #

styles_text = "STYLES"
styles_label = tk.Label(root, text=styles_text, bg="white", fg="black", font=("Arial", 22))
styles_label.place(x=65, y=10)



blue_image = Image.open("blue.png")
blue_image = blue_image.resize((100,100))
blue_photo = ImageTk.PhotoImage(blue_image)
ColBlueButton = tk.Button(root, image=blue_photo, command=chooseBlue, width=30, height=30, )
ColBlueButton.place(x=20, y=80)


red_image = Image.open("red.png")
red_image = red_image.resize((100,100))
red_photo = ImageTk.PhotoImage(red_image)
ColRedButton = tk.Button(root, image=red_photo, command=chooseRed, width=30, height=30, )
ColRedButton.place(x=70, y=80)

yellow_image = Image.open("yellow.png")
yellow_image = yellow_image.resize((100,100))
yellow_photo = ImageTk.PhotoImage(yellow_image)
ColYellowButton = tk.Button(root, image=yellow_photo, command=chooseYellow, width=30, height=30, )
ColYellowButton.place(x=120, y=80)

black_image = Image.open("black.webp")
black_image = black_image.resize((100,100))
black_photo = ImageTk.PhotoImage(black_image)
ColBlackButton = tk.Button(root, image=black_photo, command=chooseBlack, width=30, height=30, )
ColBlackButton.place(x=170, y=80)

# ------------------------------------------------------------------------- #

rødbil_image = Image.open("rødbil.png")
rødbil_image = rødbil_image.resize((30, 30))
rødbil_photo = ImageTk.PhotoImage(rødbil_image)
image_label = tk.Label(root, image=rødbil_photo)
image_label.place(x=400, y=400) 


# ------------------------------------------------------------------------- #

canvas = tk.Canvas(root, bg="white", width=800, height=800)
canvas.place(x=280, y=40)

canvas.bind("<Button-1>", on_left_click)
canvas.bind("<ButtonRelease-1>", on_left_release)
canvas.bind("<B1-Motion>", motion)

canvas.create_rectangle(0, 0, 1, 1, fill="black", width=2, tags="current_line")

# ------------------------------------------------------------------------- #

slider_text = "CHANGE TOOL SIZE"
slider_label = tk.Label(root, text=slider_text, bg="white", fg="black", font=("Arial", 17))
slider_label.place(x=2, y=753)
slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, length=165, command=update_slider)
slider.place(x=3, y=775)
    
# ------------------------------------------------------------------------- #

root.mainloop()
