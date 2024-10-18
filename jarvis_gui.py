import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import os
import sys
import pygame  
import time

def window_1():
    root = tk.Tk()
    root.title("Echo Initializing")
    window_width = 1000  
    window_height = 800  
    root.geometry(f"{window_width}x{window_height}")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.configure(bg='black')  

    pygame.mixer.init()

    gif_label = Label(root)
    gif_label.pack(fill=tk.BOTH, expand=True)  

    title_label = Label(root, text="Echo Initializing", font=("Helvetica", 24), bg='black', fg='white')
    title_label.pack(pady=20)  

    frame_folder = "frames2"  

    gif_frames = []
    for frame_file in sorted(os.listdir(frame_folder), key=lambda x: int(x.split('_')[1].split('.')[0])):
        if frame_file.endswith(".jpg"):  
            frame_path = os.path.join(frame_folder, frame_file)
            img = Image.open(frame_path)

            img_resized = img.resize((window_width, window_height), Image.LANCZOS)  
            gif_frames.append(ImageTk.PhotoImage(img_resized))

    total_frames = len(gif_frames)

    loop_count = 0  
    max_loops = 1  

    def update_gif(frame_index=0):
        nonlocal loop_count
        gif_label.config(image=gif_frames[frame_index])
        frame_index = (frame_index + 1) % total_frames

        if frame_index == 0:
            loop_count += 1

        if loop_count < max_loops:
            root.after(100, update_gif, frame_index) 
        else:
            time.sleep(0.8)
            switch_to_window_2()  

    
    root.after(0, update_gif)  

    
    def play_music():
        pygame.mixer.music.load("iron_man.mp3")  
        pygame.mixer.music.play(-1) 

    
    root.after(0, play_music)  

    
    def stop_music():
        pygame.mixer.music.stop()

    def switch_to_window_2():
        stop_music()  
        root.destroy()  

    def on_closing():
        stop_music()  
        root.destroy()  
        sys.exit()      

    root.protocol("WM_DELETE_WINDOW", on_closing)  
    root.mainloop()
