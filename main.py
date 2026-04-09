import random
from gtts import gTTS
from PIL import Image, ImageDraw
from moviepy.editor import ImageSequenceClip, AudioFileClip, CompositeAudioClip
import numpy as np

hooks = [
"90% log ye nahi jaante...",
"Ye fact aapko shock kar dega...",
"Agar aap intelligent ho to...",
"Science ke according...",
"ये fact आपको हिला देगा...",
"आपका दिमाग घूम जाएगा..."
]

facts = [
"human brain raat ko zyada active hota hai",
"overthinking intelligent logo ki habit hoti hai",
"sleep kam ho to memory weak hoti hai",
"subah phone dekhna stress badhata hai",
"log 8 minute me interest lose kar dete hai"
]

text = random.choice(hooks) + " " + random.choice(facts)

# voice
tts = gTTS(text=text, lang='hi')
tts.save("voice.mp3")

frames = []

for i in range(20):

    img = Image.new("RGB",(1080,1920),(8,8,25))
    draw = ImageDraw.Draw(img)

    # head movement
    offset = 5 if i%2==0 else -5

    # realistic avatar head
    draw.ellipse((420+offset,200,660+offset,440), fill=(255,220,200))

    # blinking eyes
    if i % 6 == 0:
        draw.rectangle((470+offset,270,510+offset,275), fill="black")
        draw.rectangle((570+offset,270,610+offset,275), fill="black")
    else:
        draw.ellipse((470+offset,260,510+offset,300), fill="black")
        draw.ellipse((570+offset,260,610+offset,300), fill="black")

    # talking mouth
    if i%2==0:
        draw.rectangle((500+offset,330,580+offset,350), fill="red")
    else:
        draw.rectangle((500+offset,320,580+offset,370), fill="red")

    # hand movement
    if i%2==0:
        draw.rectangle((380,400,420,520), fill=(255,220,200))
    else:
        draw.rectangle((380,420,420,540), fill=(255,220,200))

    # text
    draw.text((80,700),"Did You Know?", fill=(255,255,0))
    draw.text((80,900), text, fill=(255,255,255))

    frame = f"frame_{i}.png"
    img.save(frame)
    frames.append(frame)

# thumbnail
thumb = Image.new("RGB",(1280,720),(25,0,0))
d = ImageDraw.Draw(thumb)

d.text((100,200),"SHOCKING FACT", fill=(255,255,0))
d.text((100,350), text[:60], fill=(255,255,255))

thumb.save("thumbnail.png")

# create video
voice = AudioFileClip("voice.mp3")

# background music (generated tone)
duration = voice.duration
fps = 44100
t = np.linspace(0, duration, int(fps*duration))
audio_bg = 0.02*np.sin(2*np.pi*220*t)
bg_audio = AudioFileClip("voice.mp3").volumex(0.1)

audio = CompositeAudioClip([voice, bg_audio])

clip = ImageSequenceClip(frames, fps=6)
clip = clip.set_audio(audio)

clip.write_videofile("short.mp4", fps=24)

print("Realistic animated avatar created")
