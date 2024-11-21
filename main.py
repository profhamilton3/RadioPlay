def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
    if receivedNumber == 1:
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
            music.PlaybackMode.IN_BACKGROUND)
    elif receivedNumber == 3:
        music._play_default_background(music.built_in_playable_melody(Melodies.BA_DING),
            music.PlaybackMode.IN_BACKGROUND)
    else:
        basic.show_icon(IconNames.SMALL_SQUARE, 1000)
        basic.show_number(receivedNumber)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music._play_default_background(music.built_in_playable_melody(Melodies.CHASE),
        music.PlaybackMode.IN_BACKGROUND)
    radio.send_number(5)
    basic.pause(500)
    radio.send_string("Good Day")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_number(3)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
        music.PlaybackMode.IN_BACKGROUND)
    radio.send_string("Hello from Prof Hamilton")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

radio.set_group(1)
radio.set_transmit_power(7)
radio.set_frequency_band(3)

def on_forever():
    pass
basic.forever(on_forever)
