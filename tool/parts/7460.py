from binvec import BV
from prototypes import (PackageDIP14, Pin, Test)

'''
NOTE on testing expanders:
~X and X are outputs, but not in a TTL-levels sense: ~X is output transistor collector, X is its emmiter.
Pin configuration does the following:
 * pulls up the collector with the internal pull-up resistor (OC output)
 * connects the emmiter to a current sink (output driven low)
Thus, ~X becomes the actual output, and X needs to be always driven low.
'''

class Part7460(PackageDIP14):
    name = "7460"
    desc = "Dual 4-input expanders"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("1C", Pin.IN),
        4: Pin("2A", Pin.IN),
        5: Pin("2B", Pin.IN),
        6: Pin("2C", Pin.IN),
        8: Pin("2D", Pin.IN),
        9: Pin("~2X", Pin.OC),
        10: Pin("2X", Pin.IN),
        11: Pin("1X", Pin.IN),
        12: Pin("~1X", Pin.OC),
        13: Pin("1D", Pin.IN),
    }

    test_async = Test("Asynchronous operation", Test.COMB,
        inputs=[11, 10,  1, 2, 3, 13,  4, 5, 6, 8],
        outputs=[12, 9],
        loops = 64,
        body = [
            [[0, 0, *i, *i],  [*~i.vand(), *~i.vand()]] for i in BV.range(0, 16)
        ]
    )

    tests = [test_async]
