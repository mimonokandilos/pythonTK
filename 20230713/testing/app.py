import tkinter as tk
import subprocess

def open_location(event):
    line_start = search_results.index('current linestart')
    line_end = search_results.index('current lineend')
    path = search_results.get(line_start, line_end).split(' - ')[-1]
    subprocess.run(['open', '-R', path])

def search_files():
    keyword = entry.get()

    # Execute the Go program and pass the keyword as a command-line argument
    result = subprocess.run(['go', 'run', 'search.go', keyword], capture_output=True, text=True)

    # Display the search results
    search_results.delete(1.0, tk.END)  # Clear previous search results
    if result.returncode == 0:
        output_lines = result.stdout.splitlines()
        for line in output_lines:
            path_start_index = line.rindex(":") + 2
            path = line[path_start_index:]
            search_results.insert(tk.END, line + '\n')
            search_results.tag_add('clickable', f'{search_results.index(tk.END)}-{len(path) + 1}l')
    else:
        search_results.insert(tk.END, f"An error occurred: {result.stderr}")

def init_tags():
    search_results.tag_configure('clickable', foreground='blue', underline=True)

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

init_tags()
search_results.bind('<Button-1>', open_location)

root.mainloop()

