
code = '.... . .-.. .-.. ---'


print("\n\n Your code is : ")
print('"',code,'"')

import time
from pygame import mixer


for character in code:
    if character == "-":
            mixer.init()
            sound=mixer.Sound("beep1.wav")
            sound.play()
    if character == ".":
            mixer.init()
            sound= mixer.Sound("beep4.wav")
            sound.play()
    else:
        time.sleep(.6)
