import os
import random

VIDEO_FILE = "short.mp4"

titles = [
"ये fact आपको shock कर देगा 😱",
"90% लोग ये नहीं जानते 🤯",
"आपका दिमाग हिल जाएगा 🧠",
"ये सच है और shocking भी 😳",
"Did you know ये? 🤔"
]

hashtags = "#shorts #facts #viral #didyouknow #hindifacts"

title = random.choice(titles)

if os.path.exists(VIDEO_FILE):
    print("Uploading:", VIDEO_FILE)
    print("Title:", title)
    print("Tags:", hashtags)
else:
    print("Video not found")

print("Auto upload ready")
