import tkinter as tk
import subprocess

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
                button = tk.Button(root, text="Open in Finder", command=lambda fp=file_path: open_finder_location(fp))
                search_results.window_create(tk.END, window=button)
                search_results.insert(tk.END, "\n")
    else:
        search_results.insert(tk.END, f"An error occurred: {result.stderr}\n")

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

