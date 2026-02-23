import customtkinter as ctk
from PIL import Image, ImageDraw
import pystray
import threading
import sys

class ChatApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chattle")
        self.geometry("400x500")

        # UI Elements
        self.label = ctk.CTkLabel(self, text="Chatting with Friend...", font=("Arial", 20))
        self.label.pack(pady=20)
        
        self.textbox = ctk.CTkTextbox(self, width=350, height=300)
        self.textbox.pack(pady=10)

        # Handle the 'X' button click
        self.protocol("WM_DELETE_WINDOW", self.hide_window)

        # Start the System Tray in a background thread
        self.tray_thread = threading.Thread(target=self.setup_tray, daemon=True)
        self.tray_thread.start()

    #TODO: load a custom image here
    def create_menu_icon(self):
        # Create a simple 64x64 blue square icon (or load a .png)
        img = Image.new('RGB', (64, 64), color=(30, 144, 255))
        d = ImageDraw.Draw(img)
        d.rectangle([16, 16, 48, 48], fill=(255, 255, 255))
        return img

    def setup_tray(self):
        menu = pystray.Menu(
            pystray.MenuItem("Show Chattle", self.show_window),
            pystray.MenuItem("Exit", self.exit_app)
        )
        self.icon = pystray.Icon("chat_app", self.create_menu_icon(), "Chattle", menu)
        self.icon.run()

    def hide_window(self):
        self.withdraw() # Hides the window from taskbar and screen

    def show_window(self):
        self.deiconify() # Brings the window back
        self.focus_force()

    def exit_app(self):
        self.icon.stop() # Stop the tray icon
        self.destroy()   # Destroy the Tkinter window
        sys.exit()       # Kill the process

if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()