import random
from gtts import gTTS
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont

facts = [
"Aapka brain raat ko zyada active hota hai",
"Human body me 206 bones hoti hai",
"Overthinking intelligent logo ki habit hoti hai",
"Sleep kam ho to memory weak hoti hai",
"90% log phone use karte waqt time bhool jate hai"
]

text = random.choice(facts)

# create voice
tts = gTTS(text=text, lang='hi')
tts.save("voice.mp3")

# create image
img = Image.new("RGB",(1080,1920),(0,0,0))
draw = ImageDraw.Draw(img)
draw.text((100,900), text, fill=(255,255,255))
img.save("frame.png")

# create video
audio = AudioFileClip("voice.mp3")
clip = ImageClip("frame.png").set_duration(audio.duration)
video = clip.set_audio(audio)

video.write_videofile("short.mp4", fps=24)

print("video created")
