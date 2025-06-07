import tkinter as tk
from tkinter import filedialog
import vlc
import time
import threading

class VLCPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python VLC Player")

        # VLC setup
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # UI Components
        self.build_ui()
        self.update_time_thread = threading.Thread(target=self.update_time)
        self.update_time_thread.daemon = True
        self.update_time_thread.start()

    def build_ui(self):
        # Buttons
        tk.Button(self.root, text="Open File", command=self.open_file).pack()

        self.play_pause_btn = tk.Button(self.root, text="Play", command=self.toggle_play_pause)
        self.play_pause_btn.pack()

        tk.Button(self.root, text="Stop", command=self.stop).pack()

        # Volume
        self.volume_slider = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL,
                                      label="Volume", command=self.set_volume)
        self.volume_slider.set(70)
        self.volume_slider.pack()

        # Seek
        self.seek_slider = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL,
                                    label="Seek (%)", command=self.set_position)
        self.seek_slider.pack()

        # Time info
        self.time_label = tk.Label(self.root, text="00:00 / 00:00")
        self.time_label.pack()

        # Fullscreen toggle
        tk.Button(self.root, text="Toggle Fullscreen", command=self.toggle_fullscreen).pack()

        # Subtitles toggle
        tk.Button(self.root, text="Toggle Subtitles", command=self.toggle_subtitles).pack()

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            media = self.instance.media_new(file_path)
            self.player.set_media(media)
            self.player.play()
            time.sleep(0.5)  # Allow time for media to load
            self.play_pause_btn.config(text="Pause")

    def toggle_play_pause(self):
        if self.player.is_playing():
            self.player.pause()
            self.play_pause_btn.config(text="Play")
        else:
            self.player.play()
            self.play_pause_btn.config(text="Pause")

    def stop(self):
        self.player.stop()
        self.play_pause_btn.config(text="Play")

    def set_volume(self, val):
        self.player.audio_set_volume(int(val))

    def set_position(self, val):
        pos = float(val) / 100
        self.player.set_position(pos)

    def update_time(self):
        while True:
            if self.player.is_playing():
                current = self.player.get_time() // 1000
                total = self.player.get_length() // 1000
                time_str = f"{self.format_time(current)} / {self.format_time(total)}"
                self.time_label.config(text=time_str)

                try:
                    pos_percent = self.player.get_position() * 100
                    self.seek_slider.set(pos_percent)
                except:
                    pass
            time.sleep(1)

    def format_time(self, seconds):
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02d}:{secs:02d}"

    def toggle_fullscreen(self):
        self.player.set_fullscreen(not self.player.get_fullscreen())

    def toggle_subtitles(self):
        current_spu = self.player.video_get_spu()
        if current_spu == -1 or current_spu == 0:
            self.player.video_set_spu(1)  # Enable
        else:
            self.player.video_set_spu(0)  # Disable


if __name__ == "__main__":
    root = tk.Tk()
    app = VLCPlayer(root)
    root.mainloop()
