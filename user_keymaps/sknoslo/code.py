# A keyboard layout inspired by Miryoku for a 3x5+3 split keyboard.
import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.tapdance import TapDance
from kmk.modules.holdtap import HoldTapRepeat
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.capsword import CapsWord


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
keyboard.modules.append(TapDance())
keyboard.modules.append(split)
keyboard.modules.append(CapsWord())

quick_tap = 160
slow_tap = 500

NAV_ESC = KC.LT(2, KC.ESC, prefer_hold=False, tap_interrupted=False, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)
DEV_TAB = KC.LT(3, KC.TAB, prefer_hold=False, tap_interrupted=False, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)

SYM_ENT = KC.LT(4, KC.ENT, prefer_hold=False, tap_interrupted=False, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)
NUM_SPC = KC.LT(5, KC.SPC, prefer_hold=False, tap_interrupted=False, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)
FUN_BKSP = KC.LT(6, KC.BKSP, prefer_hold=False, tap_interrupted=False, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)

GUI_A = KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=False, tap_time=slow_tap, repeat=HoldTapRepeat.TAP)

ALT_S = KC.MT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=False, tap_time=slow_tap, repeat=HoldTapRepeat.TAP)
ALT_R = KC.MT(KC.R, KC.LALT, prefer_hold=False, tap_interrupted=False, tap_time=slow_tap, repeat=HoldTapRepeat.TAP)

CTL_D = KC.MT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=False, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)
CTL_S = KC.MT(KC.S, KC.LCTL, prefer_hold=False, tap_interrupted=False, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)

SFT_F = KC.MT(KC.F, KC.LSFT, prefer_hold=True, tap_interrupted=True, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)
SFT_T = KC.MT(KC.T, KC.LSFT, prefer_hold=True, tap_interrupted=True, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)

GUI_QUOT = KC.MT(KC.QUOT, KC.RGUI, prefer_hold=False, tap_interrupted=False, tap_time=slow_tap, repeat=HoldTapRepeat.TAP)
GUI_O = KC.MT(KC.O, KC.RGUI, prefer_hold=False, tap_interrupted=False, tap_time=slow_tap, repeat=HoldTapRepeat.TAP)

ALT_L = KC.MT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=False, tap_time=slow_tap, repeat=HoldTapRepeat.TAP) # Use LALT, because RALT is special
ALT_I = KC.MT(KC.I, KC.LALT, prefer_hold=False, tap_interrupted=False, tap_time=slow_tap, repeat=HoldTapRepeat.TAP) # Use LALT, because RALT is special

CTL_K = KC.MT(KC.K, KC.RCTL, prefer_hold=False, tap_interrupted=False, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)
CTL_E = KC.MT(KC.E, KC.RCTL, prefer_hold=False, tap_interrupted=False, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)

SFT_J = KC.MT(KC.J, KC.RSFT, prefer_hold=True, tap_interrupted=True, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)
SFT_N = KC.MT(KC.N, KC.RSFT, prefer_hold=True, tap_interrupted=True, tap_time=quick_tap, repeat=HoldTapRepeat.TAP)

# TODO: these aliases don't really make sense any more. rename more abstractly or nix all together.
OLGUI = KC.LGUI
OLALT = KC.LALT
OLSFT = KC.LSFT
OLCTL = KC.LCTL

ORGUI = KC.RGUI
ORSFT = KC.RSFT
ORCTL = KC.RCTL

UNDO = KC.LCTL(KC.Z)
REDO = KC.LCTL(KC.Y)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)

CSC = KC.LCTL(KC.LSFT(KC.C))
CSV = KC.LCTL(KC.LSFT(KC.V))

QWERT = KC.TD(KC.NO, KC.DF(0))
COLMK = KC.TD(KC.NO, KC.DF(1))

XXXX = KC.NO
____ = KC.TRNS

