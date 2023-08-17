from PIL import Image
from stegano import lsb

def hide_text_in_image_cli():
    # Ask for a phrase to hide
    phrase = input("Enter the phrase to hide: ")

    while True:
        # Open file dialog to choose an image file
        file_path = input("Enter the path to the image file (or 'q' to quit): ")

        if file_path == 'q':
            break

        try:
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
        except FileNotFoundError:
            print("Invalid file path. Please try again.")

def decode_image_cli():
    while True:
        # Ask for the path to the steganography image file
        file_path = input("Enter the path to the steganography image file (or 'q' to quit): ")

        if file_path == 'q':
            break

        try:
            # Load the steganography image
            steganography_image = Image.open(file_path)

            # Decode the hidden text from the steganography image
            hidden_text = lsb.reveal(steganography_image)

            if hidden_text:
                print("Hidden Text:", hidden_text)
            else:
                print("No hidden text found in the steganography image.")
        except FileNotFoundError:
            print("Invalid file path. Please try again.")

def main():
    print("Running in CLI mode...")
    
    while True:
        menu = '''
        Menu:
        1. Hide text in an image
        2. Decode hidden text from a steganography image
        '''

        print(menu)
        choice = input("Enter your choice (1 or 2, or 'q' to quit): ")

        if choice == '1':
            hide_text_in_image_cli()
        elif choice == '2':
            decode_image_cli()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
