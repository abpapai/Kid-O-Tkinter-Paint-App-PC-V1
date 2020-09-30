from tkinter import *
from PIL import Image, ImageDraw, ImageGrab, ImageTk
import PIL
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title('Paint Digitaly')
root.iconbitmap('c:/paint/Kid-O-Tkinter.ico')
root.geometry("1000x1000")
root.config(bg="#D3D3D3")
root.minsize(1000,980)

brush_color = "black"
def paint(e):

    #Brush Parameters

    brush_width = '%0.0f' % float(my_slider.get())
    #brush_color = "green"
    #Brush Type: BUTT, ROUND, PROJECTING
    brush_type2 = brush_type.get()
    #Starting position
    x1 = e.x - 1
    y1 = e.y - 1
    #Ending position
    x2 = e.x + 1
    y2 = e.y + 1
    # Draw on the canvas
    my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type2, smooth=True)

# Change the brush size
def change_brush_size(thing):
    slider_label.config(text='%0.0f' % float(my_slider.get()))

# Change Brush Color
def change_brush_color():
    global brush_color
    brush_color = "black"
    brush_color = colorchooser.askcolor(color=brush_color)[1]
    #color = Label(root,text=brush_color)
    #color.pack(pady=20)

# Change Canvas Color
def change_canvas_color():
    global bg_color
    bg_color = "black"
    bg_color = colorchooser.askcolor(color=bg_color)[1]
    my_canvas.config(bg=bg_color)
    #color = Label(root,text=brush_color)
    #color.pack(pady=20)

#Clear Screen
def clear_screen():
    my_canvas.delete(ALL)
    my_canvas.config(bg="white")

# Save Image
def save_as_png():
    result = filedialog.asksaveasfilename(initialdir='C:/paint/images/', filetypes=(("png files", "*.png"), ("all files", "*.*")))
    
    if result.endswith('.png'):
       pass
    else:
       result = result + '.png'
    
    if result:
       x=root.winfo_rootx()+my_canvas.winfo_x()
       y=root.winfo_rooty()+my_canvas.winfo_y()
       x1=x+my_canvas.winfo_width()
       y1=y+my_canvas.winfo_height()
       ImageGrab.grab().crop((x,y,x1,y1)).save(result)

    #result_label = Label(root, text=result)
    #result_label.pack(pady=10)
    
    # Pop Up Sucess Message
    messagebox.showinfo("Image Saved", "Your Image Has Been Saved!")

# Create Our Canvas
w=900
h=720
my_canvas= Canvas(root, width=w, height=h, bg="white", borderwidth=2)
my_canvas.pack(pady=20)

#my_canvas.create_line(0, 100, 300, 100, fill="red" )
#my_canvas.create_line(150, 0, 150, 200, fill="yellow" )

my_canvas.bind('<B1-Motion>',paint)

# Create Brush Options Frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

# Brush Size
brush_size_frame = LabelFrame(brush_options_frame, text="Brush Size", font=('Helvetica',10,'bold'))
brush_size_frame.grid(row=0, column=0, padx=50)
# Brush Slider
my_slider = ttk.Scale(brush_size_frame, from_=1, to=100, command=change_brush_size, orient=VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)

# Brush Slider Label
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)

# Brush Type
brush_type_frame = LabelFrame(brush_options_frame, text="Brush Type", height=400, font=('Helvetica',10,'bold'))
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set("round")

# Create Radio Buttons for Brush Type
brush_type_radio1 = Radiobutton(brush_type_frame, text="Round", variable=brush_type, value="round", font=('Helvetica',8,'italic','bold'))
brush_type_radio2 = Radiobutton(brush_type_frame, text="Slash", variable=brush_type, value="butt", font=('Helvetica',8,'italic','bold'))
brush_type_radio3 = Radiobutton(brush_type_frame, text="Diamond", variable=brush_type, value="projecting", font=('Helvetica',8,'italic','bold'))

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# Change colors
change_colors_frame = LabelFrame(brush_options_frame, text="Change Colors", font=('Helvetica',10,'bold'))
change_colors_frame.grid(row=0, column=2)

# Change Brush Colors Button
brush_color_button = Button(change_colors_frame, text="Brush Color", command=change_brush_color, font=('Helvetica',8,'italic','bold'))
brush_color_button.pack(pady=10,padx=10)

# Change Canvas Background Color
canvas_color_button = Button(change_colors_frame, text="Canvas Color", command=change_canvas_color, font=('Helvetica',8,'italic','bold'))
canvas_color_button.pack(pady=10,padx=10)

# Program Options frame
options_frame = LabelFrame(brush_options_frame, text="Program Options", font=('Helvetica',10,'bold'))
options_frame.grid(row=0, column=3, padx=50)

# Clear Screen button
clear_button = Button(options_frame, text="Clear Screen", command= clear_screen, font=('Helvetica',8,'italic','bold'))
clear_button.pack(padx=10, pady=10)

# Save Image Button
save_image_button = Button(options_frame, text="Save To PNG", command= save_as_png, font=('Helvetica',8,'italic','bold'))
save_image_button.pack(padx=10, pady=10)

# Exit button 
button_quit = Button(options_frame, text="Exit Program", command= root.quit, font=('Helvetica',8,'italic','bold'))
button_quit.pack(padx=10, pady=10)


root.mainloop()



