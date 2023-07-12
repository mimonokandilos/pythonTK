import tkinter as tk
import webbrowser

def search_google():
    query = entry.get()
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def show_results():
    query = entry.get()
    search_results = get_search_results(query)

    # Create a new window to display the results
    results_window = tk.Toplevel(root)
    results_window.title("Search Results")

    # Create a label for each result
    for result in search_results:
        label = tk.Label(results_window, text=result)
        label.pack()

def get_search_results(query):
    # Replace this with your own logic to retrieve search results
    # This is just a placeholder
    return ["Result 1", "Result 2", "Result 3", "Result 4", "Result 5"]

# Create the Tkinter application
root = tk.Tk()
root.title("Google Search")

# Create a label and an entry field
label = tk.Label(root, text="Enter your search query:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to trigger the search
search_button = tk.Button(root, text="Search", command=search_google)
search_button.pack()

# Create a button to show the results
results_button = tk.Button(root, text="Show Results", command=show_results)
results_button.pack()

# Start the Tkinter event loop
root.mainloop()

