import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from stegano import lsb

def hide_text_in_image_cli():
    # Ask for a phrase to hide
    phrase = input("Enter the phrase to hide: ")

    # Open file dialog to choose an image file
    file_path = input("Enter the path to the image file: ")

    # Load the image
    image = Image.open(file_path)

    # Hide the text in the image using steganography
    steganography_image = lsb.hide(image, phrase)

    # Ask for the new file name for the steganography image
    new_file_name = input("Enter the new file name for the steganography image (with extension): ")
    save_path = new_file_name

    # Save the steganography image
    steganography_image.save(save_path)

    print(f"Text hidden in the image. Saved as {save_path}")


def decode_image_cli():
    # Ask for the path to the steganography image file
    file_path = input("Enter the path to the steganography image file: ")

    # Load the steganography image
    steganography_image = Image.open(file_path)

    # Decode the hidden text from the steganography image
    hidden_text = lsb.reveal(steganography_image)

    if hidden_text:
        print("Hidden Text:", hidden_text)
    else:
        print("No hidden text found in the steganography image.")


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
    upload_button = tk.Button(window, text="Hide Text in Image", command=hide_text_in_image)
    upload_button.pack()

    # Start the GUI main loop
    window.mainloop()


def decode_image_gui():
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

    # Create the button to trigger image upload and decoding
    decode_button = tk.Button(window, text="Decode Image", command=decode_image)
    decode_button.pack()

    # Start the GUI main loop
    window.mainloop()


def main():
    # Ask for the mode choice
    mode_choice = input("Enter your choice (1 for CLI, 2 for GUI): ")

    if mode_choice == '1':
        print("Running in CLI mode...")
        menu = '''
        Menu:
        1. Hide text in an image
        2. Decode hidden text from a steganography image
        '''

        print(menu)
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            hide_text_in_image_cli()
        elif choice == '2':
            decode_image_cli()
        else:
            print("Invalid choice. Exiting...")

    elif mode_choice == '2':
        print("Running in GUI mode...")
        # Create the main window
        window = tk.Tk()
        window.title("Steganography App")

        # Create the label for the mode selection
        mode_label = tk.Label(window, text="Select Mode:")
        mode_label.pack()

        # Create the button to hide text
        hide_text_button = tk.Button(window, text="Hide text in an image", command=hide_text_in_image_gui)
        hide_text_button.pack()

        # Create the button to reveal text
        decode_text_button = tk.Button(window, text="Decode hidden text from a steganography image", command=decode_image_gui)
        decode_text_button.pack()

        # Start the GUI main loop
        window.mainloop()

    else:
        print("Invalid choice. Exiting...")


if __name__ == '__main__':
    main()
