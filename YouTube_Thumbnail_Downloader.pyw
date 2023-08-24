import webbrowser
import requests
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def download_image():
    video_id = video_id_entry.get()
    if video_id:
        url = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
        res = requests.get(url)
        
        # Open a file dialog to choose the download directory
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        
        if file_path:
            with open(file_path, 'wb') as f:
                f.write(res.content)
            messagebox.showinfo("Download Successful", "Image downloaded successfully!")
        else:
            messagebox.showinfo("Download Cancelled", "Image download was cancelled.")
    else:
        messagebox.showwarning("Error", "Please enter a Video ID.")

def open_browser(event):
    webbrowser.open("https://github.com/ElliotCHEN37/YouTubeThumbnailDownloader")  # Replace with your desired URL

root = tk.Tk()
root.title("YouTube Thumbnail Downloader GUI v1.1")
root.geometry("600x270")  # Set the initial window size
root.resizable(False, False)  # Disable resizing

# Load and resize the image
image_path = 'logo.png'  # Replace with your image path
image = Image.open(image_path)
image = image.resize((291, 215))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo, cursor="hand2")
image_label.bind("<Button-1>", open_browser)
image_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

welcome_label = tk.Label(root, text="Welcome")
welcome_label.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

video_id_entry = tk.Entry(root, width=30)
video_id_entry.insert(0, "Enter Video ID")
video_id_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

download_button = tk.Button(root, text="Download", command=download_image, cursor="hand2")
download_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

root.mainloop()
