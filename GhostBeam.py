import tkinter as tk
import pyfiglet
import random
import time
import threading
from colorama import init

# Initialize Colorama for color output
init(autoreset=True)

# UI Setup
root = tk.Tk()
root.title("Ghost Beam")
root.geometry("900x600")
root.configure(bg="black")

# ASCII Art Title (Now Purple)
ascii_art = pyfiglet.figlet_format("GHOST BEAM", font="basic")
ascii_label = tk.Label(root, text=ascii_art, fg="purple", bg="black", font=("Courier", 12), justify="left")
ascii_label.pack()

# Text Output Box (Resized)
output_text = tk.Text(root, height=15, width=100, bg="black", fg="lime", font=("Courier", 12), wrap=tk.WORD)
output_text.pack()

# Message at the Bottom
footer_label = tk.Label(root, text="Made by zktrade on Discord", fg="yellow", bg="black", font=("Courier", 10))
footer_label.pack(side="bottom", pady=5)

# Function to toggle fullscreen when F11 is pressed
def toggle_fullscreen(event=None):
    is_fullscreen = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not is_fullscreen)

def end_fullscreen(event=None):
    root.attributes('-fullscreen', False)

# Bind F11 to toggle fullscreen
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', end_fullscreen)  # Escape to exit fullscreen

def update_text(message, delay=0.1):
    output_text.insert(tk.END, message + "\n")
    output_text.see(tk.END)
    root.update()
    time.sleep(delay)

def fake_hack_sequence():
    update_text("Initializing Ghost Protocol...", 0.5)
    update_text("[+] Connecting to deep web relays...", 0.3)
    update_text("[+] Bypassing multiple firewall layers...", 0.2)
    update_text("[+] Engaging rootkit deployment...", 0.3)
    update_text("[+] Extracting encrypted blockchain data...")
    
    fake_data = [
        "Interfacing with quantum algorithms...",
        "Breaking SHA-512 encryption...",
        "Intercepting classified transmissions...",
        "Deploying neural network intrusion...",
        "Activating hyper-threaded attack modules..."
    ]
    
    for _ in range(10):
        update_text(f"[{random.randint(10000, 99999)}] {random.choice(fake_data)}", random.uniform(0.1, 0.4))
    
    update_text("\n[WARNING] FEDERAL TRACE DETECTED! MASKING LOCATION...", 1)
    update_text("[+] Location spoofed. Secure connection reestablished.", 2)
    
    update_text("\n[!!!] SYSTEM SELF-DESTRUCT SEQUENCE INITIATED! 10 SECONDS REMAIN!", 1)
    for i in range(10, 0, -1):
        update_text(f" >> {i} seconds remaining...", 1)
    
    update_text("\n[+] Self-destruct overridden. Connection secured.")
    update_text("[+] Ghost Beam operation complete.")
    update_text("\n[+] Closing session...", 1)

def start_hack():
    threading.Thread(target=fake_hack_sequence, daemon=True).start()

# Frame for buttons with vertical spacing
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

# Start Hack Button (Green, on Top)
start_button = tk.Button(button_frame, text="START HACK", command=start_hack, fg="black", bg="green", font=("Courier", 14, "bold"), width=20, height=2)
start_button.grid(row=0, column=0, pady=10)

# Clear Output Button (Yellow, in Middle)
clear_button = tk.Button(button_frame, text="CLEAR OUTPUT", command=lambda: output_text.delete(1.0, tk.END), fg="black", bg="yellow", font=("Courier", 12, "bold"), width=20, height=2)
clear_button.grid(row=1, column=0, pady=10)

# Exit Button (Red, on Bottom)
exit_button = tk.Button(button_frame, text="EXIT", command=root.quit, fg="black", bg="red", font=("Courier", 12, "bold"), width=20, height=2)
exit_button.grid(row=2, column=0, pady=10)

root.mainloop()