keyboard.keymap = [
    # QWERTY BASE
    [
        KC.Q,      KC.W,      KC.E,      KC.R,      KC.T,           KC.Y,      KC.U,      KC.I,      KC.O,      KC.P,
        GUI_A,     ALT_S,     CTL_D,     SFT_F,     KC.G,           KC.H,      SFT_J,     CTL_K,     ALT_L,     GUI_QUOT,
        KC.Z,      KC.X,      KC.C,      KC.V,      KC.B,           KC.N,      KC.M,      KC.COMM,   KC.DOT,    KC.SLSH,
                              KC.DEL,    NAV_ESC,   DEV_TAB,        NUM_SPC,   SYM_ENT,   FUN_BKSP
    ],

    # COLEMAK MOD-DH BASE
    [
        KC.Q,      KC.W,      KC.F,      KC.P,      KC.B,           KC.J,      KC.L,      KC.U,      KC.Y,      KC.QUOT,
        GUI_A,     ALT_R,     CTL_S,     SFT_T,     KC.G,           KC.M,      SFT_N,     CTL_E,     ALT_I,     GUI_O,
        KC.Z,      KC.X,      KC.C,      KC.D,      KC.V,           KC.K,      KC.H,      KC.COMM,   KC.DOT,    KC.SLSH,
                              KC.DEL,    NAV_ESC,   DEV_TAB,        NUM_SPC,   SYM_ENT,   FUN_BKSP
    ],

    # NAV
    [
        XXXX,      XXXX,      COLMK,     QWERT,     XXXX,           REDO,      CUT,       COPY,      PASTE,     UNDO,
        OLGUI,     OLALT,     OLCTL,     OLSFT,     XXXX,           KC.LEFT,   KC.DOWN,   KC.UP,     KC.RGHT,   KC.CW,
        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,           KC.INS,    KC.HOME,   KC.PGDN,   KC.PGUP,   KC.END,
                              XXXX,      ____,      XXXX,           KC.SPC,    KC.ENT,    KC.BKSP
    ],

    # DEV
    [
        XXXX,      XXXX,      COLMK,     QWERT,     XXXX,           KC.UNDS,   KC.EQL,    KC.LPRN,   KC.RPRN,   KC.GRV,
        OLGUI,     OLALT,     OLCTL,     OLSFT,     XXXX,           KC.MINS,   KC.PLUS,   KC.LCBR,   KC.RCBR,   KC.COLN,
        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,           KC.PIPE,   KC.BSLS,   KC.LBRC,   KC.RBRC,   KC.SCLN,
                              XXXX,      XXXX,      ____,           KC.SPC,    KC.ENT,    KC.BKSP
    ],

    # SYM
    [
        KC.LCBR,   KC.AMPR,   KC.ASTR,   KC.LPRN,   KC.RCBR,        XXXX,      QWERT,     COLMK,     XXXX,      XXXX,
        KC.COLN,   KC.DLR,    KC.PERC,   KC.CIRC,   KC.PLUS,        XXXX,      ORSFT,     ORCTL,     OLALT,     ORGUI,
        KC.TILD,   KC.EXLM,   KC.AT,     KC.HASH,   KC.PIPE,        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,
                              KC.LPRN,   KC.RPRN,   KC.UNDS,        XXXX,      ____,      XXXX
    ],

    # NUM
    [
        KC.LBRC,   KC.N7,     KC.N8,     KC.N9,     KC.RBRC,        XXXX,      QWERT,     COLMK,     XXXX,      XXXX,
        KC.SCLN,   KC.N4,     KC.N5,     KC.N6,     KC.EQL,         XXXX,      ORSFT,     ORCTL,     OLALT,     ORGUI,
        KC.GRV,    KC.N1,     KC.N2,     KC.N3,     KC.BSLS,        XXXX,      XXXX,      XXXX,      XXXX,      XXXX,
                              KC.DOT,    KC.N0,     KC.MINS,        ____,      XXXX,      XXXX
    ],

    # FUN
    [
        KC.F12,    KC.F7,     KC.F8,     KC.F9,     XXXX,           XXXX,      QWERT,     COLMK,     XXXX,      XXXX,
        KC.F11,    KC.F4,     KC.F5,     KC.F6,     XXXX,           XXXX,      ORSFT,     ORCTL,     OLALT,     ORGUI,
        KC.F10,    KC.F1,     KC.F2,     KC.F3,     XXXX,           XXXX,      XXXX,      XXXX,      XXXX,      XXXX,
                              KC.DEL,    KC.ESC,    KC.TAB,         XXXX,      XXXX,      ____
    ]
]

if __name__ == '__main__':
    print("Starting")
    keyboard.go()
