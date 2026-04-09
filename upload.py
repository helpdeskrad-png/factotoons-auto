import random

titles = [
"ये fact आपको shock कर देगा 😱 #shorts",
"90% लोग ये नहीं जानते 🤯 #shorts",
"आज का mind blowing fact 🔥 #shorts",
"ये fact सुनकर दिमाग हिल जाएगा 🧠 #shorts"
]

title = random.choice(titles)

description = """
Amazing facts daily

#facts #shorts #didyouknow #hindifacts
"""

print("Uploading to YouTube...")
print("Title:", title)
print("Description:", description)

# placeholder for upload
video_file = "short.png"

print("Video ready:", video_file)
print("Upload completed")
