pins.set_pull(DigitalPin.P8, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P9, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P2, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P13, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P14, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P15, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P16, PinPullMode.PULL_UP)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P8) == 0:
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        if pins.digital_read_pin(DigitalPin.P9) == 0:
            music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
        else:
            if pins.digital_read_pin(DigitalPin.P2) == 0:
                music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
                    music.PlaybackMode.UNTIL_DONE)
            else:
                if pins.digital_read_pin(DigitalPin.P13) == 0:
                    music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
                        music.PlaybackMode.UNTIL_DONE)
                else:
                    if pins.digital_read_pin(DigitalPin.P14) == 0:
                        music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
                            music.PlaybackMode.UNTIL_DONE)
                    else:
                        if pins.digital_read_pin(DigitalPin.P15) == 0:
                            music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
                                music.PlaybackMode.UNTIL_DONE)
                        else:
                            if pins.digital_read_pin(DigitalPin.P16) == 0:
                                music.play(music.tone_playable(494, music.beat(BeatFraction.WHOLE)),
                                    music.PlaybackMode.UNTIL_DONE)
                            else:
                                pass
basic.forever(on_forever)
