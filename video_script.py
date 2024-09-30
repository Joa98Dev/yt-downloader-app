'''

THIS SCRIPT MANAGE THE VIDEO DOWNLOADING FEATURES

'''

# Libraries
import tkinter as tk
from tkinter import ttk
from yt_dlp import YoutubeDL

# Manage the video tab
def _video_tab(notebook):
    video_tab = ttk.Frame(notebook)
    video_tab.video_tab_image = tk.PhotoImage(file='icons/video_icon.png')
    notebook.add(video_tab, text="Video Downloader", image=video_tab.video_tab_image, compound=tk.LEFT)

    # UI Elements
    video_url_label = tk.Label(video_tab, text="Enter Video/Playlist URL:")
    video_url_label.pack(pady=5)
    video_url_entry = tk.Entry(video_tab, width=50)
    video_url_entry.pack(pady=5)

    video_quality_label = tk.Label(video_tab, text="Select Video Quality:")
    video_quality_label.pack(pady=5)
    video_quality_var = tk.StringVar()
    video_quality_dropdown = ttk.Combobox(video_tab, textvariable=video_quality_var)
    video_quality_dropdown['values'] = ('360p', '480p', '720p', '1080p')
    video_quality_dropdown.current(3)  # Default to 1080p
    video_quality_dropdown.pack(pady=5)

    # Video download function with yt-dlp
    def download_video():
        url = video_url_entry.get()
        video_quality = video_quality_var.get()

        # Check if the URL is not empty
        if not url:
            print("Please enter a valid URL.")
            return

        # Configure yt-dlp options based on selected video quality
        ydl_opts = {
            'format': f'bestvideo[height<={video_quality}]+bestaudio/best',
            'outtmpl': f'videos/video_%(title)s_{video_quality}.mp4',
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"Downloaded video in {video_quality} quality.")
        except Exception as e:
            print(f"Error downloading video: {e}")

    # Buttons manager
    download_video_button = tk.Button(video_tab, text="Download", command=download_video)
    download_video_button.pack(pady=20)

'''
# Example to create the main window and notebook (for the sake of completeness)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("YT Downloader")
    
    notebook = ttk.Notebook(root)
    notebook.pack(expand=1, fill='both')
    
    _video_tab(notebook)
    
    root.mainloop()
'''