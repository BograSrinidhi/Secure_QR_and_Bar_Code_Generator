from barcode import Code39 as code39  # Import the Code39 barcode type
from barcode.writer import ImageWriter
import qrcode
import getpass
import tkinter as tk
from tkinter import simpledialog, filedialog

def get_password():
    return getpass.getpass("Enter the password: ")

def check_password(password):
    # You can customize this function to check the entered password against a stored one.
    stored_password = "jai"  # Replace with your actual secure password
    return password == stored_password

def generate_qrcode(data, filename, password):
    if check_password(password):
        qr = qrcode.QRCode(
            version=2,  # You can adjust the version as needed
            error_correction= qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print("QR code generated successfully.")
    else:
        print("Incorrect password. Access denied.")

def generate_barcode(data, filename, password):
    if check_password(password):
        code = code39(data, writer=ImageWriter())
        code.save(filename)
        print("Barcode generated successfully.")
    else:
        print("Incorrect password. Access denied.")

def main():
    password = get_password()

    # Create Tkinter GUI
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    text_to_encode = simpledialog.askstring("Input", "Enter the text to encode:")
    if text_to_encode:
        # Generate QR code
        qrcode_filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        generate_qrcode(text_to_encode, qrcode_filename, password)

        # Generate Barcode (using Code39 from python-barcode)
        barcode_filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        generate_barcode(text_to_encode, barcode_filename, password)

if __name__ == "__main__":
    main()
