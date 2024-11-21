radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    basic.showNumber(receivedNumber)
    if (receivedNumber == 1) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.InBackground)
    } else if (receivedNumber == 3) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.BaDing), music.PlaybackMode.InBackground)
    } else {
        basic.showIcon(IconNames.SmallSquare, 1000)
        basic.showNumber(receivedNumber)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Chase), music.PlaybackMode.InBackground)
    radio.sendNumber(5)
    basic.pause(500)
    radio.sendString("Good Day")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendNumber(3)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.JumpUp), music.PlaybackMode.InBackground)
    radio.sendString("Hello from Prof Hamilton")
})
radio.setGroup(1)
radio.setTransmitPower(7)
radio.setFrequencyBand(3)
basic.forever(function on_forever() {
    
})
