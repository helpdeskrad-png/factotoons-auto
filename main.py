import random
from gtts import gTTS
from PIL import Image, ImageDraw
from moviepy.editor import ImageSequenceClip, AudioFileClip

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

tts = gTTS(text=text, lang='hi')
tts.save("voice.mp3")

frames = []

for i in range(24):

    zoom = i*2

    img = Image.new("RGB",(1080,1920),(8,8,30))
    draw = ImageDraw.Draw(img)

    offset = 5 if i%2==0 else -5

    # avatar
    draw.ellipse((420+offset-zoom,200-zoom,660+offset+zoom,440+zoom),
                 fill=(255,220,200))

    # blinking
    if i%6==0:
        draw.rectangle((470+offset,270,510+offset,275), fill="black")
        draw.rectangle((570+offset,270,610+offset,275), fill="black")
    else:
        draw.ellipse((470+offset,260,510+offset,300), fill="black")
        draw.ellipse((570+offset,260,610+offset,300), fill="black")

    # mouth
    if i%2==0:
        draw.rectangle((500+offset,330,580+offset,350), fill="red")
    else:
        draw.rectangle((500+offset,320,580+offset,370), fill="red")

    # animated subtitles
    y = 900 + (i%3)*3

    draw.text((80,700),"Did You Know?", fill=(255,255,0))
    draw.text((80,y), text, fill=(255,255,255))

    frame = f"frame_{i}.png"
    img.save(frame)
    frames.append(frame)

audio = AudioFileClip("voice.mp3")

clip = ImageSequenceClip(frames, fps=8)
clip = clip.set_audio(audio)

clip.write_videofile("short.mp4", fps=24)

print("Ultra viral video created")
