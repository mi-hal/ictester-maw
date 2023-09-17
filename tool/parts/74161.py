from prototypes import (PackageDIP16, Pin, PinType, TestLogic)

class Part74161(PackageDIP16):
    name = "74161"
    desc = "Synchronous presettable 4-bit counter"
    pin_cfg = {
        1: Pin("~CLR", PinType.IN),
        2: Pin("CLK", PinType.IN),
        3: Pin("A", PinType.IN),
        4: Pin("B", PinType.IN),
        5: Pin("C", PinType.IN),
        6: Pin("D", PinType.IN),
        7: Pin("ENP", PinType.IN),
        9: Pin("~LOAD", PinType.IN),
        10: Pin("ENT", PinType.IN),
        11: Pin("QD", PinType.OUT),
        12: Pin("QC", PinType.OUT),
        13: Pin("QB", PinType.OUT),
        14: Pin("QA", PinType.OUT),
        15: Pin("RCO", PinType.OUT),
    }

    test_all = TestLogic("Complete logic",
        inputs=[1, 9, 2,  10, 7,  6, 5, 4, 3],
        outputs=[11, 12, 13, 14,  15],
        body=[
            # NOTE: "enable" transitions done on clock high,
            # some chips are more sensitive to that
            # initial clear
            [['\\', 1,   1,  0, 0,  0, 0, 0, 0], [0, 0, 0, 0,  0]],
            [[  1, 1,   1,  0, 0,  0, 0, 0, 0], [0, 0, 0, 0,  0]],
            # loads
            [[  1, 0,   1,  0, 0,  0, 0, 0, 0], [0, 0, 0, 0,  0]],
            [[  1, 0, '/',  0, 0,  0, 0, 0, 1], [0, 0, 0, 1,  0]],
            [[  1, 0, '/',  0, 0,  0, 0, 1, 0], [0, 0, 1, 0,  0]],
            [[  1, 0, '/',  0, 0,  0, 0, 1, 1], [0, 0, 1, 1,  0]],
            [[  1, 0, '/',  0, 0,  0, 1, 0, 0], [0, 1, 0, 0,  0]],
            [[  1, 0, '/',  0, 0,  0, 1, 0, 1], [0, 1, 0, 1,  0]],
            [[  1, 0, '/',  0, 0,  0, 1, 1, 0], [0, 1, 1, 0,  0]],
            [[  1, 0, '/',  0, 0,  0, 1, 1, 1], [0, 1, 1, 1,  0]],
            [[  1, 0, '/',  0, 0,  1, 0, 0, 0], [1, 0, 0, 0,  0]],
            [[  1, 0, '/',  0, 0,  1, 0, 0, 1], [1, 0, 0, 1,  0]],
            [[  1, 0, '/',  0, 0,  1, 0, 1, 0], [1, 0, 1, 0,  0]],
            [[  1, 0, '/',  0, 0,  1, 0, 1, 1], [1, 0, 1, 1,  0]],
            [[  1, 0, '/',  0, 0,  1, 1, 0, 0], [1, 1, 0, 0,  0]],
            [[  1, 0, '/',  0, 0,  1, 1, 0, 1], [1, 1, 0, 1,  0]],
            [[  1, 0, '/',  0, 0,  1, 1, 1, 0], [1, 1, 1, 0,  0]],
            [[  1, 0, '/',  0, 0,  1, 1, 1, 1], [1, 1, 1, 1,  0]],
            # disable load, enable count
            [[  1, 1,   1,  1, 1,  0, 0, 0, 0], [1, 1, 1, 1,  1]],
            # count
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [0, 0, 0, 0,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [0, 0, 0, 1,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [0, 0, 1, 0,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [0, 0, 1, 1,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [0, 1, 0, 0,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [0, 1, 0, 1,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [0, 1, 1, 0,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [0, 1, 1, 1,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [1, 0, 0, 0,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [1, 0, 0, 1,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [1, 0, 1, 0,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [1, 0, 1, 1,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [1, 1, 0, 0,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [1, 1, 0, 1,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [1, 1, 1, 0,  0]],
            [[  1, 1, '/',  1, 1,  0, 0, 0, 0], [1, 1, 1, 1,  1]],
            # count inhibit
            [[  1, 1,   1,  0, 1,  0, 0, 0, 0], [1, 1, 1, 1,  0]],
            [[  1, 1,   0,  0, 1,  0, 0, 0, 0], [1, 1, 1, 1,  0]],
            [[  1, 1,   1,  0, 1,  0, 0, 0, 0], [1, 1, 1, 1,  0]],

            [[  1, 1,   1,  1, 0,  0, 0, 0, 0], [1, 1, 1, 1,  1]],
            [[  1, 1,   0,  1, 0,  0, 0, 0, 0], [1, 1, 1, 1,  1]],
            [[  1, 1,   1,  1, 0,  0, 0, 0, 0], [1, 1, 1, 1,  1]],

            [[  1, 1,   1,  0, 0,  0, 0, 0, 0], [1, 1, 1, 1,  0]],
            [[  1, 1,   0,  0, 0,  0, 0, 0, 0], [1, 1, 1, 1,  0]],
            [[  1, 1,   1,  0, 0,  0, 0, 0, 0], [1, 1, 1, 1,  0]],
        ]
    )

    tests = [test_all]
