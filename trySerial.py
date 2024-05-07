from microbit import *
import radio

uart.init(baudrate=115200, bits=8, parity=None, stop=1)
# sleep(400)
radio.config(group=1)
radio.on()

while True:
    if uart.any():
        data = uart.read()
        x = str(data)[2:-1]
        uart.write("I sent " + x)
        radio.send(x)
        if data:
            display.show("Y")
        else:
            display.show("N")
        sleep(100)
    else:
        display.show("o")
        sleep(100)
