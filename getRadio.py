from microbit import *
import radio

uart.init(baudrate=115200, bits=8, parity=None, stop=1)
# sleep(400)
radio.config(group=1)
radio.on()

radio.on()
while True:
    message = radio.receive()
    if message:
        display.show(message)
        uart.write(message)

# while True:
#     if button_a.was_pressed():
#         display.show('A')
#         radio.send('A')
#     if button_b.was_pressed():
#         display.show('B')
#         radio.send('B')
#     sleep(100)

