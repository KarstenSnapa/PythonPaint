import tkinter as tk
from PIL import Image, ImageTk, ImageGrab
import os
import tkinter.colorchooser as colorchooser

root = tk.Tk()
root.title("Paint")
root.configure(bg="white")

Tool = 'Pen'
Color = 'Black'
left_click = False  # Initialize left_click variable
slider_value = 0

# ------------------------------------------------------------------------- #

saved_image_count = 0

def save_canvas_as_image():
    global saved_image_count
    # Find the highest numbered image already saved
    existing_images = [f for f in os.listdir() if f.startswith("canvas_image_") and f.endswith(".png")]
    if existing_images:
        existing_numbers = [int(f.split("_")[2].split(".")[0]) for f in existing_images]
        highest_number = max(existing_numbers)
        saved_image_count = highest_number + 1
    else:
        saved_image_count = 1
    
    # Get the bounding box coordinates of the canvas
    x0 = root.winfo_rootx() + canvas.winfo_x()
    y0 = root.winfo_rooty() + canvas.winfo_y()
    x1 = x0 + canvas.winfo_width()
    y1 = y0 + canvas.winfo_height()
    
    # Grab the content of the canvas as an image
    canvas_image = ImageGrab.grab(bbox=(x0, y0, x1, y1))
    
    # Save the image as a PNG file with the determined number
    image_filename = f"canvas_image_{saved_image_count}.png"
    canvas_image.save(image_filename, "PNG")
    print(f"Canvas content saved as {image_filename}")



SaveButton = tk.Button(root, text="Save Canvas", command=save_canvas_as_image)
SaveButton.place(x=560, y=860)

# ------------------------------------------------------------------------- #

xCoords = 1130
yCoords = 20

def display_all_images():
    global photo_references, yCoords, xCoords

    if not root.winfo_exists():
        return

    # Clear the canvas before loading new images
    canvas.delete("all")

    photo_references = []  # Create a list to hold references to PhotoImage objects
    image_files = [f for f in os.listdir() if f.startswith("canvas_image_") and f.endswith(".png")]

    # Sort the image filenames numerically
    image_files = sorted(image_files, key=lambda x: int(x.split("_")[2].split(".")[0]))

    for image_file in image_files:
        print(f"Loading image: {image_file}")
        # Load the image
        image = Image.open(image_file)
        image = image.resize((100, 100))  # Resize image for thumbnail display
        # Convert the image to a format that Tkinter can work with
        photo = ImageTk.PhotoImage(image)
        # Create a label widget to display the image
        label = tk.Label(root, image=photo)
        label.image = photo  # Keep a reference to the image to prevent garbage collection
        label.bind("<Button-1>", lambda event, img=image: display_image_on_canvas(img))
        label.place(x=xCoords, y=yCoords)
        if xCoords == 1130:
            xCoords += 120
        else:
            xCoords -= 120
            yCoords += 120
        print("Label packed")
        # Append the PhotoImage object to the list to keep a reference
        photo_references.append(photo)

    print("All images loaded successfully")

def display_image_on_canvas(pil_image):
    # Convert PIL image to PhotoImage
    resized_image = pil_image.resize((800, 800))
    photo_image = ImageTk.PhotoImage(resized_image)
    
    
    # Clear canvas
    canvas.delete("all")
    
    # Display clicked image on canvas
    canvas.create_image(0, 0, anchor="nw", image=photo_image, tags="image")    
    # Keep a reference to the PhotoImage object to prevent garbage collection
    canvas.photo_image = photo_image

    canvas.tag_lower("image")


displayButton = tk.Button(root, text="Load Images", command=display_all_images)
displayButton.place(x=700, y=860)

# ------------------------------------------------------------------------- #

def choosePen():
    global Tool
    print('Pen')
    Tool = 'Pen'
    slider.config(from_=1, to=15)


def chooseEraser():
    global Tool
    print('Eraser')
    Tool = 'Eraser'
    slider.config(from_=10, to=100)


def chooseCircle():
    global Tool
    print('Circle')
    Tool = 'Circle'
    slider.config(from_=20, to=200)



# ------------------------------------------------------------------------- #



def chooseBlue():
    global Color
    Color = "Blue"
    ColBlueButton.config(width=sel_color_button_size, height=sel_color_button_size)
    reset_color_buttons(ColBlueButton)

def chooseRed():
    global Color
    Color = "Red"
    ColRedButton.config(width=sel_color_button_size, height=sel_color_button_size)
    reset_color_buttons(ColRedButton)

def chooseBlack():
    global Color
    Color = "Black"
    print("black")
    ColBlackButton.config(width=sel_color_button_size, height=sel_color_button_size)
    reset_color_buttons(ColBlackButton)

def chooseYellow():
    global Color
    Color = "Yellow"
    ColYellowButton.config(width=sel_color_button_size, height=sel_color_button_size)
    reset_color_buttons(ColYellowButton)

def chooseGreen():
    global Color
    Color = "Green"
    ColGreenButton.config(width=sel_color_button_size, height=sel_color_button_size)
    reset_color_buttons(ColGreenButton)

def chooseOrange():
    global Color
    Color = "Orange"
    ColOrangeButton.config(width=sel_color_button_size, height=sel_color_button_size)
    reset_color_buttons(ColOrangeButton)

def choosePink():
    global Color
    Color = "Pink"
    ColPinkButton.config(width=sel_color_button_size, height=sel_color_button_size)
    reset_color_buttons(ColPinkButton)

def chooseGray():
    global Color
    Color = "Grey"
    ColGrayButton.config(width=sel_color_button_size, height=sel_color_button_size)
    reset_color_buttons(ColGrayButton)

