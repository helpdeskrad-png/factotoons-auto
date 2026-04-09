import random
from gtts import gTTS

facts = [
"Human body me 206 bones hoti hai",
"Aapka brain 75% water se bana hai",
"Sleep ke bina brain shrink ho sakta hai",
"Heart ek din me 100000 baar beat karta hai",
"90% log phone use karte waqt time bhool jate hai"
]

text = random.choice(facts)

tts = gTTS(text=text, lang='hi')
tts.save("voice.mp3")

print("voice generated")
