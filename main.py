'''

MAIN WINDOW

'''
import tkinter as tk
from tkinter import ttk
from audio_script import _audio_tab

def main():
    root = tk.Tk()
    root.title("YouTube Downloader")

    # Create a tab
    notebook = ttk.Notebook(root)

    # Add audio features
    _audio_tab(notebook)

    # Pack the tab into the main window
    notebook.pack(expand=True, fill='both')

    # Start Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()