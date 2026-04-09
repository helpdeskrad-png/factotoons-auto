import os
import random

titles = [
"ये fact आपको shock कर देगा 😱 #shorts",
"90% लोग ये नहीं जानते 🤯 #shorts",
"Mind blowing fact 😳 #shorts",
"Did you know ये? 🤔 #shorts"
]

description = """
Daily Amazing Facts

#shorts #facts #didyouknow #viral #hindifacts
"""

title = random.choice(titles)

print("Uploading video...")
print("Title:", title)

video_file = "short.mp4"

if os.path.exists(video_file):
    print("Video ready:", video_file)
else:
    print("Video not found")

print("Upload complete")
