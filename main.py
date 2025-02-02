import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def convert_py_to_exe():
    # Open a file dialog to select multiple .py files
    file_paths = filedialog.askopenfilenames(title="Select Python files", filetypes=[("Python files", "*.py")])
    if file_paths:
        # Specify additional files to include
        additional_files = ["key.json"]  # Add any other files you want to include here

        # Create a setup.py file for cx_Freeze
        setup_script = f"""
from cx_Freeze import setup, Executable

setup(
    name="PythonToExeConverter",
    version="0.1",
    description="A simple GUI to convert Python scripts to executables",
    options={{'build_exe': {{'include_files': {additional_files}}}}},
    executables=[Executable(file, base=None) for file in {file_paths}]
)
"""
        # Write the setup script to a file
        with open("setup.py", "w") as f:
            f.write(setup_script)

        # Run the setup.py script to build the executables
        subprocess.run(["python", "setup.py", "build"], shell=True)
        messagebox.showinfo("Success", f"Converted {', '.join(file_paths)} and included {', '.join(additional_files)} to .exe using cx_Freeze")

# Create a simple GUI
root = tk.Tk()
root.title("Python to EXE Converter")
root.geometry("400x200")  # Set the window size
root.configure(bg="#f0f0f0")  # Set background color

# Add a title label
title_label = tk.Label(root, text="Python to EXE Converter", font=("Helvetica", 16), bg="#f0f0f0")
title_label.pack(pady=10)

# Add a convert button with styling
convert_button = tk.Button(root, text="Convert .py to .exe", command=convert_py_to_exe, 
                            bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=10, pady=5)
convert_button.pack(pady=20)

# Add a footer label
footer_label = tk.Label(root, text="Select multiple files to convert", font=("Helvetica", 10), bg="#f0f0f0")
footer_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
