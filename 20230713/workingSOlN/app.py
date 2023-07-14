import tkinter as tk
import subprocess

def search_files():
    keyword = entry.get()

    # Execute the Go program and pass the keyword as a command-line argument
    result = subprocess.run(['go', 'run', 'search.go', keyword], capture_output=True, text=True)

    # Display the search results
    search_results.delete(1.0, tk.END)  # Clear previous search results
    if result.returncode == 0:
        search_results.insert(tk.END, result.stdout)
    else:
        search_results.insert(tk.END, f"An error occurred: {result.stderr}")

# Create the GUI
root = tk.Tk()
root.title("File Search")

label = tk.Label(root, text="Enter the keyword:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Search", command=search_files)
button.pack()

search_results = tk.Text(root)
search_results.pack()

root.mainloop()

