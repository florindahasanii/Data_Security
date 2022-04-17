import code
import Morse
import winsound
frequency = 2000
duration = 1000
winsound.Beep(frequency,duration)
mode = str(input("Decode or Encode? [d/e] "))

if mode  == "e":
    text = str(input("Enter text : "))
    encoded_message = Morse.Encoder(text).run()
    print(f">> {encoded_message}")

if mode  == "d":
    text = str(input("Enter code : "))
    decoded_message = Morse.Decoder(code).run()
    print(f">> {decoded_message}")

