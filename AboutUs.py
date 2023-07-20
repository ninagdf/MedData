from tkinter import *

def click():
    my_label.config(text="Button Clicked")

def on_enter_AboutUsBack(event):
    button4.config(image=button4.resized_hover_image)

def on_leave_AboutUsBack(event):
    button4.config(image=button4.resized_image)

window = Tk()
window.geometry("1540x800")  # Set initial window size
window.resizable(width=False, height=False)  # Disable window resizing
window.title("MedData")
icon = PhotoImage(file='materials/Icon.png')
window.iconphoto(True, icon)

canvas = Canvas(window, width=1540, height=800)
canvas.pack()

# Set the path to the background image
background_image_path4 = "D:/ninaf/MedData/MedData/materials/AboutUsBG.png"

# Create a PhotoImage object for the background image
background_image4 = PhotoImage(file=background_image_path4)

# Add the background image to the canvas
canvas.create_image(0, 0, anchor="nw", image=background_image4)

# Create transparent image
transparent_image = PhotoImage(width=1, height=1)

# Load the button image
AboutUsBackButton = PhotoImage(file='D:/ninaf/MedData/MedData/materials/AboutUsBack.png')

# Resize the button image
resized_image4 = AboutUsBackButton.subsample(int(AboutUsBackButton.width() / 100), int(AboutUsBackButton.height() / 65))

# Create button widget
button4 = Button(window, command=click, image=resized_image4, bd=0, relief="flat", highlightthickness=0, compound="center",
                 fg="white", bg="white", activebackground="white", activeforeground="white")

# Set the width and height of the button
desired_width4 = 100
desired_height4 = 65
button4.config(width=desired_width4, height=desired_height4)

# Hovered button image
AboutUsBackButtonHover = PhotoImage(file='materials/AboutUsBackHover.png')

# Store resized images as attributes of button widgets
button4.resized_image = resized_image4
button4.resized_hover_image = AboutUsBackButtonHover.subsample(50, 59)

# Add the AboutUs image to the canvas as a button
button4_window = canvas.create_window(1300, 50, anchor="nw", window=button4)

# Event bindings for hovering effect
button4.bind('<Enter>', on_enter_AboutUsBack)
button4.bind('<Leave>', on_leave_AboutUsBack)

my_label = Label(window, text='')
my_label.pack(padx=10, pady=10)

window.mainloop()
