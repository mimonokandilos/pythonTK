import tkinter as tk
import subprocess

def button_press():
    # Invoke the Go code using subprocess
    subprocess.run(["go", "run", "go_code.go"])

# Create the Tkinter application
root = tk.Tk()
root.title("Python Tkinter and Go Integration")

# Create a button
button = tk.Button(root, text="Click Me", command=button_press)
button.pack()

# Start the Tkinter event loop
root.mainloop()

