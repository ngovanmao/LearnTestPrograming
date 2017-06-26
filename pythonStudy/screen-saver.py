#!/usr/bin/python

# Simple "screensaver" program.

# Import modules
#import simplegui
import Tkinter
from Tkinter import *
import ttk
import random

# Global state
message = "Python is Fun!"
position = [50, 50]
width = 500
height = 500
interval = 2000

# Handler for text box
def update(text):
    global message
    message = text
    
# Handler for timer
def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")

# Create a frame 
#frame = simplegui.create_frame("Home", width, height)
frame = Tkinter.Tk()

# Register event handlers
L1 = Label(frame, text="Meassage")
L1.pack(side = LEFT)
E1 = Entry(frame, bd = 10)
E1.pack(side = RIGHT)
ttk.Button(frame, text="Hello World")
#ttk.grid()
#text = frame.add_input("Message:", update, 150)
#frame.set_draw_handler(draw)
#timer = simplegui.create_timer(interval, tick)

# Start the frame animation
#frame.start()
#timer.start()
frame.mainloop()
