import tkinter as tk
import random
import math

class CanvasRotatable(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.angle = 0
        self.center = (0, 0)

    def rotate(self, item, angle):
        self.angle += angle
        x, y = self.center
        x, y = self.coords(item)[0] + x, self.coords(item)[1] + y
        x, y = rotate_point((x, y), self.center, self.angle)
        self.coords(item, x - self.center[0], y - self.center[1], x + self.center[0], y + self.center[1])

    def move(self, item, x, y):
        self.center = (self.winfo_width() / 2, self.winfo_height() / 2)
        tk.Canvas.move(self, item, x, y)

def rotate_point(point, axis, angle):
    angle = math.radians(angle)
    x, y = point
    ox, oy = axis
    qx = ox + math.cos(angle) * (x - ox) - math.sin(angle) * (y - oy)
    qy = oy + math.sin(angle) * (x - ox) + math.cos(angle) * (y - oy)
    return qx, qy

def spin_wheel():
    # Get a random angle to spin the wheel
    angle = random.randint(0, 359)
    # Calculate the number of degrees to rotate the wheel
    degrees_to_rotate = angle - (angle % 30)
    # Rotate the wheel by the calculated angle
    canvas.rotate(wheel, degrees_to_rotate)
    # Calculate the option that was selected
    option_selected = math.floor(angle / 30)
    # Set the text of the label to the selected option
    label.config(text=OPTIONS[option_selected])

# Create a tkinter window
window = tk.Tk()

# Set the title of the window
window.title("Decision Wheel")

# Set the size of the window
window.geometry("400x400")

# Define the options to display on the wheel
OPTIONS = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6", "Option 7", "Option 8", "Option 9", "Option 10", "Option 11", "Option 12"]

# Create a canvas to draw the decision wheel on
canvas = CanvasRotatable(window, width=300, height=300, bg="white")
canvas.pack()

# Draw the segments of the wheel on the canvas
for i in range(12):
    start_angle = 30 * i - 15
    end_angle = start_angle + 30
    canvas.create_arc(0, 0, 300, 300, start=start_angle, extent=30, outline="black", fill="white")
    canvas.create_text(150 + 110 * math.cos(math.radians(15 + 30 * i)), 150 + 110 * math.sin(math.radians(15 + 30 * i)), text=OPTIONS[i], angle=15 + 30 * i)

# Draw the center of the wheel on the canvas
canvas.create_oval(140, 140, 160, 160, fill="black")

# Draw the wheel on the canvas
wheel = canvas.create_polygon(150, 10, 170, 60, 130, 60, fill="grey")

# Draw the pointer on the canvas
pointer = canvas.create_polygon(200, 50, 220, 100, 180, 100, fill="red")

# Bind the spin_wheel function to the canvas
canvas.bind("<Button-1>", lambda event: spin_wheel())

# Create a label widget to display the selected option
label = tk.Label(window, text="", font=("Arial", 16))
label.pack()

# Start the tkinter event loop
window.mainloop()

