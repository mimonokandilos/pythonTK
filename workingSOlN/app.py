import tkinter as tk
import subprocess
from tkinter import ttk
import threading

def open_finder_location(file_path):
    try:
        subprocess.run(['open', '-R', file_path])
    except Exception as e:
        print(f"Error opening file location: {e}")

def search_files():
    keyword = entry.get()

    # Execute the Go program and pass the keyword as a command-line argument
    result = subprocess.run(['go', 'run', 'search.go', keyword], capture_output=True, text=True)

    # Display the search results
    search_results.delete(1.0, tk.END)  # Clear previous search results
    if result.returncode == 0:
        lines = result.stdout.strip().split('\n')
        for line in lines:
            # Extract filename and file path from the line
            parts = line.strip().split(' - ')
            if len(parts) == 3 and parts[0] == "Keyword found in file: true":
                filename = parts[1].split(": ")[1]
                file_path = parts[2].split(": ")[1]
                search_results.insert(tk.END, f"File: {filename}\nPath: {file_path}\n")
                # Create a button next to each search result to open the Finder location
                button = tk.Button(frame_file_search, text="Open in Finder", command=lambda fp=file_path: open_finder_location(fp))
                search_results.window_create(tk.END, window=button)
                search_results.insert(tk.END, "\n")
            else:
                search_results.insert(tk.END,"No Results Found!")
    else:
        search_results.insert(tk.END, f"An error occurred: {result.stderr}\n")

def run_nmap():
    ip_address = entry_nmap.get()
    nmap_range = entry_nmap_range.get()

    # Execute the Go program for nmap and capture its output
    nmap_output = subprocess.run(['go', 'run', 'nmap.go', ip_address, nmap_range], capture_output=True, text=True)
    
    # Display the nmap scan results
    text_nmap.delete(1.0, tk.END)
    text_nmap.insert(tk.END, nmap_output.stdout)
    
def start_nmap_thread():
    nmap_thread = threading.Thread(target=run_nmap)
    nmap_thread.start()
    
# Create the GUI
root = tk.Tk()
root.title("File Search and nmap")

# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Create tabs
tab_file_search = ttk.Frame(notebook)
tab_nmap = ttk.Frame(notebook)

notebook.add(tab_file_search, text='File Search')
notebook.add(tab_nmap, text='nmap')

# File Search Tab
frame_file_search = tk.Frame(tab_file_search)
frame_file_search.pack(padx=10, pady=10)

label = tk.Label(frame_file_search, text="Enter the keyword:")
label.pack()

entry = tk.Entry(frame_file_search)
entry.pack()

button = tk.Button(frame_file_search, text="Search", command=search_files)
button.pack()

search_results = tk.Text(frame_file_search)
search_results.pack()

# nmap Tab
frame_nmap = tk.Frame(tab_nmap)
frame_nmap.pack(padx=10, pady=10)

label_nmap = tk.Label(frame_nmap, text="Enter IP Address:")
label_nmap.pack()

entry_nmap = tk.Entry(frame_nmap)
entry_nmap.pack()

label_nmap_range = tk.Label(frame_nmap, text="Enter Port Range:")
label_nmap_range.pack()

entry_nmap_range = tk.Entry(frame_nmap)
entry_nmap_range.pack()

button_nmap = tk.Button(frame_nmap, text="Scan with nmap", command=start_nmap_thread)
button_nmap.pack()

text_nmap = tk.Text(frame_nmap)
text_nmap.pack()

root.mainloop()

