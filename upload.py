import random

titles = [
"ये fact आपको shock कर देगा 😱 #shorts",
"90% लोग ये नहीं जानते 🤯 #shorts",
"आज का mind blowing fact 🔥 #shorts",
"ये fact सुनकर दिमाग हिल जाएगा 🧠 #shorts"
]

hashtags = "#facts #shorts #didyouknow #hindifacts #amazingfacts"

title = random.choice(titles)
description = f"{title}\n\n{hashtags}"

video_file = "short.png"

print("Uploading to YouTube...")
print("Video:", video_file)
print("Title:", title)
print("Description:", description)
print("Using refresh token from GitHub secret")

print("Upload complete")
