import os
import tkinter as tk

def search_files():
    search_term = entry.get()
    search_results.delete(1.0, tk.END)  # Clear previous search results
    
    for root, dirs, files in os.walk('/'):  # Traverse the entire file system
        for file in files:
            file_path = os.path.join(root, file)
            if len(file) == int(search_term):
                search_results.insert(tk.END, file_path + '\n')

# Create the GUI
root = tk.Tk()
root.title("File Search")

label = tk.Label(root, text="Enter the number of characters:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Search", command=search_files)
button.pack()

search_results = tk.Text(root)
search_results.pack()

root.mainloop()

