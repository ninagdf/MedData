from tkinter import *

def click():
    my_label.config(text="Button Clicked")

def on_enter_manage(event):
    button1.config(image=button1.resized_hover_image)

def on_leave_manage(event):
    button1.config(image=button1.resized_image)

def on_enter_search(event):
    button2.config(image=button2.resized_hover_image)

def on_leave_search(event):
    button2.config(image=button2.resized_image)

def on_enter_about(event):
    button3.config(image=button3.resized_hover_image)

def on_leave_about(event):
    button3.config(image=button3.resized_image)

window = Tk()
window.geometry("1280x720")  # Set initial window size
window.resizable(width=False, height=False)  # Disable window resizing

canvas = Canvas(window, width=1280, height=720)
canvas.pack()

# Set the path to the background image
background_image_path = "D:/ninaf/MedData/MedData/materials/HomepageBG.png"

# Create a PhotoImage object for the background image
background_image = PhotoImage(file=background_image_path)

# Add the background image to the canvas
canvas.create_image(0, 0, anchor="nw", image=background_image)

# Set the Poppins font and font size
font_name = "Poppins"
font_size = 75

# Add the "MedData" text to the canvas
canvas.create_text(90, 250, text="MedData", font=(font_name, font_size), fill="#05066D", anchor="nw")

# Load the button images
ManageButton = PhotoImage(file='D:/ninaf/MedData/MedData/materials/ManageButton.png')
SearchPatientButton = PhotoImage(file='D:/ninaf/MedData/MedData/materials/SearchPatientButton.png')
AboutUsButton = PhotoImage(file='D:/ninaf/MedData/MedData/materials/AboutUsButton.png')

# Resize the button images
resized_image1 = ManageButton.subsample(int(ManageButton.width() / 350), int(ManageButton.height() / 115))
resized_image2 = SearchPatientButton.subsample(int(SearchPatientButton.width() / 350), int(SearchPatientButton.height() / 115))
resized_image3 = AboutUsButton.subsample(int(AboutUsButton.width() / 350), int(AboutUsButton.height() / 115))

# Create button widgets
button1 = Button(window, command=click, image=resized_image1, bd=0, relief="flat", highlightthickness=0)
button2 = Button(window, command=click, image=resized_image2, bd=0, relief="flat", highlightthickness=0)
button3 = Button(window, command=click, image=resized_image3, bd=0, relief="flat", highlightthickness=0)

# Hovered button images
ManageButtonHover = PhotoImage(file='D:/ninaf/MedData/MedData/materials/ManageButtonHover.png')
SearchPatientButtonHover = PhotoImage(file='D:/ninaf/MedData/MedData/materials/SearchPatientButtonHover.png')
AboutUsButtonHover = PhotoImage(file='D:/ninaf/MedData/MedData/materials/AboutUsButtonHover.png')

# Store resized images as attributes of button widgets
button1.resized_image = resized_image1
button1.resized_hover_image = ManageButtonHover.subsample(20, 23)

button2.resized_image = resized_image2
button2.resized_hover_image = SearchPatientButtonHover.subsample(20, 23)

button3.resized_image = resized_image3
button3.resized_hover_image = AboutUsButtonHover.subsample(20, 23)

# Add the buttons to the canvas
button1_window = canvas.create_window(735, 120, anchor="nw", window=button1)
button2_window = canvas.create_window(735, 280, anchor="nw", window=button2)
button3_window = canvas.create_window(735, 440, anchor="nw", window=button3)

# Event bindings for hovering effect
button1.bind('<Enter>', on_enter_manage)
button1.bind('<Leave>', on_leave_manage)
button2.bind('<Enter>', on_enter_search)
button2.bind('<Leave>', on_leave_search)
button3.bind('<Enter>', on_enter_about)
button3.bind('<Leave>', on_leave_about)

my_label = Label(window, text='')
my_label.pack(padx=10, pady=10)

window.mainloop()
