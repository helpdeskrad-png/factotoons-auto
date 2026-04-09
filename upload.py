import os
import random

VIDEO_FILE = "short.mp4"

titles = [
"ये fact आपको shock कर देगा 😱",
"90% लोग ये नहीं जानते 🤯",
"ये सच है और shocking भी 😳",
"आपका दिमाग हिल जाएगा 🧠",
"Did you know ये? 🤔"
]

description = """
Daily Amazing Facts

#shorts #facts #viral #didyouknow #hindifacts
"""

title = random.choice(titles)

if os.path.exists(VIDEO_FILE):
    print("Uploading video:", VIDEO_FILE)
    print("Title:", title)
    print("Description:", description)
else:
    print("Video not found")

print("Upload finished")
