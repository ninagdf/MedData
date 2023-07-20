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

def on_enter_sqlcodes(event):
    button3.config(image=button3.resized_hover_image)

def on_leave_sqlcodes(event):
    button3.config(image=button3.resized_image)

def on_enter_about(event):
    button4.config(image=button4.resized_hover_image)

def on_leave_about(event):
    button4.config(image=button4.resized_image)
    
def to_ab():
    try:
        window.destroy()
    finally:
        import AboutUs
        AboutUs.aboutus()

window = Tk()
window.geometry("1540x800")  # Set initial window size
window.resizable(width=False, height=False)  # Disable window resizing
window.title("MedData")
icon = PhotoImage(file='materials/Icon.png')
window.iconphoto(True,icon)

canvas = Canvas(window, width=1540, height=800)
canvas.pack()

# Set the path to the background image
background_image_path = "materials/HomepageBG.png"

# Create a PhotoImage object for the background image
background_image = PhotoImage(file=background_image_path)

# Add the background image to the canvas
canvas.create_image(0, 0, anchor="nw", image=background_image)

# Load the button images
ManageButton = PhotoImage(file='materials/ManageButton.png')
SearchPatientButton = PhotoImage(file='materials/SearchPatientButton.png')
SQLCodesButton = PhotoImage(file='materials/SQLCodesButton.png')
AboutUsButton = PhotoImage(file='materials/AboutUsButton.png')

# Resize the button images
resized_image1 = ManageButton.subsample(int(ManageButton.width() / 340), int(ManageButton.height() / 105))
resized_image2 = SearchPatientButton.subsample(int(SearchPatientButton.width() / 340), int(SearchPatientButton.height() / 105))
resized_image3 = SQLCodesButton.subsample(int(SQLCodesButton.width() / 340), int(SQLCodesButton.height() / 105))
resized_image4 = AboutUsButton.subsample(int(AboutUsButton.width() / 340), int(AboutUsButton.height() / 105))

# Create button widgets
button1 = Button(window, command=click, image=resized_image1, bd=0, relief="flat", highlightthickness=0)
button2 = Button(window, command=click, image=resized_image2, bd=0, relief="flat", highlightthickness=0)
button3 = Button(window, command=click, image=resized_image3, bd=0, relief="flat", highlightthickness=0)
button4 = Button(window, command=to_ab, image=resized_image4, bd=0, relief="flat", highlightthickness=0)

# Hovered button images
ManageButtonHover = PhotoImage(file='materials/ManageButtonHover.png')
SearchPatientButtonHover = PhotoImage(file='materials/SearchPatientButtonHover.png')
SQLCodesButtonHover = PhotoImage(file='materials/SQLCodesButtonHover.png')
AboutUsButtonHover = PhotoImage(file='materials/AboutUsButtonHover.png')

# Store resized images as attributes of button widgets
button1.resized_image = resized_image1
button1.resized_hover_image = ManageButtonHover.subsample(21, 24)

button2.resized_image = resized_image2
button2.resized_hover_image = SearchPatientButtonHover.subsample(21, 24)

button3.resized_image = resized_image3
button3.resized_hover_image = SQLCodesButtonHover.subsample(21, 24)

button4.resized_image = resized_image4
button4.resized_hover_image = AboutUsButtonHover.subsample(21, 24)

# Add the buttons to the canvas
button1_window = canvas.create_window(970, 100, anchor="nw", window=button1)
button2_window = canvas.create_window(970, 245, anchor="nw", window=button2)
button3_window = canvas.create_window(970, 390, anchor="nw", window=button3)
button4_window = canvas.create_window(970, 535, anchor="nw", window=button4)

# Event bindings for hovering effect
button1.bind('<Enter>', on_enter_manage)
button1.bind('<Leave>', on_leave_manage)
button2.bind('<Enter>', on_enter_search)
button2.bind('<Leave>', on_leave_search)
button3.bind('<Enter>', on_enter_sqlcodes)
button3.bind('<Leave>', on_leave_sqlcodes)
button4.bind('<Enter>', on_enter_about)
button4.bind('<Leave>', on_leave_about)

my_label = Label(window, text='')
my_label.pack(padx=10, pady=10)

window.mainloop()