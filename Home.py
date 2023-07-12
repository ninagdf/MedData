from tkinter import *

def click():
    my_label.config(text="Button Clicked")

window = Tk()
window.geometry("1280x720")  # Set initial window size
window.resizable(width=False, height=False)  # Disable window resizing

canvas = Canvas(window, width=1280, height=720)
canvas.pack()

# Set the path to the background image
background_image_path = "D:/ninaf/MedData/materials/HomepageBG.png"

# Create a PhotoImage object for the background image
background_image = PhotoImage(file=background_image_path)

# Add the background image to the canvas
canvas.create_image(0, 0, anchor="nw", image=background_image)

# Set the Poppins font and font size
font_name = "Poppins"
font_size = 75

# Add the "MedData" text to the canvas
canvas.create_text(90, 250, text="MedData", font=(font_name, font_size), fill="#05066D", anchor="nw")

ManageButton = PhotoImage(file='D:/ninaf/MedData/materials/ManageButton.png')
SearchPatientButton = PhotoImage(file='D:/ninaf/MedData/materials/SearchPatientButton.png')
AboutUsButton = PhotoImage(file='D:/ninaf/MedData/materials/AboutUsButton.png')

# Resize the ManageButton image
desired_width1 = 350
desired_height1 = 115

resized_image1 = ManageButton.subsample(int(ManageButton.width() / desired_width1), int(ManageButton.height() / desired_height1))

# Add the ManageButton image to the canvas as a button
button1 = Button(window, command=click, image=resized_image1, bd=0, relief="flat", highlightthickness=0)
button1_window = canvas.create_window(735, 100, anchor="nw", window=button1)

# Resize the SearchPatientButton image
desired_width2 = 350
desired_height2 = 115

resized_image2 = SearchPatientButton.subsample(int(SearchPatientButton.width() / desired_width2), int(SearchPatientButton.height() / desired_height2))

# Add the SearchPatientButton image to the canvas as a button
button2 = Button(window, command=click, image=resized_image2, bd=0, relief="flat", highlightthickness=0)
button2_window = canvas.create_window(735, 260, anchor="nw", window=button2)

# Resize the AboutUsButton image
desired_width3 = 350
desired_height3 = 115

resized_image3 = AboutUsButton.subsample(int(AboutUsButton.width() / desired_width3), int(AboutUsButton.height() / desired_height3))

# Add the AboutUsButton image to the canvas as a button
button3 = Button(window, command=click, image=resized_image3, bd=0, relief="flat", highlightthickness=0)
button3_window = canvas.create_window(735, 420, anchor="nw", window=button3)

my_label = Label(window, text='')
my_label.pack(padx=10, pady=10)

window.mainloop()
