import tkinter as tk
import webbrowser

def search_google():
    query = entry.get()
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

# Create the Tkinter application
root = tk.Tk()
root.title("Google Search")

# Create a label and an entry field
label = tk.Label(root, text="Enter your search query:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to trigger the search
button = tk.Button(root, text="Search", command=search_google)
button.pack()

# Start the Tkinter event loop
root.mainloop()

