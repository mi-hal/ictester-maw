#from prototypes import (PackageDIP16, Pin, Test)
#
#class Part74165(PackageDIP16):
#    name = "74165"
#    desc = "8-bit parallel-out serial shift register"
#    pin_cfg = {
#        1: Pin("SH/~LD", Pin.IN),
#        2: Pin("CLK", Pin.IN),
#        3: Pin("E", Pin.IN),
#        4: Pin("F", Pin.IN),
#        5: Pin("G", Pin.IN),
#        6: Pin("H", Pin.IN),
#        7: Pin("~QH", Pin.OUT),
#        9: Pin("QH", Pin.OUT),
#        10: Pin("SER", Pin.IN),
#        11: Pin("A", Pin.IN),
#        12: Pin("B", Pin.IN),
#        13: Pin("C", Pin.IN),
#        14: Pin("D", Pin.IN),
#        15: Pin("CLK INH", Pin.IN),
#    }
#    test_all = Test(
#        name="Complete logic",
#        inputs=[1, 15, 2,  10,  11, 12, 13, 14, 3, 4, 5, 6],
#        outputs=[9, 7],
#        ttype=Test.SEQ,
#        body=[
#            [['-', 0,   0,  0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1]],
#
#            [['-', 0,   0,  0,  1, 1, 1, 1, 1, 1, 1, 1], [1, 0]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [1, 0]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [1, 0]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [1, 0]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [1, 1]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [1, 0]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [1, 0]],
#            [[  1, 0, '+',  0,  0, 0, 0, 0, 0, 0, 0, 0], [1, 0]],
#        ]
#    )
#    tests = [test_all]