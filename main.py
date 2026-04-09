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

text = random.choice(hooks) + " " + random.choice(facts)

# female style voice
tts = gTTS(text=text, lang='hi', slow=False)
tts.save("voice.mp3")

# shorts layout
img = Image.new("RGB",(1080,1920),(15,15,15))
draw = ImageDraw.Draw(img)

draw.text((80,700), "FACT", fill=(255,0,0))
draw.text((80,900), text, fill=(255,255,255))

img.save("short.png")

print("Generated:", text)
