from tkinter import *

def click():
    my_label.config(text="Button Clicked")

window = Tk()
window.geometry("1280x720")  # Set initial window size
window.resizable(width=False, height=False)  # Disable window resizing
window.title("MedData")
icon = PhotoImage(file='materials/Icon.png')
window.iconphoto(True,icon)

canvas = Canvas(window, width=1280, height=720)
canvas.pack()

# Set the path to the background image
background_image_path = "D:/ninaf/MedData/MedData/materials/SearchPatientPage.png"

# Create a PhotoImage object for the background image
background_image = PhotoImage(file=background_image_path)

# Add the background image to the canvas
canvas.create_image(0, 0, anchor="nw", image=background_image)

BackButton = PhotoImage(file='D:/ninaf/MedData/MedData/materials/BackButton.png')

# Resize the SearchPatient image
desired_width3 =160
desired_height3 = 55

resized_image3 = BackButton.subsample(int(BackButton.width() / desired_width3), int(BackButton.height() / desired_height3))

# Add the SearchPatient image to the canvas as a button
button3 = Button(window, command=click, image=resized_image3, bd=0, relief="flat", highlightthickness=0)
button3_window = canvas.create_window(1040, 620, anchor="nw", window=button3)

my_label = Label(window, text='')
my_label.pack(padx=10, pady=10)

window.mainloop()
