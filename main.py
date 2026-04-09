import random
from gtts import gTTS
from PIL import Image, ImageDraw

facts = [
"Aapka brain raat ko zyada active hota hai",
"Human body me 206 bones hoti hai",
"Overthinking intelligent logo ki habit hoti hai",
"Sleep kam ho to memory weak hoti hai",
"90% log phone use karte waqt time bhool jate hai"
]

text = random.choice(facts)

tts = gTTS(text=text, lang='hi')
tts.save("voice.mp3")

img = Image.new("RGB",(1080,1920),(0,0,0))
draw = ImageDraw.Draw(img)

draw.text((80,900), text, fill=(255,255,255))

img.save("short.png")

print("Generated:", text)
