import tkinter as tk
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("Image Display")

# Load the image file
image = Image.open("cool.png")  # Replace "example_image.jpg" with the path to your image file

# Convert the Image object into a Tkinter-compatible photo image
photo = ImageTk.PhotoImage(image)

# Create a label widget to display the image
label = tk.Label(root, image=photo)
label.pack()

# Run the Tkinter event loop
root.mainloop()
