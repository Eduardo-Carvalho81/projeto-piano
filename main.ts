pins.setPull(DigitalPin.P8, PinPullMode.PullUp)
pins.setPull(DigitalPin.P9, PinPullMode.PullUp)
pins.setPull(DigitalPin.P2, PinPullMode.PullUp)
pins.setPull(DigitalPin.P13, PinPullMode.PullUp)
pins.setPull(DigitalPin.P14, PinPullMode.PullUp)
pins.setPull(DigitalPin.P15, PinPullMode.PullUp)
pins.setPull(DigitalPin.P16, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P8) == 0) {
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    } else {
        if (pins.digitalReadPin(DigitalPin.P9) == 0) {
            music.play(music.tonePlayable(294, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        } else {
            if (pins.digitalReadPin(DigitalPin.P2) == 0) {
                music.play(music.tonePlayable(330, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            } else {
                if (pins.digitalReadPin(DigitalPin.P13) == 0) {
                    music.play(music.tonePlayable(349, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
                } else {
                    if (pins.digitalReadPin(DigitalPin.P14) == 0) {
                        music.play(music.tonePlayable(392, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
                    } else {
                        if (pins.digitalReadPin(DigitalPin.P15) == 0) {
                            music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
                        } else {
                            if (pins.digitalReadPin(DigitalPin.P16) == 0) {
                                music.play(music.tonePlayable(494, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
                            } else {
                            	
                            }
                        }
                    }
                }
            }
        }
    }
})
