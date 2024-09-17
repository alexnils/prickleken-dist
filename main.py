def on_received_number(receivedNumber):
    global numLeds, selectedToRemove
    basic.clear_screen()
    numLeds = receivedNumber
    selectedToRemove = 0
    drawLed(numLeds)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global selectedToRemove
    basic.clear_screen()
    if selectedToRemove < 3:
        selectedToRemove += 1
    else:
        selectedToRemove = 1
    basic.show_number(selectedToRemove)
input.on_button_pressed(Button.A, on_button_pressed_a)

def drawLed(leds: number):
    global row, index
    row = 0
    if leds != 0:
        index = 0
    while index <= leds - 1:
        if index % 5 == 0 and index != 0:
            row += 1
        led.plot(index - row * 5, row)
        index += 1

def on_button_pressed_b():
    global numLeds, selectedToRemove
    basic.clear_screen()
    numLeds = numLeds - selectedToRemove
    if numLeds <= 0:
        basic.show_string("YOU WIN")
    else:
        drawLed(numLeds)
    selectedToRemove = 0
    radio.send_number(numLeds)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.clear_screen()
    drawLed(numLeds)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

index = 0
row = 0
selectedToRemove = 0
numLeds = 0
numLeds = randint(10, 25)
selectedToRemove = 0
drawLed(numLeds)
radio.set_group(1)