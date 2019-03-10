from microbit import *


x = Image("90009:"
          "09090:"
          "00900:"
          "09090:"
          "90009")

square = Image("99999:"
               "99999:"
               "99999:"
               "99999:"
               "99999")

while True: 
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
        display.show(square)
    else:
        display.show(x)