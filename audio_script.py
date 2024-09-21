'''

THIS SCRIPT MANAGE THE AUDIO DOWNLOADING FEATURES

'''

# Libraries
import os
import re
import moviepy.editor as mp
from yt_dlp import YoutubeDL
import tkinter as tk
from tkinter import ttk

def _audio_tab(notebook):
    audio_tab = ttk.Frame(notebook)
    notebook.add(audio_tab, text="Audio Downloader")

    # Audio Link Manager
    url_label = tk.Label(audio_tab, text="Enter Video/Playlist URL:")
    url_label.pack(pady=5)
    url_entry = tk.Entry(audio_tab, width=50)
    url_entry.pack(pady=5)

    # Audio Quality Selector
    audio_quality_label = tk.Label(audio_tab, text="Select Audio Quality:")
    audio_quality_label.pack(pady=5)
    audio_quality_var = tk.StringVar()
    audio_quality_dropdown = ttk.Combobox(audio_tab, textvariable=audio_quality_var)
    audio_quality_dropdown['values'] = ('128', '192', '256', '320')
    audio_quality_dropdown.current(1)
    audio_quality_dropdown.pack(pady=5)

    def playlist_downloader():
        playlist_url = url_entry.get()
        quality = audio_quality_var.get()

        ydlp_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : quality,
            }],
            'outtmpl' : 'downloads/%(title)s.%(ext)s',
        }

        with YoutubeDL(ydlp_opts) as ydl:
            ydl.download([playlist_url])
        
        folder = "downloads"
        for file in os.listdir(folder):
            if re.search(r'\.webm\.mp4', file):
                audio_path = os.path.join(folder, file)
                mp3_path = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(audio_path)
                new_file.write_audiofile(mp3_path)
                os.remove(audio_path)
        
        print("Audio download complete!")

    download_audio_button = tk.Button(audio_tab, text="Download", command=playlist_downloader)
    download_audio_button.pack(pady=20)