def reset_color_buttons(selected_button):
    # Reset the size of all color buttons to color_button_size except for the selected button
    buttons = [ColBlueButton, ColRedButton, ColBlackButton, ColYellowButton,
            ColGreenButton, ColOrangeButton, ColPinkButton, ColGrayButton]
    for button in buttons:
        if button != selected_button:
            button.config(width=color_button_size, height=color_button_size)


def chooseCustomColor():
    global Color
    color = colorchooser.askcolor(title="Choose Color")[1]
    if color:
        Color = color

        reset_color_buttons(None)

custom_color_button = tk.Button(root, text="Custom Color", command=chooseCustomColor)
custom_color_button.place(x=20, y=180)
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
    if left_click and Tool == 'Circle':
        x, y = event.x, event.y
        radius = slider_value // 2  
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=Color, outline=Color, width=0)  

        
    if left_click and Tool == 'Eraser':
        x, y = event.x, event.y
        prev_x, prev_y = canvas.coords("current_line")[-2:]
        canvas.create_line(prev_x, prev_y, x, y, fill="white", width=slider_value, tags="current_line")
        canvas.coords("current_line", event.x, event.y, event.x, event.y)
    
    elif left_click and Tool == 'Pen':
        x, y = event.x, event.y
        prev_x, prev_y = canvas.coords("current_line")[-2:]
        canvas.create_line(prev_x, prev_y, x, y, fill=Color, width=slider_value, tags="current_line")
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

circle_image = Image.open("circle.png")
circle_image = circle_image.resize((80, 60))
circle_photo = ImageTk.PhotoImage(circle_image)
CircleButton = tk.Button(root, image=circle_photo, command=chooseCircle, width=60, height=60, relief=tk.RAISED, borderwidth=0)
CircleButton.place(x=3, y=680)

# ------------------------------------------------------------------------- #

styles_text = "STYLES"
styles_label = tk.Label(root, text=styles_text, bg="white", fg="black", font=("Arial", 22))
styles_label.place(x=65, y=10)

color_button_size = 30
sel_color_button_size = 34

blue_image = Image.open("blue.png")
blue_image = blue_image.resize((100,100))
blue_photo = ImageTk.PhotoImage(blue_image)
ColBlueButton = tk.Button(root, image=blue_photo, command=chooseBlue, width=color_button_size, height=color_button_size, )
ColBlueButton.place(x=20, y=80)


red_image = Image.open("red.png")
red_image = red_image.resize((100,100))
red_photo = ImageTk.PhotoImage(red_image)
ColRedButton = tk.Button(root, image=red_photo, command=chooseRed, width=color_button_size, height=color_button_size, )
ColRedButton.place(x=70, y=80)

yellow_image = Image.open("yellow.png")
yellow_image = yellow_image.resize((100,100))
yellow_photo = ImageTk.PhotoImage(yellow_image)
ColYellowButton = tk.Button(root, image=yellow_photo, command=chooseYellow, width=color_button_size, height=color_button_size, )
ColYellowButton.place(x=120, y=80)

black_image = Image.open("black.webp")
black_image = black_image.resize((100,100))
black_photo = ImageTk.PhotoImage(black_image)
ColBlackButton = tk.Button(root, image=black_photo, command=chooseBlack, width=color_button_size, height=color_button_size, )
ColBlackButton.place(x=170, y=80)

green_image = Image.open("Green.png")
green_image = green_image.resize((100, 100))
green_photo = ImageTk.PhotoImage(green_image)
ColGreenButton = tk.Button(root, image=green_photo, command=chooseGreen, width=color_button_size, height=color_button_size)
ColGreenButton.place(x=20, y=130)

orange_image = Image.open("Orange.png")
orange_image = orange_image.resize((100, 100))
orange_photo = ImageTk.PhotoImage(orange_image)
ColOrangeButton = tk.Button(root, image=orange_photo, command=chooseOrange, width=color_button_size, height=color_button_size)
ColOrangeButton.place(x=70, y=130)

pink_image = Image.open("Pink.jpeg")
pink_image = pink_image.resize((100, 100))
pink_photo = ImageTk.PhotoImage(pink_image)
ColPinkButton = tk.Button(root, image=pink_photo, command=choosePink, width=color_button_size, height=color_button_size)
ColPinkButton.place(x=120, y=130)

gray_image = Image.open("Gray.png")
gray_image = gray_image.resize((100, 100))
gray_photo = ImageTk.PhotoImage(gray_image)
ColGrayButton = tk.Button(root, image=gray_photo, command=chooseGray, width=color_button_size, height=color_button_size)
ColGrayButton.place(x=170, y=130)

# ------------------------------------------------------------------------- #

canvas = tk.Canvas(root, bg="white", width=800, height=800)
canvas.place(x=280, y=20)

canvas.bind("<Button-1>", on_left_click)
canvas.bind("<ButtonRelease-1>", on_left_release)
canvas.bind("<B1-Motion>", motion)

canvas.create_rectangle(0, 0, 1, 1, fill="black", width=2, tags="current_line")

# ------------------------------------------------------------------------- #

slider_text = "CHANGE TOOL SIZE"
slider_label = tk.Label(root, text=slider_text, bg="white", fg="black", font=("Arial", 17))
slider_label.place(x=2, y=753)
slider = tk.Scale(root, from_=1, to=15, orient=tk.HORIZONTAL, length=165, command=update_slider)
slider.place(x=3, y=775)

# ------------------------------------------------------------------------- #

root.mainloop()
display_all_images()