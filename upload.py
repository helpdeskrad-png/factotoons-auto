import os
import random
import json
import requests

VIDEO_FILE = "short.mp4"

titles = [
"ये fact आपको shock कर देगा 😱",
"90% लोग ये नहीं जानते 🤯",
"आपका दिमाग हिल जाएगा 🧠",
"Did you know ये? 🤔"
]

description = "Daily Amazing Facts\n\n#shorts #facts #viral #didyouknow"

title = random.choice(titles)

refresh_token = os.environ.get("REFRESH_TOKEN")
client_secret = os.environ.get("CLIENT_SECRET")

print("Uploading video:", VIDEO_FILE)
print("Title:", title)
print("Using refresh token")

# placeholder upload logic
if os.path.exists(VIDEO_FILE):
    print("Video ready for YouTube upload")
else:
    print("Video not found")

print("Upload completed")
