import json
from difflib import get_close_matches
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Load the dictionary JSON file
try:
    with open(r"C:\Users\SAKSHI CHOUDHARY\OneDrive\Desktop - Copy\data (1).json") as file:
        dictionary = json.load(file)
except FileNotFoundError:
    messagebox.showerror("Error", "Dictionary file not found.")
    exit()

# Function to search the meaning
def search_meaning():
    word = entry.get().lower()
    result_box.delete(1.0, tk.END)  # Clear previous result

    if word in dictionary:
        meanings = dictionary[word]
        if isinstance(meanings, list):
            for meaning in meanings:
                result_box.insert(tk.END, f"- {meaning}\n")
        else:
            result_box.insert(tk.END, f"- {meanings}")
    elif len(get_close_matches(word, dictionary.keys(), cutoff=0.8)) > 0:
        suggestion = get_close_matches(word, dictionary.keys())[0]
        answer = messagebox.askyesno("Did you mean?", f"Did you mean '{suggestion}'?")
        if answer:
            meanings = dictionary[suggestion]
            if isinstance(meanings, list):
                for meaning in meanings:
                    result_box.insert(tk.END, f"- {meaning}\n")
            else:
                result_box.insert(tk.END, f"- {meanings}")
        else:
            result_box.insert(tk.END, "Word not found. Please check spelling.")
    else:
        result_box.insert(tk.END, "Sorry, word not found in dictionary.")

# GUI setup
root = tk.Tk()
root.title("English Dictionary")
root.geometry("500x400")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter Word:", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=5)

search_btn = tk.Button(root, text="Search Meaning", font=("Arial", 12), command=search_meaning)
search_btn.pack(pady=10)

result_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
result_box.pack(pady=10)

# Run the GUI loop
root.mainloop()
