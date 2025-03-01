import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from cryptography.fernet import Fernet
import base64

def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32)[:32].encode())

def hide_text(image_path, text, password, output_path):
    try:
        image = Image.open(image_path).convert("RGB")
        encoded_image = image.copy()

        # Encrypt the text
        key = generate_key(password)
        cipher = Fernet(key)
        encrypted_text = cipher.encrypt(text.encode())

        # Convert encrypted text to binary
        binary_text = ''.join(format(byte, '08b') for byte in encrypted_text)
        binary_text += '1111111111111110'  # Delimiter

        # Embed the binary text into the image
        pixels = list(encoded_image.getdata())
        binary_index = 0

        for i in range(len(pixels)):
            pixel = list(pixels[i])
            for j in range(3):  # Only modify RGB values
                if binary_index < len(binary_text):
                    pixel[j] = pixel[j] & ~1 | int(binary_text[binary_index])
                    binary_index += 1
            pixels[i] = tuple(pixel)
            if binary_index >= len(binary_text):
                break

        if binary_index < len(binary_text):
            raise ValueError("The image is too small to hold the provided text.")

        encoded_image.putdata(pixels)
        encoded_image.save(output_path, format="PNG")
        messagebox.showinfo("Success", f"Text successfully hidden in {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def retrieve_text(image_path, password):
    try:
        image = Image.open(image_path).convert("RGB")
        pixels = list(image.getdata())

        # Extract binary text
        binary_text = ''
        for pixel in pixels:
            for color in pixel[:3]:  # Only read RGB values
                binary_text += str(color & 1)

            # Check for the delimiter periodically to avoid unnecessary processing
            if len(binary_text) >= 16 and '1111111111111110' in binary_text[-16:]:
                break

        # Locate the delimiter 
        delimiter = '1111111111111110'
        if delimiter in binary_text:
            binary_text = binary_text[:binary_text.index(delimiter)]
        else:
            messagebox.showerror("Error", "No hidden text found or corrupted data.")
            return

        # Convert binary data to bytes
        encrypted_text = bytes(int(binary_text[i:i+8], 2) for i in range(0, len(binary_text), 8))

        # Decrypt the text
        key = generate_key(password)
        cipher = Fernet(key)
        decrypted_text = cipher.decrypt(encrypted_text).decode()
        messagebox.showinfo("Hidden Text", decrypted_text)
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {str(e)}")

def browse_file(entry_widget):
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, filepath)

def save_file(entry_widget):
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, filepath)

def hide_text_gui():
    def on_hide():
        image_path = image_entry.get()
        text = text_entry.get()
        password = password_entry.get()
        output_path = output_entry.get()

        if not image_path or not text or not password or not output_path:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        hide_text(image_path, text, password, output_path)

    hide_window = tk.Toplevel()
    hide_window.title("Hide Text in Image")

    tk.Label(hide_window, text="Image Path:").grid(row=0, column=0, padx=5, pady=5)
    image_entry = tk.Entry(hide_window, width=50)
    image_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(hide_window, text="Browse", command=lambda: browse_file(image_entry)).grid(row=0, column=2, padx=5, pady=5)

    tk.Label(hide_window, text="Text to Hide:").grid(row=1, column=0, padx=5, pady=5)
    text_entry = tk.Entry(hide_window, width=50)
    text_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

    tk.Label(hide_window, text="Password:").grid(row=2, column=0, padx=5, pady=5)
    password_entry = tk.Entry(hide_window, show="*", width=50)
    password_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

    tk.Label(hide_window, text="Output Path:").grid(row=3, column=0, padx=5, pady=5)
    output_entry = tk.Entry(hide_window, width=50)
    output_entry.grid(row=3, column=1, padx=5, pady=5)
    tk.Button(hide_window, text="Save As", command=lambda: save_file(output_entry)).grid(row=3, column=2, padx=5, pady=5)

    tk.Button(hide_window, text="Hide Text", command=on_hide).grid(row=4, column=0, columnspan=3, pady=10)

def retrieve_text_gui():
    def on_retrieve():
        image_path = image_entry.get()
        password = password_entry.get()

        if not image_path or not password:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        retrieve_text(image_path, password)

    retrieve_window = tk.Toplevel()
    retrieve_window.title("Retrieve Text from Image")

    tk.Label(retrieve_window, text="Image Path:").grid(row=0, column=0, padx=5, pady=5)
    image_entry = tk.Entry(retrieve_window, width=50)
    image_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(retrieve_window, text="Browse", command=lambda: browse_file(image_entry)).grid(row=0, column=2, padx=5, pady=5)

    tk.Label(retrieve_window, text="Password:").grid(row=1, column=0, padx=5, pady=5)
    password_entry = tk.Entry(retrieve_window, show="*", width=50)
    password_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

    tk.Button(retrieve_window, text="Retrieve Text", command=on_retrieve).grid(row=2, column=0, columnspan=3, pady=10)

def main():
    root = tk.Tk()
    root.title("Steganography Tool")

    tk.Label(root, text="Choose an option:", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="Hide Text in Image", width=25, command=hide_text_gui).pack(pady=5)
    tk.Button(root, text="Retrieve Text from Image", width=25, command=retrieve_text_gui).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
