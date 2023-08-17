import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from stegano import lsb

def hide_text_in_image_gui():
    def hide_text_in_image():
        # Ask for a phrase to hide
        phrase = input_entry.get()

        # Open file dialog to choose an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])

        # Load the image
        image = Image.open(file_path)

        # Hide the text in the image using steganography
        steganography_image = lsb.hide(image, phrase)

        # Save the steganography image
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        steganography_image.save(save_path)

        # Display success message
        messagebox.showinfo("Success", "Text hidden in the image!")

    def decode_image():
        # Open file dialog to choose an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])

        # Load the steganography image
        steganography_image = Image.open(file_path)

        # Decode the hidden text from the steganography image
        hidden_text = lsb.reveal(steganography_image)

        # Display the hidden text
        messagebox.showinfo("Decoded Text", hidden_text)

    # Create the main window
    window = tk.Tk()
    window.title("Steganography App")

    # Create the label for the phrase input
    input_label = tk.Label(window, text="Enter the phrase to hide:")
    input_label.pack()

    # Create the input entry for the phrase
    input_entry = tk.Entry(window)
    input_entry.pack()

    # Create the button to trigger image upload and text hiding
    hide_button = tk.Button(window, text="Hide Text in Image", command=hide_text_in_image)
    hide_button.pack()

    # Create the button to trigger image decoding
    decode_button = tk.Button(window, text="Decode Image", command=decode_image)
    decode_button.pack()

    # Start the GUI main loop
    window.mainloop()
