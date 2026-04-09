import random
from gtts import gTTS
from PIL import Image, ImageDraw

hooks = [
"90% log ye nahi jaante...",
"Ye fact aapko shock kar dega...",
"Agar aap intelligent ho to...",
"Science ke according...",
"Ye sach hai aur shocking bhi..."
]

facts = [
"human brain raat ko zyada active hota hai",
"overthinking intelligent logo ki habit hoti hai",
"sleep kam ho to memory weak hoti hai",
"90% log phone use karte waqt time bhool jate hai",
"subah uthte hi phone dekhna stress badhata hai"
]

colors = [
(15,15,15),
(0,0,40),
(20,0,0),
(0,20,0),
(30,0,30)
]

text = random.choice(hooks) + " " + random.choice(facts)
bg = random.choice(colors)

# voice
tts = gTTS(text=text, lang='hi', slow=False)
tts.save("voice.mp3")

# image
img = Image.new("RGB",(1080,1920),bg)
draw = ImageDraw.Draw(img)

# branding
draw.text((80,200),"Did You Know?", fill=(255,255,0))

# subtitle box
draw.text((80,900), text, fill=(255,255,255))

# footer
draw.text((80,1700),"FactoToons", fill=(255,0,0))

img.save("short.png")

print("Generated:", text)
