print("Starting")

import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.layers import Layers
from kmk.modules.oneshot import OneShot
from kmk.modules.modtap import ModTap
from kmk.modules.holdtap import HoldTapRepeat
from kmk.modules.split import Split, SplitType, SplitSide

from storage import getmount

# Pins are switched because I'm a dumb dumb and followed a random
# picture on the internet instead of thinking for myself :)
is_left = str(getmount('/').label)[-1] == 'L'
split = Split(
    split_type=SplitType.UART,
    data_pin=board.GP0 if is_left else board.GP1,
    data_pin2=board.GP1 if is_left else board.GP0,
    use_pio=True
)

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())

oneshot = OneShot()
oneshot.tap_time = 2000
keyboard.modules.append(oneshot)

keyboard.modules.append(split)


EXT_ESC = KC.LT(1, KC.ESC, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
SYM_ENT = KC.LT(2, KC.ENT, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
NUM_DEL = KC.LT(3, KC.DEL, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
FUN_BKSP = KC.LT(4, KC.BKSP, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)

ALT_A = KC.MT(KC.A, KC.LALT, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
GUI_S = KC.MT(KC.S, KC.LGUI, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
CTL_D = KC.MT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
SFT_F = KC.MT(KC.F, KC.LSFT, prefer_hold=True, tap_interrupted=True, tap_time=200, repeat=HoldTapRepeat.TAP)

ALT_QUOT = KC.MT(KC.QUOT, KC.LALT, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP) # Use LALT, because RALT is special
GUI_L = KC.MT(KC.L, KC.RGUI, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
CTL_K = KC.MT(KC.K, KC.RCTL, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
SFT_J = KC.MT(KC.J, KC.RSFT, prefer_hold=True, tap_interrupted=True, tap_time=200, repeat=HoldTapRepeat.TAP)

OLALT = KC.OS(KC.LALT)
OLGUI = KC.OS(KC.LGUI)
OLSFT = KC.OS(KC.LSFT)
OLCTL = KC.OS(KC.LCTL)

UNDO = KC.LCTL(KC.Z)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)

CSC = KC.LCTL(KC.LSFT(KC.C))
CSV = KC.LCTL(KC.LSFT(KC.V))

keyboard.keymap = [
    # COLEMAK BASE
    # [
    #     KC.Q,      KC.W,      KC.F,      KC.P,      KC.G,           KC.J,      KC.L,      KC.U,      KC.Y,      KC.QUOT,
    #     KC.A,      KC.R,      KC.S,      KC.T,      KC.D,           KC.H,      KC.N,      KC.E,      KC.I,      KC.O,
    #     KC.Z,      KC.X,      KC.C,      KC.V,      KC.B,           KC.K,      KC.M,      KC.COMM,   KC.DOT,    KC.SLSH,
    #                           NUM,       EXT,       KC.LSFT,        KC.SPC,    SYM,       FUN
    # ],

    # QWERTY BASE
    [
        KC.Q,      KC.W,      KC.E,      KC.R,      KC.T,           KC.Y,      KC.U,      KC.I,      KC.O,      KC.P,
        ALT_A,     GUI_S,     CTL_D,     SFT_F,     KC.G,           KC.H,      SFT_J,     CTL_K,     GUI_L,     ALT_QUOT,
        KC.Z,      KC.X,      KC.C,      KC.V,      KC.B,           KC.N,      KC.M,      KC.COMM,   KC.DOT,    KC.SLSH,
                              NUM_DEL,   EXT_ESC,   KC.TAB,         KC.SPC,    SYM_ENT,   FUN_BKSP
    ],

    # EXT
    [
        KC.ESC,    KC.NO,     KC.NO,     KC.NO,     KC.INS,         KC.PGUP,   KC.HOME,   KC.UP,     KC.END,    KC.CAPS,
        OLALT,     OLGUI,     OLSFT,     OLCTL,     KC.NO,          KC.PGDN,   KC.LEFT,   KC.DOWN,   KC.RGHT,   KC.DEL,
        UNDO,      CUT,       COPY,      PASTE,     KC.LGUI,        KC.ENT,    KC.BKSP,   KC.TAB,    KC.APP,    KC.PSCR,
                              KC.NO,     KC.TRNS,   KC.NO,          KC.ENT,    KC.NO,     KC.NO
    ],

    # SYM
    [
        KC.EXLM,   KC.AT,     KC.HASH,   KC.DLR,    KC.PERC,        KC.EQL,    KC.GRV,    KC.COLN,   KC.SCLN,   KC.PLUS,
        OLALT,     OLGUI,     OLSFT,     OLCTL,     KC.CIRC,        KC.ASTR,   KC.LPRN,   KC.LCBR,   KC.LBRC,   KC.MINS,
        KC.NO,     KC.NO,     KC.BSLS,   KC.PIPE,   KC.AMPR,        KC.TILD,   KC.RPRN,   KC.RCBR,   KC.RBRC,   KC.UNDS,
                              KC.NO,     KC.NO,     KC.NO,          KC.NO,     KC.TRNS,   KC.NO
    ],

    # NUM
    [
        KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NLCK,        KC.PEQL,   KC.KP_7,   KC.KP_8,   KC.KP_9,   KC.PPLS,
        OLALT,     OLGUI,     OLSFT,     OLCTL,     KC.NO,          KC.PAST,   KC.KP_4,   KC.KP_5,   KC.KP_6,   KC.PMNS,
        KC.NO,     KC.APP,    KC.TAB,    KC.BKSP,   KC.PENT,        KC.KP_0,   KC.KP_1,   KC.KP_2,   KC.KP_3,   KC.PSLS,
                              KC.TRNS,   KC.NO,     KC.NO,          KC.PENT,   KC.NO,     KC.NO
    ],

    # FUN
    [
        KC.MSTP,   KC.MPRV,   KC.MPLY,   KC.MNXT,   KC.BRIU,        KC.F12,    KC.F7,     KC.F8,     KC.F9,     KC.SLCK,
        OLALT,     OLGUI,     OLSFT,     OLCTL,     KC.BRID,        KC.F11,    KC.F4,     KC.F5,     KC.F6,     KC.NO,
        KC.MUTE,   KC.VOLD,   CSC,       CSV,       KC.VOLU,        KC.F10,    KC.F1,     KC.F2,     KC.F3,     KC.NO,
                              KC.NO,     KC.NO,     KC.NO,          KC.ENT,    KC.NO,     KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()
