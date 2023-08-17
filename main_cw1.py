import argparse
from cli import main as cli_main
from gui import hide_text_in_image_gui

def main():
    print("Steganography App")
    print("Select Mode:")
    print("1. CLI mode")
    print("2. GUI mode")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        cli_main()
    elif choice == '2':
        hide_text_in_image_gui()
    else:
        print("Invalid choice. Exiting...")

if __name__ == '__main__':
    main()
