radio.onReceivedNumber(function (receivedNumber) {
    basic.clearScreen()
    numLeds = receivedNumber
    selectedToRemove = 0
    drawLed(numLeds)
})
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    if (selectedToRemove < 3) {
        selectedToRemove += 1
    } else {
        selectedToRemove = 1
    }
    basic.showNumber(selectedToRemove)
})
function drawLed (leds: number) {
    row = 0
    if (leds != 0) {
        index = 0
    }
    while (index <= leds - 1) {
        if (index % 5 == 0 && index != 0) {
            row += 1
        }
        led.plot(index - row * 5, row)
        index += 1
    }
}
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    numLeds = numLeds - selectedToRemove
    if (numLeds <= 0) {
        basic.showString("YOU WIN")
    } else {
        drawLed(numLeds)
    }
    selectedToRemove = 0
    radio.sendNumber(numLeds)
})
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    drawLed(numLeds)
})
let index = 0
let row = 0
let selectedToRemove = 0
let numLeds = 0
numLeds = randint(10, 25)
selectedToRemove = 0
drawLed(numLeds)
radio.setGroup(122)
