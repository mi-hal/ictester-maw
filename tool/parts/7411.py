from prototypes import (PackageDIP14, Pin, Test)

class Part7411(PackageDIP14):
    name = "7411"
    desc = "Triple 3-input positive-AND gates"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("2A", Pin.IN),
        4: Pin("2B", Pin.IN),
        5: Pin("2C", Pin.IN),
        6: Pin("2Y", Pin.OUT),
        8: Pin("3Y", Pin.OUT),
        9: Pin("3A", Pin.IN),
        10: Pin("3B", Pin.IN),
        11: Pin("3C", Pin.IN),
        12: Pin("1Y", Pin.OUT),
        13: Pin("1C", Pin.IN),
    }

    tests = [
        Test(
            name="Complete logic",
            inputs=[1, 2, 13, 3, 4, 5, 9, 10, 11],
            outputs=[12, 6, 8],
            ttype=Test.COMB,
            body=Test.binary_fun_gen(3, 3, lambda a, b: a & b)
        )
    ]