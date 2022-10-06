import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/User/ishaa/Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png','.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2','.mpeg','.mpe','.mpv', '.mp4','.m4p','.m4v','.avi','.mov'],
    "Document_Files": ['.ppt','.xis','.xisx','.csu','.pdf','.txt'],
    "Setup_Files": ['.exe','.bin','.cmd','msi','.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")
    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified!")
    def on_moved(self, event):
        print(f"Oops! Someone moved {event.src_path}!")
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running....")

except KeyboardInterrupt:
    print("stopped!")
    observer.stop()