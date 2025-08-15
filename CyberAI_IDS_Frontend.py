import tkinter as tk
from tkinter import messagebox

# Functions for each button
def scan():
    messagebox.showinfo("Scan", "Scanning started...")

def threats():
    messagebox.showinfo("Threats", "No threats found!")

def database():
    messagebox.showinfo("Database", "Database accessed successfully.")

def exit_app():
    root.destroy()

# Main window
root = tk.Tk()
root.title("CyberAI_IDS")
root.geometry("300x250")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="CyberAI_IDS", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Buttons
scan_button = tk.Button(root, text="Scan", width=15, height=2, command=scan)
scan_button.pack(pady=5)

threats_button = tk.Button(root, text="Threats", width=15, height=2, command=threats)
threats_button.pack(pady=5)

database_button = tk.Button(root, text="Database", width=15, height=2, command=database)
database_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", width=15, height=2, command=exit_app, bg="red", fg="white")
exit_button.pack(pady=5)

root.mainloop()
