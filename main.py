xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)
basic.show_icon(IconNames.SKULL)

def on_forever():
    basic.show_icon(IconNames.SILLY)
    xgo.execution_action(xgo.action_enum.SQUAT)
    basic.pause(5000)
    xgo.execution_action(xgo.action_enum.CRAWL_FORWARD)
    basic.pause(5000)
    xgo.execution_action(xgo.action_enum.STAND)
    basic.pause(2000)
    xgo.execution_action(xgo.action_enum.WHIRL)
    basic.pause(5000)
basic.forever(on_forever)
