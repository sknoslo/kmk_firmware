# A keyboard layout inspired by Miryoku for a 3x5+3 split keyboard.
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


NAV_ESC = KC.LT(1, KC.ESC, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
DEV_TAB = KC.LT(2, KC.TAB, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)

SYM_ENT = KC.LT(3, KC.ENT, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
NUM_SPC = KC.LT(4, KC.SPC, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
FUN_BKSP = KC.LT(5, KC.BKSP, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)

GUI_A = KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=False, tap_time=500, repeat=HoldTapRepeat.TAP)
ALT_S = KC.MT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=False, tap_time=500, repeat=HoldTapRepeat.TAP)
CTL_D = KC.MT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
SFT_F = KC.MT(KC.F, KC.LSFT, prefer_hold=True, tap_interrupted=True, tap_time=200, repeat=HoldTapRepeat.TAP)

GUI_QUOT = KC.MT(KC.QUOT, KC.RGUI, prefer_hold=False, tap_interrupted=False, tap_time=500, repeat=HoldTapRepeat.TAP)
ALT_L = KC.MT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=False, tap_time=500, repeat=HoldTapRepeat.TAP) # Use LALT, because RALT is special
CTL_K = KC.MT(KC.K, KC.RCTL, prefer_hold=False, tap_interrupted=False, tap_time=200, repeat=HoldTapRepeat.TAP)
SFT_J = KC.MT(KC.J, KC.RSFT, prefer_hold=True, tap_interrupted=True, tap_time=200, repeat=HoldTapRepeat.TAP)

OLGUI = KC.OS(KC.LGUI)
OLALT = KC.OS(KC.LALT)
OLSFT = KC.OS(KC.LSFT)
OLCTL = KC.OS(KC.LCTL)

ORGUI = KC.OS(KC.RGUI)
ORSFT = KC.OS(KC.RSFT)
ORCTL = KC.OS(KC.RCTL)

UNDO = KC.LCTL(KC.Z)
REDO = KC.LCTL(KC.Y)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)

CSC = KC.LCTL(KC.LSFT(KC.C))
CSV = KC.LCTL(KC.LSFT(KC.V))

XXXX = KC.NO
____ = KC.TRNS

# TODO: make colemak a toggleable layer so that I can practice.
keyboard.keymap = [
    # COLEMAK BASE
    # [
    #     KC.Q,      KC.W,      KC.F,      KC.P,      KC.G,           KC.J,      KC.L,      KC.U,      KC.Y,      KC.QUOT,
    #     KC.A,      KC.R,      KC.S,      KC.T,      KC.D,           KC.H,      KC.N,      KC.E,      KC.I,      KC.O,
    #     KC.Z,      KC.X,      KC.C,      KC.V,      KC.B,           KC.K,      KC.M,      KC.COMM,   KC.DOT,    KC.SLSH,
    #                           KC.DEL,    NAV_ESC,   DEV_TAB,        NUM_SPC,   SYM_ENT,   FUN_BKSP
    # ],

    # QWERTY BASE
    [
        KC.Q,      KC.W,      KC.E,      KC.R,      KC.T,           KC.Y,      KC.U,      KC.I,      KC.O,      KC.P,
        GUI_A,     ALT_S,     CTL_D,     SFT_F,     KC.G,           KC.H,      SFT_J,     CTL_K,     ALT_L,     GUI_QUOT,
        KC.Z,      KC.X,      KC.C,      KC.V,      KC.B,           KC.N,      KC.M,      KC.COMM,   KC.DOT,    KC.SLSH,
                              KC.DEL,    NAV_ESC,   DEV_TAB,        NUM_SPC,   SYM_ENT,   FUN_BKSP
    ],

    # NAV
    [
        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,           REDO,      CUT,       COPY,      PASTE,     UNDO,
        OLGUI,     OLALT,     OLSFT,     OLCTL,     XXXX,           KC.LEFT,   KC.DOWN,   KC.UP,     KC.RGHT,   KC.CAPS,
        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,           KC.INS,    KC.HOME,   KC.PGDN,   KC.PGUP,   KC.END,
                              XXXX,      ____,      XXXX,           KC.SPC,    KC.ENT,    KC.BKSP
    ],

    # DEV
    [
        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,           KC.UNDS,   KC.EQL,    KC.LPRN,   KC.RPRN,   KC.GRV,
        OLGUI,     OLALT,     OLSFT,     OLCTL,     XXXX,           KC.MINS,   KC.PLUS,   KC.LCBR,   KC.RCBR,   KC.COLN,
        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,           KC.PIPE,   KC.BSLS,   KC.LBRC,   KC.RBRC,   KC.SCLN,
                              XXXX,      XXXX,      ____,           KC.SPC,    KC.ENT,    KC.BKSP
    ],

    # SYM
    [
        KC.LCBR,   KC.AMPR,   KC.ASTR,   KC.LPRN,   KC.RCBR,        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,
        KC.COLN,   KC.DLR,    KC.PERC,   KC.CIRC,   KC.PLUS,        XXXX,      ORSFT,     ORCTL,     OLALT,     ORGUI,
        KC.TILD,   KC.EXLM,   KC.AT,     KC.HASH,   KC.PIPE,        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,
                              KC.LPRN,   KC.RPRN,   KC.UNDS,        XXXX,      ____,      XXXX
    ],

    # NUM
    [
        KC.LBRC,   KC.N7,     KC.N8,     KC.N9,     KC.RBRC,        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,
        KC.SCLN,   KC.N4,     KC.N5,     KC.N6,     KC.EQL,         XXXX,      ORSFT,     ORCTL,     OLALT,     ORGUI,
        KC.GRV,    KC.N1,     KC.N2,     KC.N3,     KC.BSLS,        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,
                              KC.DOT,    KC.N0,     KC.MINS,        ____,      XXXX,      XXXX
    ],

    # FUN
    [
        KC.F12,    KC.F7,     KC.F8,     KC.F9,     XXXX,           XXXX,      XXXX,      XXXX,      XXXX,      XXXX,
        KC.F11,    KC.F4,     KC.F5,     KC.F6,     XXXX,           XXXX,      ORSFT,     ORCTL,     OLALT,     ORGUI,
        KC.F10,    KC.F1,     KC.F2,     KC.F3,     XXXX,           XXXX,      XXXX,      XXXX,      XXXX,      XXXX,
                              KC.DEL,    KC.ESC,    KC.TAB,         XXXX,      XXXX,      ____
    ]
]

if __name__ == '__main__':
    print("Starting")
    keyboard.go()
