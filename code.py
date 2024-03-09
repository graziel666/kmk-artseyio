#this is my port for kmk of ardux.io 
#i added 2 extra keys, they only should work as GUI and SHIFT on every layer, so there should not be any problem using this for an 8 keys keyboard
#
#The Programming Raccoon (https://github.com/graziel666)

print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Chord
from kmk.modules.holdtap import HoldTap
from kmk.modules.oneshot import OneShot

# from kmk.extensions.LED import LED
# from kmk.extensions.led import AnimationModes

# led_ext = LED(led_pin=[board.GP18, board.GP19],brightness=50,animation_mode=AnimationModes.STATIC)



keyboard = KMKKeyboard()
layers = Layers()
combos = Combos()
holdtap = HoldTap()
oneshot = OneShot()

keyboard.row_pins = (board.GP0,)
#right hand pins
keyboard.col_pins = (board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8 , board.GP10 , board.GP9)
#left hand pins
#keyboard.col_pins = (board.GP4, board.GP3, board.GP2, board.GP1, board.GP8, board.GP7, board.GP6, board.GP5 , board.GP9 , board.GP10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(layers)
keyboard.modules.append(combos)
keyboard.modules.append(holdtap)
keyboard.modules.append(oneshot)
# keyboard.extensions.append(led_ext)

layers.prefer_hold=False
layers.tap_interrupted=True
# layers.tap_time=1000

combos.prefer_hold=True
combos.tap_interrupted=False

holdtap.prefer_hold=True
holdtap.tap_time=50


#debug
keyboard.debug_enabled = True
# combos.timeout=1000

TRNS = KC.TRNS
# RAISE = KC.DF(1)
BASE = KC.DF(0)
NUM_S = KC.LT(1, KC.S)
FN_O = KC.LT(2, KC.O)
PAR_A = KC.LT(3, KC.A)
SYM_E = KC.LT(4, KC.E)
#space if tap, shift if held
SPC_SHF = KC.HT(KC.SPC, KC.LSFT)
ENT_GUI = KC.HT(KC.ENT, KC.LCMD)
OS_LSFT = KC.OS(KC.LSFT)
V_ALT = KC.HT(KC.V, KC.LALT)

# LED_TOG_ALL = KC.LED_TOG()

keyboard.keymap = [
    #Layer 0: Base
    [PAR_A, KC.R, KC.T, NUM_S,
    SYM_E, KC.Y, KC.I, FN_O,
    SPC_SHF, ENT_GUI,],
    #Layer 1: Numeros
    [KC.N1, KC.N2, KC.N3, TRNS,
    KC.N4, KC.N5, KC.N6, KC.LSFT,
    TRNS, TRNS,],
    #Layer 2: Fn
    [KC.F1, KC.F2, KC.F3, TRNS,
    KC.F4, KC.F5, KC.F6, TRNS,
    TRNS, TRNS,],
    #Layer 3: Parentheticals
    [TRNS, KC.LPRN, KC.RPRN, KC.LCBR,
    TRNS, KC.LBRC, KC.RBRC, KC.RCBR,
    TRNS, TRNS,],
    #Layer 4: Symbols
    [KC.EXLM, KC.BSLS, KC.SCLN, KC.GRV,
    TRNS, KC.QUES, KC.MINS, KC.EQL,
    TRNS, TRNS,],
    #Layer 5: Games
    [KC.E, KC.W, KC.Q, KC.MO(1),
    KC.D, KC.S, KC.A, KC.MO(2),
    KC.SPC, V_ALT,],
]


combos.combos = [
    #alphabet
    Chord((SYM_E, FN_O), KC.B),
    Chord((SYM_E, KC.Y), KC.C),
    Chord((KC.T, KC.R, PAR_A), KC.D),
    Chord((KC.R, PAR_A), KC.F),
    Chord((KC.T, KC.R), KC.G),
    Chord((KC.I, SYM_E), KC.H),
    Chord((KC.T, NUM_S), KC.J),
    Chord((KC.Y, FN_O), KC.K),
    Chord((SYM_E, KC.I, KC.Y), KC.L),
    Chord((FN_O, KC.I, KC.Y), KC.M),
    Chord((FN_O, KC.I), KC.N),
    Chord((SYM_E, KC.I, FN_O), KC.P),
    Chord((PAR_A, KC.T, NUM_S), KC.Q),
    Chord((KC.Y, KC.I), KC.U),
    Chord((NUM_S, KC.R), KC.V),
    Chord((NUM_S, PAR_A), KC.W),
    Chord((NUM_S, KC.R, KC.T), KC.X),
    Chord((NUM_S, KC.R, KC.T, PAR_A), KC.Z),
    #symbols
    Chord((KC.I, PAR_A), KC.COMM),
    Chord((KC.I, KC.T), KC.EXLM),
    Chord((KC.Y, PAR_A), KC.DOT),
    Chord((KC.I, KC.Y, PAR_A), KC.QUOT),
    Chord((FN_O, PAR_A), KC.SLSH),
    #global
    Chord((SYM_E, KC.I, KC.Y, FN_O), KC.SPC),
    Chord((SYM_E, PAR_A), KC.ENT),
    Chord((FN_O,KC.T, KC.R, PAR_A), KC.TAB),
    Chord((SYM_E, KC.R), KC.BSPC),
    Chord((KC.I, KC.R), KC.DEL),
    Chord((KC.T, PAR_A),OS_LSFT),
    Chord((FN_O, KC.R, PAR_A), KC.ESC),
    #bug fixes
    Chord((SYM_E, KC.Y, FN_O), KC.NO),
    Chord((FN_O, NUM_S),KC.NO),
    Chord((FN_O, KC.I, PAR_A),KC.NO),
    Chord((FN_O, KC.I, KC.Y, PAR_A),KC.NO),
    Chord((SYM_E, NUM_S),KC.NO),
    Chord((PAR_A, KC.R, NUM_S), KC.NO),
    #numbers
    Chord((KC.N1, KC.N2), KC.N7),
    Chord((KC.N2, KC.N3), KC.N8),
    Chord((KC.N4, KC.N5), KC.N9),
    Chord((KC.N5, KC.N6), KC.N0),
    #functions
    Chord((KC.F1, KC.F2), KC.F7),
    Chord((KC.F2, KC.F3), KC.F8),
    Chord((KC.F4, KC.F5), KC.F9),
    Chord((KC.F5, KC.F6), KC.F10),
    Chord((KC.F4, KC.F2), KC.F11),
    Chord((KC.F6, KC.F2), KC.F12),
    #game layer change
    Chord((KC.R,KC.I, SYM_E), KC.DF(5)),
    Chord((KC.W,KC.A, KC.D), KC.DF(0)),
    Chord((KC.Q,KC.W), KC.N6),
    Chord((KC.E,KC.W), KC.Z),
    Chord((KC.Q,KC.E), KC.C),
    Chord((KC.A,KC.S, KC.D), KC.X),
    #just a reset to Base
    Chord((ENT_GUI, SPC_SHF), KC.RLD),
]



if __name__ == '__main__':
    keyboard.go()
