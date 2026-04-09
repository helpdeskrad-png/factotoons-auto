import random
from gtts import gTTS
from PIL import Image, ImageDraw
from moviepy.editor import ImageClip, AudioFileClip

hooks = [
"90% log ye nahi jaante...",
"Ye fact aapko shock kar dega...",
"Agar aap intelligent ho to...",
"Science ke according...",
"Ye sach hai aur shocking bhi...",
"ये fact आपको हिला देगा...",
"आपका दिमाग घूम जाएगा...",
"ये सच है और shocking है..."
]

facts = [
"human brain raat ko zyada active hota hai",
"overthinking intelligent logo ki habit hoti hai",
"sleep kam ho to memory weak hoti hai",
"90% log phone use karte waqt time bhool jate hai",
"subah uthte hi phone dekhna stress badhata hai",
"dimag 2x fast kaam karta hai jab aap thake hote ho",
"log 8 minute me interest lose kar dete hai",
"brain negative cheeze jaldi yaad rakhta hai"
]

text = random.choice(hooks) + " " + random.choice(facts)

tts = gTTS(text=text, lang='hi')
tts.save("voice.mp3")

img = Image.new("RGB",(1080,1920),(20,20,20))
draw = ImageDraw.Draw(img)

# avatar circle
draw.ellipse((420,200,660,440), fill=(255,180,180))

# eyes
draw.ellipse((480,270,510,300), fill="black")
draw.ellipse((570,270,600,300), fill="black")

# mouth
draw.rectangle((500,330,580,350), fill="black")

draw.text((80,700),"Did You Know?", fill=(255,255,0))
draw.text((80,900), text, fill=(255,255,255))

img.save("frame.png")

audio = AudioFileClip("voice.mp3")
clip = ImageClip("frame.png").set_duration(audio.duration)

video = clip.set_audio(audio)
video.write_videofile("short.mp4", fps=24)

print("Talking avatar video created")
