import sys
import inspect
from collections import namedtuple
from prototypes import (Test, Pin, PartDIP14, PartDIP14_vcc5, PartDIP14_vcc4, PartDIP16, PartDIP16_vcc5, PartDIP16_rotated, PartDIP24)
from functools import reduce


# ------------------------------------------------------------------------
class Part7400(PartDIP14):
    name = "7400"
    desc = "Quad 2-input positive-NAND gates"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("1Y", Pin.OUT),
        4: Pin("2A", Pin.IN),
        5: Pin("2B", Pin.IN),
        6: Pin("2Y", Pin.OUT),
        8: Pin("3Y", Pin.OUT),
        9: Pin("3A", Pin.IN),
        10: Pin("3B", Pin.IN),
        11: Pin("4Y", Pin.OUT),
        12: Pin("4A", Pin.IN),
        13: Pin("4B", Pin.IN),
    }
    tests = [
        Test(
            name="Complete logic",
            inputs=[1, 2, 4, 5, 10, 9, 13, 12],
            outputs=[3, 6, 8, 11],
            ttype=Test.COMB,
            body=Test.binary_fun_gen(4, 2, lambda a, b: a & b, inverted=True)
        )
    ]


# ------------------------------------------------------------------------
class Part7402(PartDIP14):
    name = "7402"
    desc = "Quad 2-input positive-NOR gates"
    pin_cfg = {
        1: Pin("1Y", Pin.OUT),
        2: Pin("1A", Pin.IN),
        3: Pin("1B", Pin.IN),
        4: Pin("2Y", Pin.OUT),
        5: Pin("2A", Pin.IN),
        6: Pin("2B", Pin.IN),
        8: Pin("3A", Pin.IN),
        9: Pin("3B", Pin.IN),
        10: Pin("3Y", Pin.OUT),
        11: Pin("4A", Pin.IN),
        12: Pin("4B", Pin.IN),
        13: Pin("4Y", Pin.OUT),
    }
    tests = [
        Test(
            name="Complete logic",
            inputs=[2, 3, 5, 6, 8, 9, 11, 12],
            outputs=[1, 4, 10, 13],
            ttype=Test.COMB,
            body=Test.binary_fun_gen(4, 2, lambda a, b: a | b, inverted=True)
        )
    ]


# ------------------------------------------------------------------------
class Part7403(Part7400):
    name = "7403"
    desc = "Quad 2-input positive-NAND gates with open-collector outputs"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("1Y", Pin.OC),
        4: Pin("2A", Pin.IN),
        5: Pin("2B", Pin.IN),
        6: Pin("2Y", Pin.OC),
        8: Pin("3Y", Pin.OC),
        9: Pin("3A", Pin.IN),
        10: Pin("3B", Pin.IN),
        11: Pin("4Y", Pin.OC),
        12: Pin("4A", Pin.IN),
        13: Pin("4B", Pin.IN),
    }


# ------------------------------------------------------------------------
class Part7404(PartDIP14):
    name = "7404"
    desc = "Hex inverters"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1Y", Pin.OUT),
        3: Pin("2A", Pin.IN),
        4: Pin("2Y", Pin.OUT),
        5: Pin("3A", Pin.IN),
        6: Pin("3Y", Pin.OUT),
        8: Pin("6Y", Pin.OUT),
        9: Pin("6A", Pin.IN),
        10: Pin("5Y", Pin.OUT),
        11: Pin("5A", Pin.IN),
        12: Pin("4Y", Pin.OUT),
        13: Pin("4A", Pin.IN),
    }
    tests = [
        Test(
            name="Complete logic",
            inputs=[1, 3, 5, 9, 11, 13],
            outputs=[2, 4, 6, 8, 10, 12],
            ttype=Test.COMB,
            body=Test.binary_fun_gen(6, 1, lambda a: a, inverted=True)
        )
    ]


# ------------------------------------------------------------------------
class Part7405(Part7404):
    name = "7405"
    desc = "Hex inverters with open collector outputs"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1Y", Pin.OC),
        3: Pin("2A", Pin.IN),
        4: Pin("2Y", Pin.OC),
        5: Pin("3A", Pin.IN),
        6: Pin("3Y", Pin.OC),
        8: Pin("6Y", Pin.OC),
        9: Pin("6A", Pin.IN),
        10: Pin("5Y", Pin.OC),
        11: Pin("5A", Pin.IN),
        12: Pin("4Y", Pin.OC),
        13: Pin("4A", Pin.IN),
    }


# ------------------------------------------------------------------------
class Part7406(Part7405):
    name = "7406"
    desc = "Hex inverter buffers / drivers with high-voltage outputs"


# ------------------------------------------------------------------------
class Part7407(Part7405):
    name = "7407"
    desc = "Hex Buffers/Drivers With Open-Collector High-Voltage Outputs"
    tests = [
        Test(
            name="Complete logic",
            inputs=[1, 3, 5, 9, 11, 13],
            outputs=[2, 4, 6, 8, 10, 12],
            ttype=Test.COMB,
            body=Test.binary_fun_gen(6, 1, lambda a: a)
        )
    ]


# ------------------------------------------------------------------------
class Part7408(PartDIP14):
    name = "7408"
    desc = "Quad 2-input positive-AND gates"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("1Y", Pin.OUT),
        4: Pin("2A", Pin.IN),
        5: Pin("2B", Pin.IN),
        6: Pin("2Y", Pin.OUT),
        8: Pin("3Y", Pin.OUT),
        9: Pin("3A", Pin.IN),
        10: Pin("3B", Pin.IN),
        11: Pin("4Y", Pin.OUT),
        12: Pin("4A", Pin.IN),
        13: Pin("4B", Pin.IN),
    }
    tests = [
        Test(
            name="Complete logic",
            inputs=[1, 2, 4, 5, 10, 9, 13, 12],
            outputs=[3, 6, 8, 11],
            ttype=Test.COMB,
            body=Test.binary_fun_gen(4, 2, lambda a, b: a & b)
        )
    ]


# ------------------------------------------------------------------------
class Part7410(PartDIP14):
    name = "7410"
    desc = "Triple 3-input positive-NAND gates"
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
            body=Test.binary_fun_gen(3, 3, lambda a, b: a & b, inverted=True)
        )
    ]


# ------------------------------------------------------------------------
class Part7411(PartDIP14):
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


# ------------------------------------------------------------------------
class Part7412(Part7410):
    name = "7412"
    desc = "Triple 3-input positive-NAND gates with open-collector outputs"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("2A", Pin.IN),
        4: Pin("2B", Pin.IN),
        5: Pin("2C", Pin.IN),
        6: Pin("2Y", Pin.OC),
        8: Pin("3Y", Pin.OC),
        9: Pin("3A", Pin.IN),
        10: Pin("3B", Pin.IN),
        11: Pin("3C", Pin.IN),
        12: Pin("1Y", Pin.OC),
        13: Pin("1C", Pin.IN),
    }


# ------------------------------------------------------------------------
class Part7413(PartDIP14):
    name = "7413"
    desc = "Dual 4-input positive-NAND Schmitt triggers"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("NC", Pin.NC),
        4: Pin("1C", Pin.IN),
        5: Pin("1D", Pin.IN),
        6: Pin("1Y", Pin.OUT),
        8: Pin("2Y", Pin.OUT),
        9: Pin("2A", Pin.IN),
        10: Pin("2B", Pin.IN),
        11: Pin("NC", Pin.NC),
        12: Pin("2C", Pin.IN),
        13: Pin("2D", Pin.IN),
    }

    tests = [
        Test(
            name="Complete logic",
            inputs=[1, 2, 4, 5, 13, 12, 10, 9],
            outputs=[6, 8],
            ttype=Test.COMB,
            body=Test.binary_fun_gen(2, 4, lambda a, b: a & b, inverted=True)
        )
    ]


# ------------------------------------------------------------------------
class Part7420(Part7413):
    name = "7420"
    desc = "Dual 4-input positive-NAND gates"


# ------------------------------------------------------------------------
class Part7421(Part7413):
    name = "7421"
    desc = "Dual 4-input positive-AND gates"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("NC", Pin.NC),
        4: Pin("1C", Pin.IN),
        5: Pin("1D", Pin.IN),
        6: Pin("1Y", Pin.OUT),
        8: Pin("2Y", Pin.OUT),
        9: Pin("2A", Pin.IN),
        10: Pin("2B", Pin.IN),
        11: Pin("NC", Pin.NC),
        12: Pin("2C", Pin.IN),
        13: Pin("2D", Pin.IN),
    }

    tests = [
        Test(
            name="Complete logic",
            inputs=[1, 2, 4, 5, 13, 12, 10, 9],
            outputs=[6, 8],
            ttype=Test.COMB,
            body=Test.binary_fun_gen(2, 4, lambda a, b: a & b, inverted=False)
        )
    ]


# ------------------------------------------------------------------------
class Part7430(PartDIP14):
    name = "7430"
    desc = "8-input positive-NAND gate"
    pin_cfg = {
        1: Pin("A", Pin.IN),
        2: Pin("B", Pin.IN),
        3: Pin("C", Pin.IN),
        4: Pin("D", Pin.IN),
        5: Pin("E", Pin.IN),
        6: Pin("F", Pin.IN),
        8: Pin("Y", Pin.OUT),
        9: Pin("NC", Pin.NC),
        10: Pin("NC", Pin.NC),
        11: Pin("G", Pin.IN),
        12: Pin("H", Pin.IN),
        13: Pin("NC", Pin.NC),
    }

    tests = [
        Test(
            name="Complete logic",
            inputs=[1, 2, 3, 4, 5, 6, 11, 12],
            outputs=[8],
            ttype=Test.COMB,
            body=Test.binary_fun_gen(1, 8, lambda a, b: a & b, inverted=True)
        )
    ]


# ------------------------------------------------------------------------
class Part7432(PartDIP14):
    name = "7432"
    desc = "Quad 2-input positive-OR gates"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("1Y", Pin.OUT),
        4: Pin("2A", Pin.IN),
        5: Pin("2B", Pin.IN),
        6: Pin("2Y", Pin.OUT),
        8: Pin("3Y", Pin.OUT),
        9: Pin("3A", Pin.IN),
        10: Pin("3B", Pin.IN),
        11: Pin("4Y", Pin.OUT),
        12: Pin("4A", Pin.IN),
        13: Pin("4B", Pin.IN),
    }
    tests = [
        Test(
            name="Complete logic",
            inputs=[1, 2, 4, 5, 10, 9, 13, 12],
            outputs=[3, 6, 8, 11],
            ttype=Test.COMB,
            body=Test.binary_fun_gen(4, 2, lambda a, b: a | b)
        )
    ]


# ------------------------------------------------------------------------
class Part7437(Part7400):
    name = "7437"
    desc = "Quad 2-input positive-NAND buffers"


# ------------------------------------------------------------------------
class Part7438(Part7400):
    name = "7438"
    desc = "Quad 2-input positive-NAND buffers with open collector outputs"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("1Y", Pin.OC),
        4: Pin("2A", Pin.IN),
        5: Pin("2B", Pin.IN),
        6: Pin("2Y", Pin.OC),
        8: Pin("3Y", Pin.OC),
        9: Pin("3A", Pin.IN),
        10: Pin("3B", Pin.IN),
        11: Pin("4Y", Pin.OC),
        12: Pin("4A", Pin.IN),
        13: Pin("4B", Pin.IN),
    }


# ------------------------------------------------------------------------
class Part7440(Part7413):
    name = "7440"
    desc = "Dual 4-input positive-NAND Buffer"


# ------------------------------------------------------------------------
class Part7442(PartDIP16):
    name = "7442"
    desc = "4-line BCD to 10-line decimal decoders"
    pin_cfg = {
        1: Pin("0", Pin.OUT),
        2: Pin("1", Pin.OUT),
        3: Pin("2", Pin.OUT),
        4: Pin("3", Pin.OUT),
        5: Pin("4", Pin.OUT),
        6: Pin("5", Pin.OUT),
        7: Pin("6", Pin.OUT),
        9: Pin("7", Pin.OUT),
        10: Pin("8", Pin.OUT),
        11: Pin("9", Pin.OUT),
        12: Pin("D", Pin.IN),
        13: Pin("C", Pin.IN),
        14: Pin("B", Pin.IN),
        15: Pin("A", Pin.IN),
    }
    test_async = Test(
        name="Asynchronous operation",
        inputs=[12, 13, 14, 15],
        outputs=[1, 2, 3, 4, 5, 6, 7, 9, 10, 11],
        ttype=Test.COMB,
        body=[
            [[0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0, 1, 0], [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]],
            [[0, 1, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]],
            [[0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]],
            [[0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 1, 1, 1]],
            [[0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 1]],
            [[1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]],
            [[1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]],
            [[1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        ]
    )
    tests = [test_async]


# ------------------------------------------------------------------------
class Part7445(Part7442):
    name = "7445"
    desc = "BCD-to-decimal decoders/drivers"
    pin_cfg = {
        1: Pin("0", Pin.OC),
        2: Pin("1", Pin.OC),
        3: Pin("2", Pin.OC),
        4: Pin("3", Pin.OC),
        5: Pin("4", Pin.OC),
        6: Pin("5", Pin.OC),
        7: Pin("6", Pin.OC),
        9: Pin("7", Pin.OC),
        10: Pin("8", Pin.OC),
        11: Pin("9", Pin.OC),
        12: Pin("D", Pin.IN),
        13: Pin("C", Pin.IN),
        14: Pin("B", Pin.IN),
        15: Pin("A", Pin.IN),
    }


# ------------------------------------------------------------------------
class Part7447(PartDIP16):
    name = "7447"
    desc = "BCD-to-seven-segment decoders/drivers"
    pin_cfg = {
        1: Pin("B", Pin.IN),
        2: Pin("C", Pin.IN),
        3: Pin("~LT", Pin.IN),
        4: Pin("~BI/~RBO", Pin.IN),
        5: Pin("~RBI", Pin.IN),
        6: Pin("D", Pin.IN),
        7: Pin("A", Pin.IN),
        9: Pin("e", Pin.OC),
        10: Pin("d", Pin.OC),
        11: Pin("c", Pin.OC),
        12: Pin("b", Pin.OC),
        13: Pin("a", Pin.OC),
        14: Pin("g", Pin.OC),
        15: Pin("f", Pin.OC),
    }
    test_async = Test(
        name="Asynchronous operation",
        inputs=[6, 2, 1, 7,  3, 5, 4],
        outputs=[13, 12, 11, 10, 9, 15, 14],
        ttype=Test.COMB,
        body=[
            # symbols
            [[0, 0, 0, 0,  1, 1, 1], [0, 0, 0, 0, 0, 0, 1]],
            [[0, 0, 0, 1,  1, 1, 1], [1, 0, 0, 1, 1, 1, 1]],
            [[0, 0, 1, 0,  1, 1, 1], [0, 0, 1, 0, 0, 1, 0]],
            [[0, 0, 1, 1,  1, 1, 1], [0, 0, 0, 0, 1, 1, 0]],
            [[0, 1, 0, 0,  1, 1, 1], [1, 0, 0, 1, 1, 0, 0]],
            [[0, 1, 0, 1,  1, 1, 1], [0, 1, 0, 0, 1, 0, 0]],
            [[0, 1, 1, 0,  1, 1, 1], [1, 1, 0, 0, 0, 0, 0]],
            [[0, 1, 1, 1,  1, 1, 1], [0, 0, 0, 1, 1, 1, 1]],
            [[1, 0, 0, 0,  1, 1, 1], [0, 0, 0, 0, 0, 0, 0]],
            [[1, 0, 0, 1,  1, 1, 1], [0, 0, 0, 1, 1, 0, 0]],
            [[1, 0, 1, 0,  1, 1, 1], [1, 1, 1, 0, 0, 1, 0]],
            [[1, 0, 1, 1,  1, 1, 1], [1, 1, 0, 0, 1, 1, 0]],
            [[1, 1, 0, 0,  1, 1, 1], [1, 0, 1, 1, 1, 0, 0]],
            [[1, 1, 0, 1,  1, 1, 1], [0, 1, 1, 0, 1, 0, 0]],
            [[1, 1, 1, 0,  1, 1, 1], [1, 1, 1, 0, 0, 0, 0]],
            [[1, 1, 1, 1,  1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],
            # BI/RBI
            [[0, 0, 0, 0,  1, 1, 0], [1, 1, 1, 1, 1, 1, 1]],
            [[0, 0, 0, 0,  1, 0, 0], [1, 1, 1, 1, 1, 1, 1]],
            [[0, 0, 0, 0,  0, 1, 0], [1, 1, 1, 1, 1, 1, 1]],
            [[0, 0, 0, 0,  0, 0, 0], [1, 1, 1, 1, 1, 1, 1]],
            # LT
            [[1, 1, 1, 1,  0, 0, 1], [0, 0, 0, 0, 0, 0, 0]],
            [[1, 1, 1, 1,  0, 1, 1], [0, 0, 0, 0, 0, 0, 0]],
        ]
    )
    tests = [test_async]


# ------------------------------------------------------------------------
class Part7450(PartDIP14):
    name = "7450"
    desc = "Dual 2−Wide 2−Input AND/OR Invert Gate (One Gate Expandable)"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("2A", Pin.IN),
        3: Pin("2B", Pin.IN),
        4: Pin("2C", Pin.IN),
        5: Pin("2D", Pin.IN),
        6: Pin("2Y", Pin.OUT),
        8: Pin("1Y", Pin.OUT),
        9: Pin("1C", Pin.IN),
        10: Pin("1D", Pin.IN),
        11: Pin("1X", Pin.NC),
        12: Pin("~1X", Pin.NC),
        13: Pin("1B", Pin.IN),
    }
    missing = "Gate expansion is not tested"
    test_async = Test(
        name="Asynchronous operation",
        inputs=[1, 13, 9, 10,  2, 3, 4, 5],
        outputs=[8, 6],
        ttype=Test.COMB,
        body=[
            [[0, 0, 0, 0,  0, 0, 0, 0], [1, 1]],
            [[0, 0, 0, 1,  0, 0, 0, 1], [1, 1]],
            [[0, 0, 1, 0,  0, 0, 1, 0], [1, 1]],
            [[0, 0, 1, 1,  0, 0, 1, 1], [0, 0]],
            [[0, 1, 0, 0,  0, 1, 0, 0], [1, 1]],
            [[0, 1, 0, 1,  0, 1, 0, 1], [1, 1]],
            [[0, 1, 1, 0,  0, 1, 1, 0], [1, 1]],
            [[0, 1, 1, 1,  0, 1, 1, 1], [0, 0]],
            [[1, 0, 0, 0,  1, 0, 0, 0], [1, 1]],
            [[1, 0, 0, 1,  1, 0, 0, 1], [1, 1]],
            [[1, 0, 1, 0,  1, 0, 1, 0], [1, 1]],
            [[1, 0, 1, 1,  1, 0, 1, 1], [0, 0]],
            [[1, 1, 0, 0,  1, 1, 0, 0], [0, 0]],
            [[1, 1, 0, 1,  1, 1, 0, 1], [0, 0]],
            [[1, 1, 1, 0,  1, 1, 1, 0], [0, 0]],
            [[1, 1, 1, 1,  1, 1, 1, 1], [0, 0]],
        ]
    )
    tests = [test_async]


# ------------------------------------------------------------------------
class Part7451(Part7450):
    name = "7451"
    desc = "AND-OR-INVERT Gate"
    missing = None


# ------------------------------------------------------------------------
class Part7452(PartDIP14):
    name = "7452"
    desc = "AND-OR Gate (Expandable)"
    pin_cfg = {
        1: Pin("A", Pin.IN),
        2: Pin("B", Pin.IN),
        3: Pin("C", Pin.IN),
        4: Pin("D", Pin.IN),
        5: Pin("E", Pin.IN),
        6: Pin("NC", Pin.NC),
        8: Pin("Y", Pin.OUT),
        9: Pin("X", Pin.NC),
        10: Pin("F", Pin.IN),
        11: Pin("G", Pin.IN),
        12: Pin("H", Pin.IN),
        13: Pin("I", Pin.IN),
    }
    missing = "Gate expansion is not tested"
    test_async = Test(
        name="Asynchronous operation",
        inputs=[1, 2,  3, 4, 5,  10, 11,  12, 13],
        outputs=[8],
        ttype=Test.COMB,
        loops = 128,
        body = [
            [i, [(i[0] & i[1]) | (i[2] & i[3] & i[4]) | (i[5] & i[6]) | (i[7] & i[8])]]
            for i in Test.binary_combinator(9)
        ]
    )
    tests = [test_async]


# ------------------------------------------------------------------------
class Part74H53(PartDIP14):
    name = "74H53"
    desc = "Expandable 4-wide, 2-2-3-2 And-Or-Invert gate"
    pin_cfg = {
        1: Pin("A1", Pin.IN),
        2: Pin("B1", Pin.IN),
        3: Pin("B2", Pin.IN),
        4: Pin("C1", Pin.IN),
        5: Pin("C2", Pin.IN),
        6: Pin("C3", Pin.IN),
        8: Pin("~Y", Pin.OUT),
        9: Pin("D1", Pin.IN),
        10: Pin("D2", Pin.IN),
        11: Pin("X", Pin.NC),
        12: Pin("~X", Pin.NC),
        13: Pin("A2", Pin.IN),
    }
    missing = "Gate expansion is not tested"
    test_async = Test(
        name="Asynchronous operation",
        inputs=[1, 13, 2, 3, 4, 5, 6, 9, 10],
        outputs=[8],
        ttype=Test.COMB,
        body=[
            [[0, 0,  0, 0,  0, 0, 0,  0, 0], [1]],
            [[1, 0,  1, 0,  1, 0, 0,  1, 0], [1]],
            [[0, 1,  0, 1,  0, 1, 0,  0, 1], [1]],
            [[0, 1,  0, 1,  0, 0, 1,  0, 1], [1]],
            [[0, 1,  0, 1,  0, 1, 1,  0, 1], [1]],
            [[0, 1,  0, 1,  1, 0, 1,  0, 1], [1]],
            [[0, 1,  0, 1,  1, 1, 0,  0, 1], [1]],

            [[1, 1,  0, 0,  0, 0, 0,  0, 0], [0]],
            [[0, 0,  1, 1,  0, 0, 0,  0, 0], [0]],
            [[0, 0,  0, 0,  1, 1, 1,  0, 0], [0]],
            [[0, 0,  0, 0,  0, 0, 0,  1, 1], [0]],
            [[1, 1,  1, 1,  1, 1, 1,  1, 1], [0]],
        ]
    )
    tests = [test_async]


# ------------------------------------------------------------------------
class Part7453(PartDIP14):
    name = "7453"
    desc = "Expandable 4-wide, 2-input And-Or-Invert gate"
    pin_cfg = {
        1: Pin("A1", Pin.IN),
        2: Pin("B1", Pin.IN),
        3: Pin("B2", Pin.IN),
        4: Pin("C1", Pin.IN),
        5: Pin("C2", Pin.IN),
        6: Pin("NC", Pin.IN), # this is to not confuse it with 3-input version
        8: Pin("~Y", Pin.OUT),
        9: Pin("D1", Pin.IN),
        10: Pin("D2", Pin.IN),
        11: Pin("X", Pin.NC),
        12: Pin("~X", Pin.NC),
        13: Pin("A2", Pin.IN),
    }
    missing = "Gate expansion is not tested"
    test_async = Test(
        name="Asynchronous operation",
        inputs=[1, 13, 2, 3, 4, 5, 6, 9, 10],
        outputs=[8],
        ttype=Test.COMB,
        body=[
            [[0, 0,  0, 0,  0, 0, 0,  0, 0], [1]],
            [[1, 0,  1, 0,  1, 0, 0,  1, 0], [1]],
            [[0, 1,  0, 1,  0, 1, 0,  0, 1], [1]],

            [[1, 1,  0, 0,  0, 0, 0,  0, 0], [0]],
            [[0, 0,  1, 1,  0, 0, 0,  0, 0], [0]],
            [[0, 0,  0, 0,  1, 1, 0,  0, 0], [0]],
            [[0, 0,  0, 0,  0, 0, 0,  1, 1], [0]],
            [[1, 1,  1, 1,  1, 1, 0,  1, 1], [0]],
        ]
    )
    tests = [test_async]


# ------------------------------------------------------------------------
class Part7462(PartDIP14):
    name = "7462"
    desc = "AND-OR Gate Expander"
    '''
    ~X and X are outputs, but not in a TTL-levels sense: ~X is output transistor collector, X is its emmiter.
    Pin configuration does the following:
     * pulls up the collector with the internal pull-up resistor (OC output)
     * connects the emmiter to a current sink (output driven low)
    Thus, ~X becomes the actual output, and X needs to be always driven low.
    '''
    pin_cfg = {
        1: Pin("A", Pin.IN),
        2: Pin("B", Pin.IN),
        3: Pin("C", Pin.IN),
        4: Pin("D", Pin.IN),
        5: Pin("E", Pin.IN),
        6: Pin("~X", Pin.OC),
        8: Pin("X", Pin.IN),
        9: Pin("F", Pin.IN),
        10: Pin("G", Pin.IN),
        11: Pin("H", Pin.IN),
        12: Pin("I", Pin.IN),
        13: Pin("J", Pin.IN),
    }
    missing = "Gate expansion is not tested"
    test_async = Test(
        name="Asynchronous operation",
        inputs=[8,  1, 2,  3, 4, 5,  9, 10, 11,  12, 13],
        outputs=[6],
        ttype=Test.COMB,
        loops = 64,
        body = [
            [
                [0] + i,
                [not ((i[0] & i[1]) | (i[2] & i[3] & i[4]) | (i[5] & i[6] & i[7]) | (i[8] & i[9]))]
            ]
            for i in Test.binary_combinator(10)
        ]
    )
    tests = [test_async]


# ------------------------------------------------------------------------
class Part7472(PartDIP14):
    name = "7472"
    desc = "And-gated J-K master-slave flip-flops with preset and clear"
    pin_cfg = {
        1: Pin("NC", Pin.NC),
        2: Pin("~CLR", Pin.IN),
        3: Pin("J1", Pin.IN),
        4: Pin("J2", Pin.IN),
        5: Pin("J3", Pin.IN),
        6: Pin("~Q", Pin.IN),
        8: Pin("Q", Pin.OUT),
        9: Pin("K1", Pin.OUT),
        10: Pin("K2", Pin.IN),
        11: Pin("K3", Pin.IN),
        12: Pin("CLK", Pin.IN),
        13: Pin("~PRE", Pin.IN),
    }
    test_sync = Test(
        name="Load, clear, toogle, keep",
        inputs=[3, 4, 5,  9, 10, 11,  13, 2, 12],
        outputs=[8, 6],
        ttype=Test.SEQ,
        body=[
            # load 1
            [[1, 1, 1,  0, 0, 0,  1, 1, '-'], [1, 0]],
            # keep
            [[0, 0, 0,  0, 0, 0,  1, 1, '-'], [1, 0]],
            # load 0
            [[0, 0, 0,  1, 1, 1,  1, 1, '-'], [0, 1]],
            # keep
            [[0, 0, 0,  0, 0, 0,  1, 1, '-'], [0, 1]],
            # toggle
            [[1, 1, 1,  1, 1, 1,  1, 1, '-'], [1, 0]],
            # keep
            [[0, 0, 0,  0, 0, 0,  1, 1, '-'], [1, 0]],
            # toggle
            [[1, 1, 1,  1, 1, 1,  1, 1, '-'], [0, 1]],
        ]
    )
    test_async = Test(
        name="Set, preset",
        inputs=[3, 4, 5,  9, 10, 11,  13, 2, 12],
        outputs=[8, 6],
        ttype=Test.SEQ,
        body=[
            [[0, 0, 0,  1, 1, 1,  0, 1, '-'], [1, 0]],
            [[1, 1, 1,  0, 0, 0,  1, 0, '-'], [0, 1]],
            [[0, 0, 0,  1, 1, 1,  0, 1, '-'], [1, 0]],
            [[1, 1, 1,  0, 0, 0,  1, 0, '-'], [0, 1]],
            [[1, 1, 1,  1, 1, 1,  0, 1, '-'], [1, 0]],
            [[1, 1, 1,  1, 1, 1,  1, 0, '-'], [0, 1]],
            [[0, 0, 0,  0, 0, 0,  0, 1, '-'], [1, 0]],
            [[0, 0, 0,  0, 0, 0,  1, 0, '-'], [0, 1]],
        ]
    )
    test_and = Test(
        name="And input gates",
        inputs=[3, 4, 5,  9, 10, 11,  13, 2, 12],
        outputs=[8, 6],
        ttype=Test.SEQ,
        body=[
            # try J=1 with not fully set K
            [[1, 1, 1,  0, 0, 0,  1, 1, '-'], [1, 0]],
            [[1, 1, 1,  0, 0, 1,  1, 1, '-'], [1, 0]],
            [[1, 1, 1,  0, 1, 0,  1, 1, '-'], [1, 0]],
            [[1, 1, 1,  0, 1, 1,  1, 1, '-'], [1, 0]],
            [[1, 1, 1,  1, 0, 0,  1, 1, '-'], [1, 0]],
            [[1, 1, 1,  1, 0, 1,  1, 1, '-'], [1, 0]],
            [[1, 1, 1,  1, 1, 0,  1, 1, '-'], [1, 0]],
            [[1, 1, 1,  1, 1, 1,  1, 1, '-'], [0, 1]],

            # try K=1 with not fully set J
            [[0, 0, 0,  1, 1, 1,  1, 1, '-'], [0, 1]],
            [[0, 0, 1,  1, 1, 1,  1, 1, '-'], [0, 1]],
            [[0, 1, 0,  1, 1, 1,  1, 1, '-'], [0, 1]],
            [[0, 1, 1,  1, 1, 1,  1, 1, '-'], [0, 1]],
            [[1, 0, 0,  1, 1, 1,  1, 1, '-'], [0, 1]],
            [[1, 0, 1,  1, 1, 1,  1, 1, '-'], [0, 1]],
            [[1, 1, 0,  1, 1, 1,  1, 1, '-'], [0, 1]],
            [[1, 1, 1,  1, 1, 1,  1, 1, '-'], [1, 0]],
        ]
    )

    tests = [test_sync, test_async, test_and]


# ------------------------------------------------------------------------
class Part7473(PartDIP14_vcc4):
    name = "7473"
    desc = "Dual J−K Flip−Flop with Clear"
    pin_cfg = {
        1: Pin("1CLK", Pin.IN),
        2: Pin("~1CLR", Pin.IN),
        3: Pin("1K", Pin.IN),
        5: Pin("2CLK", Pin.IN),
        6: Pin("~2CLR", Pin.IN),
        7: Pin("2J", Pin.IN),
        8: Pin("~2Q", Pin.OUT),
        9: Pin("2Q", Pin.OUT),
        10: Pin("2K", Pin.IN),
        12: Pin("1Q", Pin.OUT),
        13: Pin("~1Q", Pin.OUT),
        14: Pin("1J", Pin.IN),
    }
    test_all = Test(
        name="Sync/Async operation",
        inputs=[14, 3, 2, 1,  7, 10, 6, 5],
        outputs=[12, 13, 9, 8],
        ttype=Test.SEQ,
        body=[
            # load 1
            [[1, 0, 1, '-',  1, 0, 1, '-'], [1, 0,  1, 0]],
            # keep
            [[0, 0, 1, '-',  0, 0, 1, '-'], [1, 0,  1, 0]],
            # load 0
            [[0, 1, 1, '-',  0, 1, 1, '-'], [0, 1,  0, 1]],
            # keep
            [[0, 0, 1, '-',  0, 0, 1, '-'], [0, 1,  0, 1]],
            # toggle
            [[1, 1, 1, '-',  1, 1, 1, '-'], [1, 0,  1, 0]],
            # keep
            [[0, 0, 1, '-',  0, 0, 1, '-'], [1, 0,  1, 0]],

            # clear with J=0, K=0
            [[1, 0, 1, '-',  1, 0, 1, '-'], [1, 0,  1, 0]],
            [[0, 0, 0, '-',  0, 0, 0, '-'], [0, 1,  0, 1]],
            # clear with J=1, K=0
            [[1, 0, 1, '-',  1, 0, 1, '-'], [1, 0,  1, 0]],
            [[1, 0, 0, '-',  1, 0, 0, '-'], [0, 1,  0, 1]],
            # clear with J=0, K=1
            [[1, 0, 1, '-',  1, 0, 1, '-'], [1, 0,  1, 0]],
            [[0, 1, 0, '-',  1, 0, 0, '-'], [0, 1,  0, 1]],
            # clear with J=1, K=1
            [[1, 0, 1, '-',  1, 0, 1, '-'], [1, 0,  1, 0]],
            [[1, 1, 0, '-',  1, 0, 0, '-'], [0, 1,  0, 1]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part7474(PartDIP14):
    name = "7474"
    desc = "Dual D-type positive-edge-triggered flip-flops with preset and clear"
    pin_cfg = {
        1: Pin("~1CLR", Pin.IN),
        2: Pin("1D", Pin.IN),
        3: Pin("1CLK", Pin.IN),
        4: Pin("~1PRE", Pin.IN),
        5: Pin("1Q", Pin.OUT),
        6: Pin("~1Q", Pin.OUT),
        8: Pin("~2Q", Pin.OUT),
        9: Pin("2Q", Pin.OUT),
        10: Pin("~2PRE", Pin.IN),
        11: Pin("2CLK", Pin.IN),
        12: Pin("2D", Pin.IN),
        13: Pin("~2CLR", Pin.IN),
    }
    test_sync = Test(
        name="Synchronous operation",
        inputs=[1, 4, 2, 3, 13, 10, 12, 11],
        outputs=[5, 6, 9, 8],
        ttype=Test.SEQ,
        body=[
            [[1, 1, 0, '+',  1, 1, 0, '+'], [0, 1,  0, 1]],
            [[1, 1, 1, '+',  1, 1, 1, '+'], [1, 0,  1, 0]],
        ]
    )
    test_async = Test(
        name="Asynchronous operation",
        inputs=[1, 4, 2, 3, 13, 10, 12, 11],
        outputs=[5, 6, 9, 8],
        ttype=Test.COMB,
        body=[
            [[0, 1, 0, 0,  0, 1, 0, 0], [0, 1,  0, 1]],
            [[1, 0, 0, 0,  1, 0, 0, 0], [1, 0,  1, 0]],
        ]
    )
    tests = [test_sync, test_async]


# ------------------------------------------------------------------------
class Part7475(PartDIP16_vcc5):
    name = "7475"
    desc = "4-bit bistable latches"
    pin_cfg = {
        1: Pin("~1Q", Pin.OUT),
        2: Pin("1D", Pin.IN),
        3: Pin("2D", Pin.IN),
        4: Pin("3C,4C", Pin.IN),
        6: Pin("3D", Pin.IN),
        7: Pin("4D", Pin.IN),
        8: Pin("~4Q", Pin.OUT),
        9: Pin("4Q", Pin.OUT),
        10: Pin("3Q", Pin.OUT),
        11: Pin("~3Q", Pin.OUT),
        13: Pin("1C,2C", Pin.IN),
        14: Pin("~2Q", Pin.OUT),
        15: Pin("2Q", Pin.OUT),
        16: Pin("1Q", Pin.OUT),
    }
    test_async = Test(
        name="Asynchronous operation",
        inputs=[2, 3, 13,  6, 7, 4],
        outputs=[16, 1,  15, 14,  10, 11,  9, 8],
        ttype=Test.COMB,
        body=[
            [[0, 0, 1,  0, 0, 1], [0, 1,  0, 1,  0, 1,  0, 1]],
            [[1, 1, 0,  1, 1, 0], [0, 1,  0, 1,  0, 1,  0, 1]],

            [[0, 1, 1,  0, 1, 1], [0, 1,  1, 0,  0, 1,  1, 0]],
            [[1, 0, 0,  1, 0, 0], [0, 1,  1, 0,  0, 1,  1, 0]],

            [[1, 0, 1,  1, 0, 1], [1, 0,  0, 1,  1, 0,  0, 1]],
            [[0, 1, 0,  0, 1, 0], [1, 0,  0, 1,  1, 0,  0, 1]],

            [[1, 1, 1,  1, 1, 1], [1, 0,  1, 0,  1, 0,  1, 0]],
            [[0, 0, 0,  0, 0, 0], [1, 0,  1, 0,  1, 0,  1, 0]],
        ]
    )
    tests = [test_async]


# ------------------------------------------------------------------------
class Part7483(PartDIP16_vcc5):
    name = "7483"
    desc = "4-bit binary full adder with fast carry"
    pin_cfg = {
        1: Pin("A4", Pin.IN),
        2: Pin("S3", Pin.OUT),
        3: Pin("A3", Pin.IN),
        4: Pin("B3", Pin.IN),
        6: Pin("S2", Pin.OUT),
        7: Pin("B2", Pin.IN),
        8: Pin("A2", Pin.IN),
        9: Pin("S1", Pin.OUT),
        10: Pin("A1", Pin.IN),
        11: Pin("B1", Pin.IN),
        13: Pin("C0", Pin.IN),
        14: Pin("C4", Pin.OUT),
        15: Pin("S4", Pin.OUT),
        16: Pin("B4", Pin.IN),
    }

    # ------------------------------------------------------------------------
    def add_test_gen():
        Vector = namedtuple('Vector', ['a', 'b', 'c', 'f'])

        # raw, numerical test data
        data = [
            Vector(a, b, c, a + b + c)
            for a in range(0, 16)
            for b in range(0, 16)
            for c in range(0, 2)
        ]

        # test vectors in [[inputs], [outputs]] order:
        # [[cin, a4, a3, a2, a1,  b4, b3, b2, b1], [f4, f3, f2, f1,  cout]]
        body = [
            [
                [v.c] + Test.bin2vec(v.a, 4) + Test.bin2vec(v.b, 4),
                Test.bin2vec(v.f & 0b1111, 4) + [True if v.f & 0b10000 else False]
            ]
            for v in data
        ]
        return body

    test_all = Test(
        name="Complete logic",
        inputs=[13,  1, 3, 8, 10,  16, 4, 7, 11],
        outputs=[15, 2, 6, 9,  14],
        ttype=Test.COMB,
        body=add_test_gen()
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part7486(PartDIP14):
    name = "7486"
    desc = "Quad 2-input exclusive-OR gates"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("1Y", Pin.OUT),
        4: Pin("2A", Pin.IN),
        5: Pin("2B", Pin.IN),
        6: Pin("2Y", Pin.OUT),
        8: Pin("3Y", Pin.OUT),
        9: Pin("3A", Pin.IN),
        10: Pin("3B", Pin.IN),
        11: Pin("4Y", Pin.OUT),
        12: Pin("4A", Pin.IN),
        13: Pin("4B", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[1, 2, 4, 5, 10, 9, 13, 12],
        outputs=[3, 6, 8, 11],
        ttype=Test.COMB,
        body=Test.binary_fun_gen(4, 2, lambda a, b: a ^ b)
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part7487(PartDIP14):
    name = "7487"
    desc = "4-bit True/Complement, Zero/One Element"
    pin_cfg = {
        1: Pin("C", Pin.IN),
        2: Pin("A1", Pin.IN),
        3: Pin("Y1", Pin.OUT),
        4: Pin("NC", Pin.NC),
        5: Pin("A2", Pin.IN),
        6: Pin("Y2", Pin.OUT),
        8: Pin("B", Pin.IN),
        9: Pin("Y3", Pin.OUT),
        10: Pin("A3", Pin.IN),
        11: Pin("NC", Pin.NC),
        12: Pin("Y4", Pin.OUT),
        13: Pin("A4", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[8, 1,  2, 5, 10, 13],
        outputs=[3, 6, 9, 12],
        ttype=Test.COMB,
        body=[
            [[0, 0,  0, 0, 0, 0], [1, 1, 1, 1]],
            [[0, 0,  1, 1, 1, 1], [0, 0, 0, 0]],
            [[0, 1,  0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 1,  1, 1, 1, 1], [1, 1, 1, 1]],
            [[1, 0,  0, 0, 0, 0], [1, 1, 1, 1]],
            [[1, 0,  1, 1, 1, 1], [1, 1, 1, 1]],
            [[1, 1,  0, 0, 0, 0], [0, 0, 0, 0]],
            [[1, 1,  1, 1, 1, 1], [0, 0, 0, 0]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part7489(PartDIP16):
    name = "7489"
    desc = "64-bit random-access read/write memory"
    pin_cfg = {
        1: Pin("A0", Pin.IN),
        2: Pin("~ME", Pin.IN),
        3: Pin("~WE", Pin.IN),
        4: Pin("D1", Pin.IN),
        5: Pin("~Q1", Pin.OC),
        6: Pin("D2", Pin.IN),
        7: Pin("~Q2", Pin.OC),
        9: Pin("~Q3", Pin.OC),
        10: Pin("D3", Pin.IN),
        11: Pin("~Q4", Pin.OC),
        12: Pin("D4", Pin.IN),
        13: Pin("A3", Pin.IN),
        14: Pin("A2", Pin.IN),
        15: Pin("A1", Pin.IN),
    }
    # ------------------------------------------------------------------------
    def mem_rw_test_gen():
        # --------------------------------------------------------------------
        def rw_cycle(addr_vec):
            return [
                # write 1s
                [addr_vec + [1, 1, 1, 1,  1, 1], [1, 1, 1, 1]],  # NONE: ou = 1
                [addr_vec + [1, 1, 1, 1,  0, 0], [0, 0, 0, 0]],  # WRITE: ou = ~in
                [addr_vec + [1, 1, 1, 1,  1, 1], [1, 1, 1, 1]],  # NONE: ou = 1
                [addr_vec + [0, 0, 0, 0,  1, 0], [1, 1, 1, 1]],  # WR INHIBIT (with data inputs swapped): ou = ~in
                # read 1s
                [addr_vec + [1, 1, 1, 1,  0, 1], [0, 0, 0, 0]],  # READ: ou = ~mem word
                [addr_vec + [1, 1, 1, 1,  1, 1], [1, 1, 1, 1]],  # NONE ou = 1
                # write 0s
                [addr_vec + [0, 0, 0, 0,  1, 1], [1, 1, 1, 1]],  # NONE: ou = 1
                [addr_vec + [0, 0, 0, 0,  0, 0], [1, 1, 1, 1]],  # WRITE: ou = ~in
                [addr_vec + [0, 0, 0, 0,  1, 1], [1, 1, 1, 1]],  # NONE: ou = 1
                [addr_vec + [1, 1, 1, 1,  1, 0], [0, 0, 0, 0]],  # WR INHIBIT (with data inputs swapped): ou = ~in
                # read 0s
                [addr_vec + [0, 0, 0, 0,  0, 1], [1, 1, 1, 1]],  # READ: ou = ~mem word
                [addr_vec + [0, 0, 0, 0,  1, 1], [1, 1, 1, 1]],  # NONE: ou = 1
            ]

        body = []
        for v in Test.binary_combinator(4):
            body.extend(rw_cycle(v))

        return Test(
            name="Complete array",
            inputs=[1, 15, 14, 13,  4, 6, 10, 12,  2, 3],
            outputs=[5, 7, 9, 11],
            ttype=Test.COMB,
            body=body,
            loops=256,
        )

    tests = [mem_rw_test_gen()]


# ------------------------------------------------------------------------
class Part780101(Part7489):
    name = "780101"
    '''
    Similar to 7489. Same pinout, but differences in behavior:
     * outputs are always high during write
     * outputs are always high when CS is high
    '''
    # ------------------------------------------------------------------------
    def mem_rw_test_gen():
        # --------------------------------------------------------------------
        def rw_cycle(addr_vec):
            return [
                # write 1s
                [addr_vec + [1, 1, 1, 1,  1, 1], [1, 1, 1, 1]],  # NONE: ou = 1
                [addr_vec + [1, 1, 1, 1,  0, 0], [1, 1, 1, 1]],  # WRITE: ou = 1
                [addr_vec + [1, 1, 1, 1,  1, 1], [1, 1, 1, 1]],  # NONE: ou = 1
                [addr_vec + [0, 0, 0, 0,  1, 0], [1, 1, 1, 1]],  # NONE: ou = 1
                # read 1s
                [addr_vec + [1, 1, 1, 1,  0, 1], [0, 0, 0, 0]],  # READ: ou = ~mem word
                [addr_vec + [1, 1, 1, 1,  1, 1], [1, 1, 1, 1]],  # NONE ou = 1
                # write 0s
                [addr_vec + [0, 0, 0, 0,  1, 1], [1, 1, 1, 1]],  # NONE: ou = 1
                [addr_vec + [0, 0, 0, 0,  0, 0], [1, 1, 1, 1]],  # WRITE: ou = 1
                [addr_vec + [0, 0, 0, 0,  1, 1], [1, 1, 1, 1]],  # NONE: ou = 1
                [addr_vec + [1, 1, 1, 1,  1, 0], [1, 1, 1, 1]],  # NONE: ou = 1
                # read 0s
                [addr_vec + [0, 0, 0, 0,  0, 1], [1, 1, 1, 1]],  # READ: ou = ~mem word
                [addr_vec + [0, 0, 0, 0,  1, 1], [1, 1, 1, 1]],  # NONE: ou = 1
            ]

        body = []
        for v in Test.binary_combinator(4):
            body.extend(rw_cycle(v))

        return Test(
            name="Complete array",
            inputs=[1, 15, 14, 13,  4, 6, 10, 12,  2, 3],
            outputs=[5, 7, 9, 11],
            ttype=Test.COMB,
            body=body,
            loops=256,
        )

    tests = [mem_rw_test_gen()]


# ------------------------------------------------------------------------
class Part7490(PartDIP14_vcc5):
    name = "7490"
    desc = "Decade counter"
    pin_cfg = {
        1: Pin("CKB", Pin.IN),
        2: Pin("R0(1)", Pin.IN),
        3: Pin("R0(2)", Pin.IN),
        4: Pin("NC", Pin.NC),
        6: Pin("R9-1", Pin.IN),
        7: Pin("R9-2", Pin.IN),
        8: Pin("QC", Pin.OUT),
        9: Pin("QB", Pin.OUT),
        11: Pin("QD", Pin.OUT),
        12: Pin("QA", Pin.OUT),
        13: Pin("NC", Pin.NC),
        14: Pin("CKA", Pin.IN),
    }
    test_resets = Test(
        name="Resets",
        inputs=[2, 3,  6, 7,  14, 1],
        outputs=[12, 9, 8, 11],
        ttype=Test.COMB,
        body=[
            # resets
            [[1, 1,  0, 0,  0, 0], [0, 0, 0, 0]],
            [[1, 1,  0, 1,  0, 0], [0, 0, 0, 0]],
            [[0, 0,  1, 1,  0, 0], [1, 0, 0, 1]],
            [[0, 1,  1, 1,  0, 0], [1, 0, 0, 1]],
            [[1, 0,  1, 1,  0, 0], [1, 0, 0, 1]],
            [[1, 1,  1, 1,  0, 0], [1, 0, 0, 1]],
        ]
    )
    test_count_cka = Test(
        name="Count CKA",
        inputs=[2, 3,  6, 7,  14, 1],
        outputs=[12, 11, 8, 9],
        ttype=Test.SEQ,
        body=[
            # reset
            [[1, 1,  0, 0,  0, 0], [0, 0, 0, 0]],
            # count CKA
            [[0, 0,  0, 0,  '-', 0], [1, 0, 0, 0]],
            [[0, 0,  0, 0,  '-', 0], [0, 0, 0, 0]],
            [[0, 0,  0, 0,  '-', 0], [1, 0, 0, 0]],
        ]
    )
    test_count_ckb = Test(
        name="Count CKB",
        inputs=[2, 3,  6, 7,  14, 1],
        outputs=[12, 11, 8, 9],
        ttype=Test.SEQ,
        body=[
            #reset
            [[1, 1,  0, 0,  0, 0], [0, 0, 0, 0]],
            # count CKB
            [[0, 0,  0, 0,  0, '-'], [0, 0, 0, 1]],
            [[0, 0,  0, 0,  0, '-'], [0, 0, 1, 0]],
            [[0, 0,  0, 0,  0, '-'], [0, 0, 1, 1]],
            [[0, 0,  0, 0,  0, '-'], [0, 1, 0, 0]],
            [[0, 0,  0, 0,  0, '-'], [0, 0, 0, 0]],
            # count CKB again to fill bits with 1s
            [[0, 0,  0, 0,  0, '-'], [0, 0, 0, 1]],
            [[0, 0,  0, 0,  0, '-'], [0, 0, 1, 0]],
            [[0, 0,  0, 0,  0, '-'], [0, 0, 1, 1]],
        ]
    )
    tests = [test_resets, test_count_cka, test_count_ckb]


# ------------------------------------------------------------------------
class Part7493(PartDIP14_vcc5):
    name = "7493"
    desc = "4-bit binary counter"
    pin_cfg = {
        1: Pin("CKB", Pin.IN),
        2: Pin("R0(1)", Pin.IN),
        3: Pin("R0(2)", Pin.IN),
        4: Pin("NC", Pin.NC),
        6: Pin("NC", Pin.NC),
        7: Pin("NC", Pin.NC),
        8: Pin("QC", Pin.OUT),
        9: Pin("QB", Pin.OUT),
        11: Pin("QD", Pin.OUT),
        12: Pin("QA", Pin.OUT),
        13: Pin("NC", Pin.NC),
        14: Pin("CKA", Pin.IN),
    }
    test_count = Test(
        name="Count",
        inputs=[2, 3,  14, 1],
        outputs=[12, 9, 8, 11],
        ttype=Test.SEQ,
        body=[
            # reset
            [['-', '-',  0, 0], [0, 0, 0, 0]],
            # count CKA
            [[0, 0,  '-', 0], [1, 0, 0, 0]],
            [[0, 0,  '-', 0], [0, 0, 0, 0]],
            [[0, 0,  '-', 0], [1, 0, 0, 0]],
            # reset
            [['-', '-',  0, 0], [0, 0, 0, 0]],
            # count CKB
            [[0, 0,  0, '-'], [0, 1, 0, 0]],
            [[0, 0,  0, '-'], [0, 0, 1, 0]],
            [[0, 0,  0, '-'], [0, 1, 1, 0]],
            [[0, 0,  0, '-'], [0, 0, 0, 1]],
            [[0, 0,  0, '-'], [0, 1, 0, 1]],
            [[0, 0,  0, '-'], [0, 0, 1, 1]],
            [[0, 0,  0, '-'], [0, 1, 1, 1]],
            [[0, 0,  0, '-'], [0, 0, 0, 0]],
            # count CKB again to fill all bits with 1s
            [[0, 0,  0, '-'], [0, 1, 0, 0]],
            [[0, 0,  0, '-'], [0, 0, 1, 0]],
            [[0, 0,  0, '-'], [0, 1, 1, 0]],
            [[0, 0,  0, '-'], [0, 0, 0, 1]],
            [[0, 0,  0, '-'], [0, 1, 0, 1]],
            [[0, 0,  0, '-'], [0, 0, 1, 1]],
            [[0, 0,  0, '-'], [0, 1, 1, 1]],
            # no reset
            [[0, '-',  0, 0], [0, 1, 1, 1]],
            [['-', 0,  0, 0], [0, 1, 1, 1]],
        ]
    )
    tests = [test_count]


# ------------------------------------------------------------------------
class Part7495(PartDIP14):
    name = "7495"
    desc = "4-bit parallel-access shift registers"
    pin_cfg = {
        1: Pin("SER", Pin.IN),
        2: Pin("A", Pin.IN),
        3: Pin("B", Pin.IN),
        4: Pin("C", Pin.IN),
        5: Pin("D", Pin.IN),
        6: Pin("MODE", Pin.IN),
        8: Pin("CLK2", Pin.IN),
        9: Pin("CLK1", Pin.IN),
        10: Pin("QD", Pin.OUT),
        11: Pin("QC", Pin.OUT),
        12: Pin("QB", Pin.OUT),
        13: Pin("QA", Pin.OUT),
    }
    test_load = Test(
        name="Parallel load",
        inputs=[6, 8, 9, 1, 2, 3, 4, 5],
        outputs=[13, 12, 11, 10],
        ttype=Test.SEQ,
        body=[
            [[1, '-', 0, 0, 1, 1, 1, 1], [1, 1, 1, 1]],
            [[1, '-', 0, 0, 0, 0, 0, 0], [0, 0, 0, 0]],
        ]
    )
    test_rshift = Test(
        name="Right Shift",
        inputs=[6, 8, 9, 1, 2, 3, 4, 5],
        outputs=[13, 12, 11, 10],
        ttype=Test.SEQ,
        body=[
            # set known starting value
            [[1, '-', 0, 0, 0, 0, 0, 0], [0, 0, 0, 0]],
            # test shift
            [[0, 0, '-', 0, 0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, '-', 1, 0, 0, 0, 0], [1, 0, 0, 0]],
            [[0, 0, '-', 0, 0, 0, 0, 0], [0, 1, 0, 0]],
            [[0, 0, '-', 1, 0, 0, 0, 0], [1, 0, 1, 0]],
            [[0, 0, '-', 0, 0, 0, 0, 0], [0, 1, 0, 1]],
            [[0, 0, '-', 1, 0, 0, 0, 0], [1, 0, 1, 0]],
            [[0, 0, '-', 0, 0, 0, 0, 0], [0, 1, 0, 1]],
            [[0, 0, '-', 0, 0, 0, 0, 0], [0, 0, 1, 0]],
            [[0, 0, '-', 0, 0, 0, 0, 0], [0, 0, 0, 1]],
            [[0, 0, '-', 0, 0, 0, 0, 0], [0, 0, 0, 0]],
        ]
    )
    tests = [test_load, test_rshift]


# ------------------------------------------------------------------------
class Part7496(PartDIP16_vcc5):
    name = "7496"
    desc = "5-bit shift register"
    pin_cfg = {
        1: Pin("CLK", Pin.IN),
        2: Pin("A", Pin.IN),
        3: Pin("B", Pin.IN),
        4: Pin("C", Pin.IN),
        6: Pin("D", Pin.IN),
        7: Pin("E", Pin.IN),
        8: Pin("PRE", Pin.IN),
        9: Pin("SER", Pin.IN),
        10: Pin("QE", Pin.OUT),
        11: Pin("QD", Pin.OUT),
        13: Pin("QC", Pin.OUT),
        14: Pin("QB", Pin.OUT),
        15: Pin("QA", Pin.OUT),
        16: Pin("CLR", Pin.IN),
    }

    test_preset = Test(
        name="Preset",
        inputs=[16, 8,  2, 3, 4, 6, 7,  1, 9],
        outputs=[15, 14, 13, 11, 10],
        ttype=Test.COMB,
        body=[
            # preset all 1
            [[1, 1,  1, 1, 1, 1, 1,  0, 0], [1, 1, 1, 1, 1]],
            # clear
            [[0, 0,  0, 0, 0, 0, 0,  0, 0], [0, 0, 0, 0, 0]],
            # preset selective 1s
            [[1, 1,  0, 0, 0, 0, 1,  0, 0], [0, 0, 0, 0, 1]],
            [[1, 1,  0, 0, 0, 1, 0,  0, 0], [0, 0, 0, 1, 1]],
            [[1, 1,  0, 0, 1, 0, 0,  0, 0], [0, 0, 1, 1, 1]],
            [[1, 1,  0, 1, 0, 0, 0,  0, 0], [0, 1, 1, 1, 1]],
            [[1, 1,  1, 0, 0, 0, 0,  0, 0], [1, 1, 1, 1, 1]],
            # clear, preset known
            [[0, 0,  0, 0, 0, 0, 0,  0, 0], [0, 0, 0, 0, 0]],
            [[1, 1,  0, 1, 0, 1, 0,  0, 0], [0, 1, 0, 1, 0]],
            # no action
            [[1, 0,  1, 1, 1, 1, 1,  0, 0], [0, 1, 0, 1, 0]],
        ]
    )

    test_clear = Test(
        name="Clear",
        inputs=[16, 8,  2, 3, 4, 6, 7,  1, 9],
        outputs=[15, 14, 13, 11, 10],
        ttype=Test.COMB,
        body=[
            # preset/clear
            [[1, 1,  1, 1, 1, 1, 1,  0, 0], [1, 1, 1, 1, 1]],
            [[0, 0,  0, 0, 0, 0, 0,  0, 0], [0, 0, 0, 0, 0]],
            # preset/clear
            [[1, 1,  1, 1, 1, 1, 1,  0, 0], [1, 1, 1, 1, 1]],
            [[0, 1,  0, 0, 0, 0, 0,  0, 0], [0, 0, 0, 0, 0]],
            # preset/clear
            [[1, 1,  1, 1, 1, 1, 1,  0, 0], [1, 1, 1, 1, 1]],
            [[0, 0,  1, 1, 1, 1, 1,  0, 0], [0, 0, 0, 0, 0]],
        ]
    )

    test_serial_in = Test(
        name="Serial in",
        inputs=[16, 8,  2, 3, 4, 6, 7,  1, 9],
        outputs=[15, 14, 13, 11, 10],
        ttype=Test.COMB,
        body=[
            # clear, preset known
            [[0, 0,  0, 0, 0, 0, 0,  0, 0], [0, 0, 0, 0, 0]],
            [[1, 1,  1, 0, 1, 0, 1,  0, 0], [1, 0, 1, 0, 1]],
            # shift in 1s
            [[1, 0,  1, 1, 1, 1, 1,  0, 1], [1, 0, 1, 0, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  1, 1], [1, 1, 0, 1, 0]],
            [[1, 0,  1, 1, 1, 1, 1,  0, 1], [1, 1, 0, 1, 0]],
            [[1, 0,  1, 1, 1, 1, 1,  1, 1], [1, 1, 1, 0, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  0, 1], [1, 1, 1, 0, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  1, 1], [1, 1, 1, 1, 0]],
            [[1, 0,  1, 1, 1, 1, 1,  0, 1], [1, 1, 1, 1, 0]],
            [[1, 0,  1, 1, 1, 1, 1,  1, 1], [1, 1, 1, 1, 1]],
            # shift in 0s
            [[1, 0,  1, 1, 1, 1, 1,  0, 0], [1, 1, 1, 1, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  1, 0], [0, 1, 1, 1, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  0, 0], [0, 1, 1, 1, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  1, 0], [0, 0, 1, 1, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  0, 0], [0, 0, 1, 1, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  1, 0], [0, 0, 0, 1, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  0, 0], [0, 0, 0, 1, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  1, 0], [0, 0, 0, 0, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  0, 0], [0, 0, 0, 0, 1]],
            [[1, 0,  1, 1, 1, 1, 1,  1, 0], [0, 0, 0, 0, 0]],
        ]
    )

    tests = [
        test_preset,
        test_clear,
        test_serial_in,
    ]


# ------------------------------------------------------------------------
class Part74107(PartDIP14):
    name = "74107"
    desc = "Dual J-K flip-flops with clear"
    pin_cfg = {
        1: Pin("1J", Pin.IN),
        2: Pin("~1Q", Pin.OUT),
        3: Pin("1Q", Pin.OUT),
        4: Pin("1K", Pin.IN),
        5: Pin("2Q", Pin.OUT),
        6: Pin("~2Q", Pin.OUT),
        8: Pin("2J", Pin.IN),
        9: Pin("2CLK", Pin.IN),
        10: Pin("~2CLR", Pin.IN),
        11: Pin("2K", Pin.IN),
        12: Pin("1CLK", Pin.IN),
        13: Pin("~1CLR", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[1, 4, 12, 13,  8, 11, 9, 10],
        outputs=[3, 2,  5, 6],
        ttype=Test.SEQ,
        body=[
            # reset
            [[1, 1, '-', 0,  1, 1, '-', 0], [0, 1,  0, 1]],
            # J
            [[1, 0, '-', 1,  1, 0, '-', 1], [1, 0,  1, 0]],
            # hold
            [[0, 0, '-', 1,  0, 0, '-', 1], [1, 0,  1, 0]],
            # toggle
            [[1, 1, '-', 1,  1, 1, '-', 1], [0, 1,  0, 1]],
            # toggle
            [[1, 1, '-', 1,  1, 1, '-', 1], [1, 0,  1, 0]],
            # K
            [[0, 1, '-', 1,  0, 1, '-', 1], [0, 1,  0, 1]],
            # toggle
            [[1, 1, '-', 1,  1, 1, '-', 1], [1, 0,  1, 0]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part74125(PartDIP14):
    name = "74125"
    desc = "Quarduple bus buffers with 3-state outputs"
    pin_cfg = {
        1: Pin("~1G", Pin.IN),
        2: Pin("1A", Pin.IN),
        3: Pin("1Y", Pin.OC),
        4: Pin("~2G", Pin.IN),
        5: Pin("2A", Pin.IN),
        6: Pin("2Y", Pin.OC),
        8: Pin("3Y", Pin.OC),
        9: Pin("3A", Pin.IN),
        10: Pin("~3G", Pin.IN),
        11: Pin("4Y", Pin.OC),
        12: Pin("4A", Pin.IN),
        13: Pin("~4G", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[1, 2,  4, 5,  10, 9,  13, 12],
        outputs=[3, 6, 8, 11],
        ttype=Test.COMB,
        body=[
            [[0, 1,  0, 1,  0, 1,  0, 1], [1, 1, 1, 1]],
            [[0, 0,  0, 0,  0, 0,  0, 0], [0, 0, 0, 0]],
            [[1, 1,  1, 1,  1, 1,  1, 1], [1, 1, 1, 1]],
            [[1, 0,  1, 0,  1, 0,  1, 0], [1, 1, 1, 1]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part74126(PartDIP14):
    name = "74126"
    desc = "Quarduple bus buffers with 3-state outputs"
    pin_cfg = {
        1: Pin("1G", Pin.IN),
        2: Pin("1A", Pin.IN),
        3: Pin("1Y", Pin.OC),
        4: Pin("2G", Pin.IN),
        5: Pin("2A", Pin.IN),
        6: Pin("2Y", Pin.OC),
        8: Pin("3Y", Pin.OC),
        9: Pin("3A", Pin.IN),
        10: Pin("3G", Pin.IN),
        11: Pin("4Y", Pin.OC),
        12: Pin("4A", Pin.IN),
        13: Pin("4G", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[1, 2,  4, 5,  10, 9,  13, 12],
        outputs=[3, 6, 8, 11],
        ttype=Test.COMB,
        body=[
            [[1, 1,  1, 1,  1, 1,  1, 1], [1, 1, 1, 1]],
            [[1, 0,  1, 0,  1, 0,  1, 0], [0, 0, 0, 0]],
            [[0, 1,  0, 1,  0, 1,  0, 1], [1, 1, 1, 1]],
            [[0, 0,  0, 0,  0, 0,  0, 0], [1, 1, 1, 1]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part74132(Part7400):
    name = "74132"
    desc = "Quad 2-input positive-NAND Shmitt triggers"


# ------------------------------------------------------------------------
class Part74136(PartDIP14):
    name = "74136"
    desc = "Quarduple 2-input exclusive-OR gates with open-collector outputs"
    pin_cfg = {
        1: Pin("1A", Pin.IN),
        2: Pin("1B", Pin.IN),
        3: Pin("1Y", Pin.OC),
        4: Pin("2A", Pin.IN),
        5: Pin("2B", Pin.IN),
        6: Pin("2Y", Pin.OC),
        8: Pin("3Y", Pin.OC),
        9: Pin("3A", Pin.IN),
        10: Pin("3B", Pin.IN),
        11: Pin("4Y", Pin.OC),
        12: Pin("4A", Pin.IN),
        13: Pin("4B", Pin.IN),
    }
    tests = [
        Test(
            name="Complete logic",
            inputs=[1, 2, 4, 5, 10, 9, 13, 12],
            outputs=[3, 6, 8, 11],
            ttype=Test.COMB,
            body=Test.binary_fun_gen(4, 2, lambda a, b: a ^ b, inverted=False)
        )
    ]


# ------------------------------------------------------------------------
class Part74145(PartDIP16):
    name = "74145"
    desc = "BCD to decimal decoders/drivers"
    pin_cfg = {
         1: Pin("0", Pin.OC),
         2: Pin("1", Pin.OC),
         3: Pin("2", Pin.OC),
         4: Pin("3", Pin.OC),
         5: Pin("4", Pin.OC),
         6: Pin("5", Pin.OC),
         7: Pin("6", Pin.OC),
         9: Pin("7", Pin.OC),
        10: Pin("8", Pin.OC),
        11: Pin("9", Pin.OC),
        12: Pin("D", Pin.IN),
        13: Pin("C", Pin.IN),
        14: Pin("B", Pin.IN),
        15: Pin("A", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[12, 13, 14, 15],
        outputs=[1, 2, 3, 4, 5, 6, 7, 9, 10, 11],
        ttype=Test.COMB,
        body=[
            [[0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0, 1, 0], [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]],
            [[0, 1, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]],
            [[0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]],
            [[0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 1, 1, 1]],
            [[0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 1]],
            [[1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]],
            [[1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]],
            [[1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part74148(PartDIP16):
    name = "74148"
    desc = "8-line to 3-line priority encoder"
    pin_cfg = {
         1: Pin("4", Pin.IN),
         2: Pin("5", Pin.IN),
         3: Pin("6", Pin.IN),
         4: Pin("7", Pin.IN),
         5: Pin("EI", Pin.IN),
         6: Pin("A2", Pin.OUT),
         7: Pin("A1", Pin.OUT),
         9: Pin("A0", Pin.OUT),
        10: Pin("0", Pin.IN),
        11: Pin("1", Pin.IN),
        12: Pin("2", Pin.IN),
        13: Pin("3", Pin.IN),
        14: Pin("GS", Pin.OUT),
        15: Pin("E0", Pin.OUT),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[5,  10, 11, 12, 13, 1, 2, 3, 4],
        outputs=[6, 7, 9, 14, 15],
        ttype=Test.COMB,
        body=[
            [[1,  0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1,  1, 1]],
            [[1,  1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1,  1, 1]],

            [[0,  1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1,  1, 0]],

            [[0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0,  0, 1]],
            [[0,  0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1,  0, 1]],
            [[0,  0, 0, 0, 0, 0, 0, 1, 1], [0, 1, 0,  0, 1]],
            [[0,  0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 1,  0, 1]],
            [[0,  0, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0,  0, 1]],
            [[0,  0, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1,  0, 1]],
            [[0,  0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0,  0, 1]],
            [[0,  0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1,  0, 1]],

            [[0,  1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0,  0, 1]],
            [[0,  1, 1, 1, 1, 1, 1, 0, 1], [0, 0, 1,  0, 1]],
            [[0,  1, 1, 1, 1, 1, 0, 1, 1], [0, 1, 0,  0, 1]],
            [[0,  1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1,  0, 1]],
            [[0,  1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 0,  0, 1]],
            [[0,  1, 1, 0, 1, 1, 1, 1, 1], [1, 0, 1,  0, 1]],
            [[0,  1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0,  0, 1]],
            [[0,  0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1,  0, 1]],

        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part74150(PartDIP24):
    name = "74150"
    desc = "Data selectors/multiplexers"
    pin_cfg = {
        1: Pin("E7", Pin.IN),
        2: Pin("E6", Pin.IN),
        3: Pin("E5", Pin.IN),
        4: Pin("E4", Pin.IN),
        5: Pin("E3", Pin.IN),
        6: Pin("E2", Pin.IN),
        7: Pin("E1", Pin.IN),
        8: Pin("E0", Pin.IN),
        9: Pin("~G", Pin.IN),
        10: Pin("W", Pin.OUT),
        11: Pin("D", Pin.IN),
        13: Pin("C", Pin.IN),
        14: Pin("B", Pin.IN),
        15: Pin("A", Pin.IN),
        16: Pin("E15", Pin.IN),
        17: Pin("E14", Pin.IN),
        18: Pin("E13", Pin.IN),
        19: Pin("E12", Pin.IN),
        20: Pin("E11", Pin.IN),
        21: Pin("E10", Pin.IN),
        22: Pin("E9", Pin.IN),
        23: Pin("E8", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[11, 13, 14, 15,  9,  8, 7, 6, 5, 4, 3, 2, 1, 23, 22, 21, 20, 19, 18, 17, 16],
        outputs=[10],
        ttype=Test.COMB,
        body=[
            [[0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1]],

            [[0, 0, 0, 0,  0,  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0]],
            [[0, 0, 0, 1,  0,  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0]],
            [[0, 0, 1, 0,  0,  0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0]],
            [[0, 0, 1, 1,  0,  0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0]],
            [[0, 1, 0, 0,  0,  0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0]],
            [[0, 1, 0, 1,  0,  0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0]],
            [[0, 1, 1, 0,  0,  0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0]],
            [[0, 1, 1, 1,  0,  0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0]],
            [[1, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0]],
            [[1, 0, 0, 1,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0]],
            [[1, 0, 1, 0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0]],
            [[1, 0, 1, 1,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0]],
            [[1, 1, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0]],
            [[1, 1, 0, 1,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0]],
            [[1, 1, 1, 0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0]],
            [[1, 1, 1, 1,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0]],

            [[0, 0, 0, 0,  0,  0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1]],
            [[0, 0, 0, 1,  0,  1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1]],
            [[0, 0, 1, 0,  0,  1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1]],
            [[0, 0, 1, 1,  0,  1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1]],
            [[0, 1, 0, 0,  0,  1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1]],
            [[0, 1, 0, 1,  0,  1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1]],
            [[0, 1, 1, 0,  0,  1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1]],
            [[0, 1, 1, 1,  0,  1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], [1]],
            [[1, 0, 0, 0,  0,  1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1], [1]],
            [[1, 0, 0, 1,  0,  1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], [1]],
            [[1, 0, 1, 0,  0,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1]],
            [[1, 0, 1, 1,  0,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1], [1]],
            [[1, 1, 0, 0,  0,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [1]],
            [[1, 1, 0, 1,  0,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], [1]],
            [[1, 1, 1, 0,  0,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [1]],
            [[1, 1, 1, 1,  0,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part74151(PartDIP16):
    name = "74151"
    desc = "Data selectors/multiplexers"
    pin_cfg = {
        1: Pin("D3", Pin.IN),
        2: Pin("D2", Pin.IN),
        3: Pin("D1", Pin.IN),
        4: Pin("D0", Pin.IN),
        5: Pin("Y", Pin.OUT),
        6: Pin("W", Pin.OUT),
        7: Pin("~G", Pin.IN),
        9: Pin("C", Pin.IN),
        10: Pin("B", Pin.IN),
        11: Pin("A", Pin.IN),
        12: Pin("D7", Pin.IN),
        13: Pin("D6", Pin.IN),
        14: Pin("D5", Pin.IN),
        15: Pin("D4", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[4, 3, 2, 1, 15, 14, 13, 12,  9, 10, 11,  7],
        outputs=[5, 6],
        ttype=Test.COMB,
        body=[
            [[1, 1, 1, 1, 1, 1, 1, 1,  0, 0, 0,  1], [0, 1]],
            [[1, 1, 1, 1, 1, 1, 1, 1,  0, 0, 1,  1], [0, 1]],
            [[1, 1, 1, 1, 1, 1, 1, 1,  0, 1, 0,  1], [0, 1]],
            [[1, 1, 1, 1, 1, 1, 1, 1,  0, 1, 1,  1], [0, 1]],
            [[1, 1, 1, 1, 1, 1, 1, 1,  1, 0, 0,  1], [0, 1]],
            [[1, 1, 1, 1, 1, 1, 1, 1,  1, 0, 1,  1], [0, 1]],
            [[1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 0,  1], [0, 1]],
            [[1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1,  1], [0, 1]],

            [[0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0,  1], [0, 1]],
            [[0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 1,  1], [0, 1]],
            [[0, 0, 0, 0, 0, 0, 0, 0,  0, 1, 0,  1], [0, 1]],
            [[0, 0, 0, 0, 0, 0, 0, 0,  0, 1, 1,  1], [0, 1]],
            [[0, 0, 0, 0, 0, 0, 0, 0,  1, 0, 0,  1], [0, 1]],
            [[0, 0, 0, 0, 0, 0, 0, 0,  1, 0, 1,  1], [0, 1]],
            [[0, 0, 0, 0, 0, 0, 0, 0,  1, 1, 0,  1], [0, 1]],
            [[0, 0, 0, 0, 0, 0, 0, 0,  1, 1, 1,  1], [0, 1]],

            [[1, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0,  0], [1, 0]],
            [[0, 1, 0, 0, 0, 0, 0, 0,  0, 0, 1,  0], [1, 0]],
            [[0, 0, 1, 0, 0, 0, 0, 0,  0, 1, 0,  0], [1, 0]],
            [[0, 0, 0, 1, 0, 0, 0, 0,  0, 1, 1,  0], [1, 0]],
            [[0, 0, 0, 0, 1, 0, 0, 0,  1, 0, 0,  0], [1, 0]],
            [[0, 0, 0, 0, 0, 1, 0, 0,  1, 0, 1,  0], [1, 0]],
            [[0, 0, 0, 0, 0, 0, 1, 0,  1, 1, 0,  0], [1, 0]],
            [[0, 0, 0, 0, 0, 0, 0, 1,  1, 1, 1,  0], [1, 0]],

            [[0, 1, 1, 1, 1, 1, 1, 1,  0, 0, 0,  0], [0, 1]],
            [[1, 0, 1, 1, 1, 1, 1, 1,  0, 0, 1,  0], [0, 1]],
            [[1, 1, 0, 1, 1, 1, 1, 1,  0, 1, 0,  0], [0, 1]],
            [[1, 1, 1, 0, 1, 1, 1, 1,  0, 1, 1,  0], [0, 1]],
            [[1, 1, 1, 1, 0, 1, 1, 1,  1, 0, 0,  0], [0, 1]],
            [[1, 1, 1, 1, 1, 0, 1, 1,  1, 0, 1,  0], [0, 1]],
            [[1, 1, 1, 1, 1, 1, 0, 1,  1, 1, 0,  0], [0, 1]],
            [[1, 1, 1, 1, 1, 1, 1, 0,  1, 1, 1,  0], [0, 1]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part74153(PartDIP16):
    name = "74153"
    desc = "Dual 4-line to 1-line data selectors/multiplexers"
    pin_cfg = {
        1: Pin("~1G", Pin.IN),
        2: Pin("B", Pin.IN),
        3: Pin("1C3", Pin.IN),
        4: Pin("1C2", Pin.IN),
        5: Pin("1C1", Pin.IN),
        6: Pin("1C0", Pin.IN),
        7: Pin("1Y", Pin.OUT),
        9: Pin("2Y", Pin.OUT),
        10: Pin("2C0", Pin.IN),
        11: Pin("2C1", Pin.IN),
        12: Pin("2C2", Pin.IN),
        13: Pin("2C3", Pin.IN),
        14: Pin("A", Pin.IN),
        15: Pin("~2G", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[2, 14, 1, 3, 4, 5, 6, 15, 13, 12, 11, 10],
        outputs=[7, 9],
        ttype=Test.COMB,
        body=[
            # output is always "0" when G is high
            [[0, 0,  1,  0, 0, 0, 0,  1,  0, 0, 0, 0], [0, 0]],
            [[0, 1,  1,  0, 0, 0, 0,  1,  0, 0, 0, 0], [0, 0]],
            [[1, 0,  1,  0, 0, 0, 0,  1,  0, 0, 0, 0], [0, 0]],
            [[1, 1,  1,  0, 0, 0, 0,  1,  0, 0, 0, 0], [0, 0]],
            [[0, 0,  1,  1, 1, 1, 1,  1,  1, 1, 1, 1], [0, 0]],
            [[0, 1,  1,  1, 1, 1, 1,  1,  1, 1, 1, 1], [0, 0]],
            [[1, 0,  1,  1, 1, 1, 1,  1,  1, 1, 1, 1], [0, 0]],
            [[1, 1,  1,  1, 1, 1, 1,  1,  1, 1, 1, 1], [0, 0]],

            # selection if G is low
            [[0, 0,  0,  1, 1, 1, 0,  0,  1, 1, 1, 0], [0, 0]],
            [[0, 1,  0,  1, 1, 0, 1,  0,  1, 1, 0, 1], [0, 0]],
            [[1, 0,  0,  1, 0, 1, 1,  0,  1, 0, 1, 1], [0, 0]],
            [[1, 1,  0,  0, 1, 1, 1,  0,  0, 1, 1, 1], [0, 0]],

            [[0, 0,  0,  0, 0, 0, 1,  0,  0, 0, 0, 1], [1, 1]],
            [[0, 1,  0,  0, 0, 1, 0,  0,  0, 0, 1, 0], [1, 1]],
            [[1, 0,  0,  0, 1, 0, 0,  0,  0, 1, 0, 0], [1, 1]],
            [[1, 1,  0,  1, 0, 0, 0,  0,  1, 0, 0, 0], [1, 1]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part74154(PartDIP24):
    name = "74154"
    desc = "4-Line-to-16-Line Decoders/Demultiplexers"
    pin_cfg = {
        1: Pin("O0", Pin.OUT),
        2: Pin("O1", Pin.OUT),
        3: Pin("O2", Pin.OUT),
        4: Pin("O3", Pin.OUT),
        5: Pin("O4", Pin.OUT),
        6: Pin("O5", Pin.OUT),
        7: Pin("O6", Pin.OUT),
        8: Pin("O7", Pin.OUT),
        9: Pin("O8", Pin.OUT),
        10: Pin("O9", Pin.OUT),
        11: Pin("O10", Pin.OUT),
        13: Pin("O11", Pin.OUT),
        14: Pin("O12", Pin.OUT),
        15: Pin("O13", Pin.OUT),
        16: Pin("O14", Pin.OUT),
        17: Pin("O15", Pin.OUT),
        18: Pin("G1", Pin.IN),
        19: Pin("G2", Pin.IN),
        20: Pin("D", Pin.IN),
        21: Pin("C", Pin.IN),
        22: Pin("B", Pin.IN),
        23: Pin("A", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[18, 19, 20, 21, 22, 23],
        outputs=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17],
        ttype=Test.COMB,
        body=[
            # output is always "1" when any G input is high
            [[0, 1,  0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 0,  0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1,  0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 1,  1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 0,  1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1,  1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

            # selection
            [[0, 0,  0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0,  0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0,  0, 0, 1, 0], [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0,  0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0,  0, 1, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0,  0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0,  0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0,  0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0,  1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0,  1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]],
            [[0, 0,  1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]],
            [[0, 0,  1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]],
            [[0, 0,  1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]],
            [[0, 0,  1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]],
            [[0, 0,  1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]],
            [[0, 0,  1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part74155(PartDIP16):
    name = "74155"
    desc = "Dual 2-line to 4-line decoders/demultiplexers"
    pin_cfg = {
        1: Pin("1C", Pin.IN),
        2: Pin("~1G", Pin.IN),
        3: Pin("B", Pin.IN),
        4: Pin("1Y3", Pin.OUT),
        5: Pin("1Y2", Pin.OUT),
        6: Pin("1Y1", Pin.OUT),
        7: Pin("1Y0", Pin.OUT),
        9: Pin("2Y0", Pin.OUT),
        10: Pin("2Y1", Pin.OUT),
        11: Pin("2Y2", Pin.OUT),
        12: Pin("2Y3", Pin.OUT),
        13: Pin("A", Pin.IN),
        14: Pin("~2G", Pin.IN),
        15: Pin("~2C", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[3, 13,  2, 1,  14, 15],
        outputs=[7, 8, 5, 4,  9, 10, 11, 12],
        ttype=Test.COMB,
        body=[
            # ~G = 1, any 1C/~2C, any A/B
            [[0, 0,  1, 0,  1, 0], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[0, 1,  1, 0,  1, 0], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[1, 0,  1, 0,  1, 0], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[1, 1,  1, 0,  1, 0], [1, 1, 1, 1,  1, 1, 1, 1]],

            [[0, 0,  1, 1,  1, 1], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[0, 1,  1, 1,  1, 1], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[1, 0,  1, 1,  1, 1], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[1, 1,  1, 1,  1, 1], [1, 1, 1, 1,  1, 1, 1, 1]],
            # 1C/~2C = 0/1, any ~G, any A/B
            [[0, 0,  0, 0,  0, 1], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[0, 1,  0, 0,  0, 1], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[1, 0,  0, 0,  0, 1], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[1, 1,  0, 0,  0, 1], [1, 1, 1, 1,  1, 1, 1, 1]],

            [[0, 0,  1, 0,  1, 1], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[0, 1,  1, 0,  1, 1], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[1, 0,  1, 0,  1, 1], [1, 1, 1, 1,  1, 1, 1, 1]],
            [[1, 1,  1, 0,  1, 1], [1, 1, 1, 1,  1, 1, 1, 1]],

            # selections
            [[0, 0,  0, 1,  0, 0], [0, 1, 1, 1,  0, 1, 1, 1]],
            [[0, 1,  0, 1,  0, 0], [1, 0, 1, 1,  1, 0, 1, 1]],
            [[1, 0,  0, 1,  0, 0], [1, 1, 0, 1,  1, 1, 0, 1]],
            [[1, 1,  0, 1,  0, 0], [1, 1, 1, 0,  1, 1, 1, 0]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part74156(Part74155):
    name = "74156"
    desc = "Dual 2-line to 4-line decoders/demultiplexers"
    pin_cfg = {
        1: Pin("1C", Pin.IN),
        2: Pin("~1G", Pin.IN),
        3: Pin("B", Pin.IN),
        4: Pin("1Y3", Pin.OC),
        5: Pin("1Y2", Pin.OC),
        6: Pin("1Y1", Pin.OC),
        7: Pin("1Y0", Pin.OC),
        9: Pin("2Y0", Pin.OC),
        10: Pin("2Y1", Pin.OC),
        11: Pin("2Y2", Pin.OC),
        12: Pin("2Y3", Pin.OC),
        13: Pin("A", Pin.IN),
        14: Pin("~2G", Pin.IN),
        15: Pin("~2C", Pin.IN),
    }


# ------------------------------------------------------------------------
class Part74157(PartDIP16):
    name = "74157"
    desc = "Quad 2-line to 1-line data selectors/multiplexers"
    pin_cfg = {
        1: Pin("S", Pin.IN),
        2: Pin("A1", Pin.IN),
        3: Pin("B1", Pin.IN),
        4: Pin("Y1", Pin.OUT),
        5: Pin("A2", Pin.IN),
        6: Pin("B2", Pin.IN),
        7: Pin("Y2", Pin.OUT),
        9: Pin("Y3", Pin.OUT),
        10: Pin("B3", Pin.IN),
        11: Pin("A3", Pin.IN),
        12: Pin("Y4", Pin.OUT),
        13: Pin("B4", Pin.IN),
        14: Pin("A4", Pin.IN),
        15: Pin("G", Pin.IN),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[15, 1,  2, 3,  5, 6,  11, 10,  14, 13],
        outputs=[4, 7, 9, 12],
        ttype=Test.COMB,
        body=[
            [[1, 0,  1, 1,  1, 1,  1, 1,  1, 1], [0, 0, 0, 0]],
            [[1, 1,  1, 1,  1, 1,  1, 1,  1, 1], [0, 0, 0, 0]],
            [[1, 0,  0, 0,  0, 0,  0, 0,  0, 0], [0, 0, 0, 0]],
            [[1, 1,  0, 0,  0, 0,  0, 0,  0, 0], [0, 0, 0, 0]],

            [[0, 0,  0, 0,  0, 0,  0, 0,  0, 0], [0, 0, 0, 0]],
            [[0, 1,  0, 0,  0, 0,  0, 0,  0, 0], [0, 0, 0, 0]],
            [[0, 0,  0, 1,  0, 1,  0, 1,  0, 1], [0, 0, 0, 0]],
            [[0, 1,  0, 1,  0, 1,  0, 1,  0, 1], [1, 1, 1, 1]],
            [[0, 0,  1, 0,  1, 0,  1, 0,  1, 0], [1, 1, 1, 1]],
            [[0, 1,  1, 0,  1, 0,  1, 0,  1, 0], [0, 0, 0, 0]],
            [[0, 0,  1, 1,  1, 1,  1, 1,  1, 1], [1, 1, 1, 1]],
            [[0, 1,  1, 1,  1, 1,  1, 1,  1, 1], [1, 1, 1, 1]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
class Part74161(PartDIP16):
    name = "74161"
    desc = "Synchronous presettable 4-bit counter"
    pin_cfg = {
        1: Pin("~CLR", Pin.IN),
        2: Pin("CLK", Pin.IN),
        3: Pin("A", Pin.IN),
        4: Pin("B", Pin.IN),
        5: Pin("C", Pin.IN),
        6: Pin("D", Pin.IN),
        7: Pin("ENP", Pin.IN),
        9: Pin("~LOAD", Pin.IN),
        10: Pin("ENT", Pin.IN),
        11: Pin("QD", Pin.OUT),
        12: Pin("QC", Pin.OUT),
        13: Pin("QB", Pin.OUT),
        14: Pin("QA", Pin.OUT),
        15: Pin("RCO", Pin.OUT),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[1, 9, 2,  10, 7,  6, 5, 4, 3],
        outputs=[11, 12, 13, 14,  15],
        ttype=Test.SEQ,
        body=[
            # NOTE: "enable" transitions done on clock high,
            # some chips are more sensitive to that
            # initial clear
            [['-', 1,   1,  0, 0,  0, 0, 0, 0], [0, 0, 0, 0,  0]],
            [[  1, 1,   1,  0, 0,  0, 0, 0, 0], [0, 0, 0, 0,  0]],
            # loads
            [[  1, 0,   1,  0, 0,  0, 0, 0, 0], [0, 0, 0, 0,  0]],
            [[  1, 0, '+',  0, 0,  0, 0, 0, 1], [0, 0, 0, 1,  0]],
            [[  1, 0, '+',  0, 0,  0, 0, 1, 0], [0, 0, 1, 0,  0]],
            [[  1, 0, '+',  0, 0,  0, 0, 1, 1], [0, 0, 1, 1,  0]],
            [[  1, 0, '+',  0, 0,  0, 1, 0, 0], [0, 1, 0, 0,  0]],
            [[  1, 0, '+',  0, 0,  0, 1, 0, 1], [0, 1, 0, 1,  0]],
            [[  1, 0, '+',  0, 0,  0, 1, 1, 0], [0, 1, 1, 0,  0]],
            [[  1, 0, '+',  0, 0,  0, 1, 1, 1], [0, 1, 1, 1,  0]],
            [[  1, 0, '+',  0, 0,  1, 0, 0, 0], [1, 0, 0, 0,  0]],
            [[  1, 0, '+',  0, 0,  1, 0, 0, 1], [1, 0, 0, 1,  0]],
            [[  1, 0, '+',  0, 0,  1, 0, 1, 0], [1, 0, 1, 0,  0]],
            [[  1, 0, '+',  0, 0,  1, 0, 1, 1], [1, 0, 1, 1,  0]],
            [[  1, 0, '+',  0, 0,  1, 1, 0, 0], [1, 1, 0, 0,  0]],
            [[  1, 0, '+',  0, 0,  1, 1, 0, 1], [1, 1, 0, 1,  0]],
            [[  1, 0, '+',  0, 0,  1, 1, 1, 0], [1, 1, 1, 0,  0]],
            [[  1, 0, '+',  0, 0,  1, 1, 1, 1], [1, 1, 1, 1,  0]],
            # disable load, enable count
            [[  1, 1,   1,  1, 1,  0, 0, 0, 0], [1, 1, 1, 1,  1]],
            # count
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [0, 0, 0, 0,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [0, 0, 0, 1,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [0, 0, 1, 0,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [0, 0, 1, 1,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [0, 1, 0, 0,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [0, 1, 0, 1,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [0, 1, 1, 0,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [0, 1, 1, 1,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [1, 0, 0, 0,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [1, 0, 0, 1,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [1, 0, 1, 0,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [1, 0, 1, 1,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [1, 1, 0, 0,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [1, 1, 0, 1,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [1, 1, 1, 0,  0]],
            [[  1, 1, '+',  1, 1,  0, 0, 0, 0], [1, 1, 1, 1,  1]],
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


# ------------------------------------------------------------------------
class Part74164(PartDIP14):
    name = "74164"
    desc = "8-bit parallel-out serial shift register"
    pin_cfg = {
        1: Pin("A", Pin.IN),
        2: Pin("B", Pin.IN),
        3: Pin("QA", Pin.IN),
        4: Pin("QB", Pin.IN),
        5: Pin("QC", Pin.IN),
        6: Pin("QD", Pin.IN),
        8: Pin("CLK", Pin.IN),
        9: Pin("~CLR", Pin.IN),
        10: Pin("QE", Pin.IN),
        11: Pin("QF", Pin.OUT),
        12: Pin("QG", Pin.OUT),
        13: Pin("QH", Pin.OUT),
    }
    test_all = Test(
        name="Complete logic",
        inputs=[9, 8,  1, 2],
        outputs=[3, 4, 5, 6, 10, 11, 12, 13],
        ttype=Test.SEQ,
        body=[
            # clear
            [[0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
            # idle
            [[1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
            [[1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
            [[1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
            [[1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
            # shift in
            [[1, '+', 1, 1], [1, 0, 0, 0, 0, 0, 0, 0]],
            [[1, '+', 0, 1], [0, 1, 0, 0, 0, 0, 0, 0]],
            [[1, '+', 1, 0], [0, 0, 1, 0, 0, 0, 0, 0]],
            [[1, '+', 0, 0], [0, 0, 0, 1, 0, 0, 0, 0]],
            [[1, '+', 1, 1], [1, 0, 0, 0, 1, 0, 0, 0]],
            [[1, '+', 1, 1], [1, 1, 0, 0, 0, 1, 0, 0]],
            [[1, '+', 1, 1], [1, 1, 1, 0, 0, 0, 1, 0]],
            [[1, '+', 1, 1], [1, 1, 1, 1, 0, 0, 0, 1]],
            [[1, '+', 1, 1], [1, 1, 1, 1, 1, 0, 0, 0]],
            [[1, '+', 1, 1], [1, 1, 1, 1, 1, 1, 0, 0]],
            [[1, '+', 1, 1], [1, 1, 1, 1, 1, 1, 1, 0]],
            [[1, '+', 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
            # clear
            [[0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
        ]
    )
    tests = [test_all]


# ------------------------------------------------------------------------
#class Part74165(PartDIP16):
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


# ------------------------------------------------------------------------
class Part74170(PartDIP16):
    name = "74170"
    desc = "4-by-4 register file with open-collector outputs"
    pin_cfg = {
        1: Pin("D2", Pin.IN),
        2: Pin("D3", Pin.IN),
        3: Pin("D4", Pin.IN),
        4: Pin("RB", Pin.IN),
        5: Pin("RA", Pin.IN),
        6: Pin("Q4", Pin.OC),
        7: Pin("Q3", Pin.OC),
        9: Pin("Q2", Pin.OC),
        10: Pin("Q1", Pin.OC),
        11: Pin("~GR", Pin.IN),
        12: Pin("~GW", Pin.IN),
        13: Pin("WB", Pin.IN),
        14: Pin("WA", Pin.IN),
        15: Pin("D1", Pin.IN),
    }
    test_bits = Test(
        name="Bit storage test",
        inputs=[13, 14, 12,  4, 5, 11,  15, 1, 2, 3],
        outputs=[10, 9, 7, 6],
        ttype=Test.COMB,
        body=[
            # R/W 0's
            [[0, 0, 0,  0, 0, 1,  0, 0, 0, 0], [1, 1, 1, 1]],
            [[0, 0, 1,  0, 0, 0,  0, 0, 0, 0], [0, 0, 0, 0]],

            [[0, 1, 0,  0, 0, 1,  0, 0, 0, 0], [1, 1, 1, 1]],
            [[0, 0, 1,  0, 1, 0,  0, 0, 0, 0], [0, 0, 0, 0]],

            [[1, 0, 0,  0, 0, 1,  0, 0, 0, 0], [1, 1, 1, 1]],
            [[0, 0, 1,  1, 0, 0,  0, 0, 0, 0], [0, 0, 0, 0]],

            [[1, 1, 0,  0, 0, 1,  0, 0, 0, 0], [1, 1, 1, 1]],
            [[0, 0, 1,  1, 1, 0,  0, 0, 0, 0], [0, 0, 0, 0]],

            # R/W 1's
            [[0, 0, 0,  0, 0, 1,  1, 1, 1, 1], [1, 1, 1, 1]],
            [[0, 0, 1,  0, 0, 0,  0, 0, 0, 0], [1, 1, 1, 1]],

            [[0, 1, 0,  0, 0, 1,  1, 1, 1, 1], [1, 1, 1, 1]],
            [[0, 0, 1,  0, 1, 0,  0, 0, 0, 0], [1, 1, 1, 1]],

            [[1, 0, 0,  0, 0, 1,  1, 1, 1, 1], [1, 1, 1, 1]],
            [[0, 0, 1,  1, 0, 0,  0, 0, 0, 0], [1, 1, 1, 1]],

            [[1, 1, 0,  0, 0, 1,  1, 1, 1, 1], [1, 1, 1, 1]],
            [[0, 0, 1,  1, 1, 0,  0, 0, 0, 0], [1, 1, 1, 1]],
        ]
    )

    test_addr = Test(
        name="Addressing test",
        inputs=[13, 14, 12,  4, 5, 11,  15, 1, 2, 3],
        outputs=[10, 9, 7, 6],
        ttype=Test.COMB,
        body=[
            # W: 0 0 0 0
            [[0, 0, 0,  0, 0, 1,  0, 0, 0, 0], [1, 1, 1, 1]],
            [[0, 1, 0,  0, 0, 1,  0, 0, 0, 0], [1, 1, 1, 1]],
            [[1, 0, 0,  0, 0, 1,  0, 0, 0, 0], [1, 1, 1, 1]],
            [[1, 1, 0,  0, 0, 1,  0, 0, 0, 0], [1, 1, 1, 1]],
            # W: 1 2 4 8
            [[0, 0, 1,  0, 0, 1,  0, 0, 0, 1], [1, 1, 1, 1]],
            [[0, 0, 0,  0, 0, 1,  0, 0, 0, 1], [1, 1, 1, 1]],
            [[0, 1, 1,  0, 0, 1,  0, 0, 1, 0], [1, 1, 1, 1]],
            [[0, 1, 0,  0, 0, 1,  0, 0, 1, 0], [1, 1, 1, 1]],
            [[1, 0, 1,  0, 0, 1,  0, 1, 0, 0], [1, 1, 1, 1]],
            [[1, 0, 0,  0, 0, 1,  0, 1, 0, 0], [1, 1, 1, 1]],
            [[1, 1, 1,  0, 0, 1,  1, 0, 0, 0], [1, 1, 1, 1]],
            [[1, 1, 0,  0, 0, 1,  1, 0, 0, 0], [1, 1, 1, 1]],
            # R: 1 2 4 8
            [[0, 0, 1,  0, 0, 0,  0, 0, 0, 0], [0, 0, 0, 1]],
            [[0, 0, 1,  0, 1, 0,  0, 0, 0, 0], [0, 0, 1, 0]],
            [[0, 0, 1,  1, 0, 0,  0, 0, 0, 0], [0, 1, 0, 0]],
            [[0, 0, 1,  1, 1, 0,  0, 0, 0, 0], [1, 0, 0, 0]],
        ]
    )
    test_rw = Test(
        name="Simultaneous read/write",
        inputs=[13, 14, 12,  4, 5, 11,  15, 1, 2, 3],
        outputs=[10, 9, 7, 6],
        ttype=Test.COMB,
        body=[
            [[0, 0, 0,  0, 0, 1,  0, 0, 0, 1], [1, 1, 1, 1]],
            [[0, 0, 1,  0, 0, 0,  0, 0, 0, 0], [0, 0, 0, 1]],

            [[0, 1, 0,  0, 0, 0,  0, 0, 1, 0], [0, 0, 0, 1]],
            [[0, 1, 1,  0, 1, 0,  0, 0, 0, 0], [0, 0, 1, 0]],

            [[1, 0, 0,  0, 1, 0,  0, 1, 0, 0], [0, 0, 1, 0]],
            [[1, 0, 1,  1, 0, 0,  0, 0, 0, 0], [0, 1, 0, 0]],

            [[1, 1, 0,  1, 0, 0,  1, 0, 0, 0], [0, 1, 0, 0]],
            [[1, 1, 1,  1, 1, 0,  0, 0, 0, 0], [1, 0, 0, 0]],

            [[0, 0, 0,  1, 1, 0,  0, 0, 0, 1], [1, 0, 0, 0]],
            [[0, 0, 1,  0, 0, 0,  0, 0, 0, 0], [0, 0, 0, 1]],
        ]
    )

    tests = [test_bits, test_addr, test_rw]


# ------------------------------------------------------------------------
class Part74174(PartDIP16):
    name = "74174"
    desc = "Hex D-type filp-flops with clear"
    pin_cfg = {
        1: Pin("~CLR", Pin.IN),
        2: Pin("1Q", Pin.OUT),
        3: Pin("1D", Pin.IN),
        4: Pin("2D", Pin.IN),
        5: Pin("2Q", Pin.OUT),
        6: Pin("3D", Pin.IN),
        7: Pin("3Q", Pin.OUT),
        9: Pin("CLK", Pin.IN),
        10: Pin("4Q", Pin.OUT),
        11: Pin("4D", Pin.IN),
        12: Pin("5Q", Pin.OUT),
        13: Pin("5D", Pin.IN),
        14: Pin("6D", Pin.IN),
        15: Pin("6Q", Pin.OUT),
    }
    test_sync = Test(
        name="Synchronous operation",
        inputs=[1, 9,  3, 4, 6, 11, 13, 14],
        outputs=[2, 5, 7, 10, 12, 15],
        ttype=Test.SEQ,
        body=[
            [[1, '+',  0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
            [[1, '+',  1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]],
            [[1, '+',  0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
            [[1, '+',  1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]],
        ]
    )
    test_async = Test(
        name="Asynchronous operation",
        inputs=[1, 9,  3, 4, 6, 11, 13, 14],
        outputs=[2, 5, 7, 10, 12, 15],
        ttype=Test.COMB,
        body=[
            # clear
            [[0, 0,  1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]],
            [[1, 0,  1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]],
            # load 1s
            [[1, 1,  1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]],
            [[1, 0,  1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]],
            # clear
            [[0, 0,  1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]],
            [[1, 0,  1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]],
        ]
    )
    tests = [test_sync, test_async]


# ------------------------------------------------------------------------
class Part74175(PartDIP16):
    name = "74175"
    desc = "Quad D-type filp-flops"
    pin_cfg = {
        1: Pin("~CLR", Pin.IN),
        2: Pin("1Q", Pin.OUT),
        3: Pin("~1Q", Pin.OUT),
        4: Pin("1D", Pin.IN),
        5: Pin("2D", Pin.IN),
        6: Pin("~2Q", Pin.OUT),
        7: Pin("2Q", Pin.OUT),
        9: Pin("CLK", Pin.IN),
        10: Pin("3Q", Pin.OUT),
        11: Pin("~3Q", Pin.OUT),
        12: Pin("3D", Pin.IN),
        13: Pin("4D", Pin.IN),
        14: Pin("~4Q", Pin.OUT),
        15: Pin("4Q", Pin.OUT),
    }
    test_sync = Test(
        name="Synchronous operation",
        inputs=[1, 9,  4, 5, 12, 13],
        outputs=[2, 3,  7, 6,  10, 11,  15, 14],
        ttype=Test.SEQ,
        body=[
            [[1, '+',  0, 0, 0, 0], [0, 1,  0, 1,  0, 1,  0, 1]],
            [[1, '+',  1, 1, 1, 1], [1, 0,  1, 0,  1, 0,  1, 0]],
            [[1, '+',  0, 0, 0, 0], [0, 1,  0, 1,  0, 1,  0, 1]],
            [[1, '+',  1, 1, 1, 1], [1, 0,  1, 0,  1, 0,  1, 0]],
        ]
    )
    test_async = Test(
        name="Asynchronous operation",
        inputs=[1, 9,  4, 5, 12, 13],
        outputs=[2, 3,  7, 6,  10, 11,  15, 14],
        ttype=Test.COMB,
        body=[
            # clear
            [[0, 0,  1, 1, 1, 1], [0, 1,  0, 1,  0, 1,  0, 1]],
            [[1, 0,  1, 1, 1, 1], [0, 1,  0, 1,  0, 1,  0, 1]],
            # load 1s
            [[1, 1,  1, 1, 1, 1], [1, 0,  1, 0,  1, 0,  1, 0]],
            [[1, 0,  1, 1, 1, 1], [1, 0,  1, 0,  1, 0,  1, 0]],
            # clear
            [[0, 0,  1, 1, 1, 1], [0, 1,  0, 1,  0, 1,  0, 1]],
            [[1, 0,  1, 1, 1, 1], [0, 1,  0, 1,  0, 1,  0, 1]],
        ]
    )
    tests = [test_sync, test_async]


# ------------------------------------------------------------------------
class Part74180(PartDIP14):
    name = "74180"
    desc = "9-bit odd/even parity generator/checker"
    pin_cfg = {
        1: Pin("G", Pin.IN),
        2: Pin("H", Pin.IN),
        3: Pin("EVEN", Pin.IN),
        4: Pin("ODD", Pin.IN),
        5: Pin("sumEVEN", Pin.OUT),
        6: Pin("sumODD", Pin.OUT),
        8: Pin("A", Pin.IN),
        9: Pin("B", Pin.IN),
        10: Pin("C", Pin.IN),
        11: Pin("D", Pin.IN),
        12: Pin("E", Pin.IN),
        13: Pin("F", Pin.IN),
    }

    # ------------------------------------------------------------------------
    def parity_test_gen():
        # ------------------------------------------------------------------------
        def parity_check(v):
            if v[8] == v[9]:
                return [int(not v[8]), int(not v[8])]
            else:
                odd = reduce(lambda a, b: a^b, v[0:8] + [v[9]])
                return [int(not odd), odd]

        data = [Test.bin2vec(v, 10) for v in range(0, 2**10 - 1)]

        body = [
            [v, parity_check(v)] for v in data
        ]

        return Test(
            name="Asynchronous operation",
            inputs=[8, 9, 10, 11, 12, 13, 1, 2,  3, 4],
            outputs=[5, 6],
            ttype=Test.COMB,
            loops=64,
            body=body
        )

    tests = [parity_test_gen()]


# ------------------------------------------------------------------------
class Part74181(PartDIP24):
    name = "74181"
    desc = "Arithmetic logic units/function generators"
    pin_cfg = {
        1: Pin("B0", Pin.IN),
        2: Pin("A0", Pin.IN),
        3: Pin("S3", Pin.IN),
        4: Pin("S2", Pin.IN),
        5: Pin("S1", Pin.IN),
        6: Pin("S0", Pin.IN),
        7: Pin("~Cn", Pin.IN),
        8: Pin("M", Pin.IN),
        9: Pin("F0", Pin.OUT),
        10: Pin("F1", Pin.OUT),
        11: Pin("F2", Pin.OUT),
        13: Pin("F3", Pin.OUT),
        14: Pin("A=B", Pin.OC),
        15: Pin("X", Pin.OUT),
        16: Pin("~Cn+4", Pin.OUT),
        17: Pin("Y", Pin.OUT),
        18: Pin("B3", Pin.IN),
        19: Pin("A3", Pin.IN),
        20: Pin("B2", Pin.IN),
        21: Pin("A2", Pin.IN),
        22: Pin("B1", Pin.IN),
        23: Pin("A1", Pin.IN),
    }

    # ------------------------------------------------------------------------
    def logic_test_gen(s, name, fun):
        Vector = namedtuple('Vector', ['a', 'b', 'f'])

        # raw, numerical test data
        data = [
            Vector(a, b, fun(a, b))
            for a in range(0, 16)
            for b in range(0, 16)
        ]

        # test vectors in [[inputs], [outputs]] order:
        # [[1, s3, s2, s1, s0,  a3, a2, a1, a1,  b3, b2, b1, b0], [f3, f2, f1, f0]]
        body = [
            [[1] + Test.bin2vec(s, 4) + Test.bin2vec(v.a, 4) + Test.bin2vec(v.b, 4), Test.bin2vec(v.f, 4) + [v.f & 0b1111 == 0b1111]]
            for v in data
        ]

        return Test(
            name=name,
            inputs=[8,  3, 4, 5, 6,  19, 21, 23, 2,  18, 20, 22, 1],
            outputs=[13, 11, 10, 9, 14],
            ttype=Test.COMB,
            loops=32,
            body=body,
        )

    # ------------------------------------------------------------------------
    def arith_test_gen(s, name, fun):
        Vector = namedtuple('Vector', ['a', 'b', 'c', 'f'])

        # raw, numerical test data
        data = [
            Vector(a, b, c, fun(a, b) + (not c))
            for a in range(0, 16)
            for b in range(0, 16)
            for c in range(0, 2)
        ]

        # test vectors in [[inputs], [outputs]] order:
        # [[0, s3, s2, s1, s0,  cin,  a3, a2, a1, a1,  b3, b2, b1, b0], [f3, f2, f1, f0,  cout]]
        body = [
            [
                [0] + Test.bin2vec(s, 4) + [v.c] + Test.bin2vec(v.a, 4) + Test.bin2vec(v.b, 4),
                Test.bin2vec(v.f & 0b1111, 4) + [not v.f & 0b10000] + [v.f & 0b1111 == 0b1111]
            ]
            for v in data
        ]
        return Test(
            name=name,
            inputs=[8,  3, 4, 5, 6,  7,  19, 21, 23, 2,  18, 20, 22, 1],
            outputs=[13, 11, 10, 9, 16, 14],
            ttype=Test.COMB,
            loops=32,
            body=body
        )
    missing = "outputs G, P are not tested"
    tests = [
        logic_test_gen(0, "Logic: F = ~A", lambda a, b: ~a),
        logic_test_gen(1, "Logic: F = ~(A|B)", lambda a, b: ~(a | b)),
        logic_test_gen(2, "Logic: F = ~A&B", lambda a, b: ~a & b),
        logic_test_gen(3, "Logic: F = 0", lambda a, b: 0),
        logic_test_gen(4, "Logic: F = ~(A&B)", lambda a, b: ~(a & b)),
        logic_test_gen(5, "Logic: F = ~B", lambda a, b: ~b),
        logic_test_gen(6, "Logic: F = A^B", lambda a, b: a ^ b),
        logic_test_gen(7, "Logic: F = A&~B", lambda a, b: a & ~b),
        logic_test_gen(8, "Logic: F = ~A|B", lambda a, b: ~a | b),
        logic_test_gen(9, "Logic: F = ~(A^B)", lambda a, b: ~(a ^ b)),
        logic_test_gen(10, "Logic: F = B", lambda a, b: b),
        logic_test_gen(11, "Logic: F = A&B", lambda a, b: a & b),
        logic_test_gen(12, "Logic: F = 1", lambda a, b: 0xf),
        logic_test_gen(13, "Logic: F = A|~B", lambda a, b: a | ~b),
        logic_test_gen(14, "Logic: F = A|B", lambda a, b: a | b),
        logic_test_gen(15, "Logic: F = A", lambda a, b: a),
        arith_test_gen(0, "Arithmetic: F = A", lambda a, b: a),
        arith_test_gen(1, "Arithmetic: F = A|B", lambda a, b: a | b),
        arith_test_gen(2, "Arithmetic: F = A|~B", lambda a, b: a | (~b & 15)),
        arith_test_gen(3, "Arithmetic: F = -1", lambda a, b: 15),
        arith_test_gen(4, "Arithmetic: F = A+(A&~B)", lambda a, b: a + (a & (~b & 15))),
        arith_test_gen(5, "Arithmetic: F = (A|B)+(A&~B)", lambda a, b: (a | b) + (a & (~b & 15))),
        arith_test_gen(6, "Arithmetic: F = A-B-1", lambda a, b: (a - b) + 15),
        arith_test_gen(7, "Arithmetic: F = A&~B-1", lambda a, b: (a & (~b & 15)) + 15),
        arith_test_gen(8, "Arithmetic: F = A+(A&B)", lambda a, b: a + (a & b)),
        arith_test_gen(9, "Arithmetic: F = A+B", lambda a, b: a + b),
        arith_test_gen(10, "Arithmetic: F = (A|~B)+(A&B)", lambda a, b: (a | (~b & 15)) + (a & b)),
        arith_test_gen(11, "Arithmetic: F = (A&B)-1", lambda a, b: (a & b) + 15),
        arith_test_gen(12, "Arithmetic: F = A+A", lambda a, b: a + a),
        arith_test_gen(13, "Arithmetic: F = (A|B)+A", lambda a, b: (a | b) + a),
        arith_test_gen(14, "Arithmetic: F = (A|~B)+A", lambda a, b: (a | (~b & 15)) + a),
        arith_test_gen(15, "Arithmetic: F = A-1", lambda a, b: a + 15),
        # TODO: G, P (X, Y)
    ]


# ------------------------------------------------------------------------
class Part74182(PartDIP16):
    name = "74182"
    desc = "Look-ahead carry generator"
    pin_cfg = {
        1: Pin("~G1", Pin.IN),
        2: Pin("~P1", Pin.IN),
        3: Pin("~G0", Pin.IN),
        4: Pin("~P0", Pin.IN),
        5: Pin("~G3", Pin.IN),
        6: Pin("~P3", Pin.IN),
        7: Pin("~P", Pin.OUT),
        9: Pin("Cn+z", Pin.OUT),
        10: Pin("~G", Pin.OUT),
        11: Pin("Cn+y", Pin.OUT),
        12: Pin("Cn+x", Pin.OUT),
        13: Pin("Cn", Pin.IN),
        14: Pin("~G2", Pin.IN),
        15: Pin("~P2", Pin.IN),
    }
    test_g = Test(
        name="~G",
        inputs=[5, 14, 1, 3, 6, 15, 2],
        outputs=[10],
        ttype=Test.SEQ,
        loops=64,
        body=[
            [
                v, [0] if not v[0]
                or (not v[1] and not v[4])
                or (not v[2] and v[4:6] == [0, 0])
                or v[3:] == [0, 0, 0, 0]
                else [1]
            ]
            for v in Test.binary_combinator(7)
        ]
    )
    test_p = Test(
        name="~P",
        inputs=[2, 4, 6, 15],
        outputs=[7],
        ttype=Test.SEQ,
        loops=64,
        body=[
            [v, [0] if v == [0, 0, 0, 0] else [1]]
            for v in Test.binary_combinator(4)
        ]
    )
    test_cnx = Test(
        name="Cn+x",
        inputs=[3, 4, 13],
        outputs=[12],
        ttype=Test.SEQ,
        loops=64,
        body=[
            [v, [1] if not v[0] or v[1:3] == [0, 1] else [0]]
            for v in Test.binary_combinator(3)
        ]
    )
    test_cny = Test(
        name="Cn+y",
        inputs=[1, 3, 2, 4, 13],
        outputs=[11],
        ttype=Test.SEQ,
        loops=64,
        body=[
            [v, [1] if not v[0] or v[1:3] == [0, 0] or v[2:5] == [0, 0, 1] else [0]]
            for v in Test.binary_combinator(5)
        ]
    )
    test_cnz = Test(
        name="Cn+z",
        inputs=[14, 1, 3, 15, 2, 4, 13],
        outputs=[9],
        ttype=Test.SEQ,
        loops=64,
        body=[
            [v, [1] if not v[0] or (not v[1] and not v[3]) or v[2:5] == [0, 0, 0] or v[3:] == [0, 0, 0, 1] else [0]]
            for v in Test.binary_combinator(7)
        ]
    )

    tests = [test_g, test_p, test_cnx, test_cny, test_cnz]


# ------------------------------------------------------------------------
class Part74194(PartDIP16):
    name = "74194"
    desc = "4-bit bidirectional universal shift register"
    pin_cfg = {
        1: Pin("~CLR", Pin.IN),
        2: Pin("SR SER", Pin.IN),
        3: Pin("A", Pin.IN),
        4: Pin("B", Pin.IN),
        5: Pin("C", Pin.IN),
        6: Pin("D", Pin.IN),
        7: Pin("SL SER", Pin.IN),
        9: Pin("S0", Pin.IN),
        10: Pin("S1", Pin.IN),
        11: Pin("CLK", Pin.IN),
        12: Pin("QD", Pin.OUT),
        13: Pin("QC", Pin.OUT),
        14: Pin("QB", Pin.OUT),
        15: Pin("QA", Pin.OUT),
    }

    test_load = Test(
        name="Load",
        inputs=[1,  10, 9,  11,  7, 2,  3, 4, 5, 6],
        outputs=[15, 14, 13, 12],
        ttype=Test.SEQ,
        body=[
            # load 1's
            [[1,  1, 1,  '+',  0, 0,  1, 1, 1, 1], [1, 1, 1, 1]],
            # output current
            [[1,  0, 0,  '+',  0, 0,  0, 0, 0, 0], [1, 1, 1, 1]],
            # load 0's
            [[1,  1, 1,  '+',  1, 1,  0, 0, 0, 0], [0, 0, 0, 0]],
            # output current
            [[1,  0, 0,  '+',  1, 1,  1, 1, 1, 1], [0, 0, 0, 0]],

        ]
    )
    test_shright = Test(
        name="Shift right",
        inputs=[1,  10, 9,  11,  7, 2,  3, 4, 5, 6],
        outputs=[15, 14, 13, 12],
        ttype=Test.SEQ,
        body=[
            # shift right, insert 1's
            [[1,  0, 1,  '+',  0, 1,  0, 0, 0, 0], [1, 0, 0, 0]],
            [[1,  0, 1,  '+',  0, 1,  0, 0, 0, 0], [1, 1, 0, 0]],
            [[1,  0, 1,  '+',  0, 1,  0, 0, 0, 0], [1, 1, 1, 0]],
            [[1,  0, 1,  '+',  0, 1,  0, 0, 0, 0], [1, 1, 1, 1]],
            # shift right, insert 0's
            [[1,  0, 1,  '+',  1, 0,  1, 1, 1, 1], [0, 1, 1, 1]],
            [[1,  0, 1,  '+',  1, 0,  1, 1, 1, 1], [0, 0, 1, 1]],
            [[1,  0, 1,  '+',  1, 0,  1, 1, 1, 1], [0, 0, 0, 1]],
            [[1,  0, 1,  '+',  1, 0,  1, 1, 1, 1], [0, 0, 0, 0]],
        ]
    )
    test_shleft = Test(
        name="Shift left",
        inputs=[1,  10, 9,  11,  7, 2,  3, 4, 5, 6],
        outputs=[15, 14, 13, 12],
        ttype=Test.SEQ,
        body=[
            # shift left, insert 1's
            [[1,  1, 0,  '+',  1, 0,  0, 0, 0, 0], [0, 0, 0, 1]],
            [[1,  1, 0,  '+',  1, 0,  0, 0, 0, 0], [0, 0, 1, 1]],
            [[1,  1, 0,  '+',  1, 0,  0, 0, 0, 0], [0, 1, 1, 1]],
            [[1,  1, 0,  '+',  1, 0,  0, 0, 0, 0], [1, 1, 1, 1]],
            # shift left, insert 0's
            [[1,  1, 0,  '+',  0, 1,  1, 1, 1, 1], [1, 1, 1, 0]],
            [[1,  1, 0,  '+',  0, 1,  1, 1, 1, 1], [1, 1, 0, 0]],
            [[1,  1, 0,  '+',  0, 1,  1, 1, 1, 1], [1, 0, 0, 0]],
            [[1,  1, 0,  '+',  0, 1,  1, 1, 1, 1], [0, 0, 0, 0]],

        ]
    )
    test_clear = Test(
        name="Clear",
        inputs=[1,  10, 9,  11,  7, 2,  3, 4, 5, 6],
        outputs=[15, 14, 13, 12],
        ttype=Test.SEQ,
        body=[
            # load 1's
            [[1,  1, 1,  '+',  0, 0,  1, 1, 1, 1], [1, 1, 1, 1]],
            # clear
            [[0,  1, 1,  '+',  1, 1,  1, 1, 1, 1], [0, 0, 0, 0]],
        ]
    )

    tests = [test_load, test_shright, test_shleft, test_clear]


# ------------------------------------------------------------------------
class Part74198(PartDIP24):
    name = "74198"
    desc = "8-bit shift registers"
    pin_cfg = {
        1: Pin("S0", Pin.IN),
        2: Pin("SR SER", Pin.IN),
        3: Pin("A", Pin.IN),
        4: Pin("QA", Pin.OUT),
        5: Pin("B", Pin.IN),
        6: Pin("QB", Pin.OUT),
        7: Pin("C", Pin.IN),
        8: Pin("QC", Pin.OUT),
        9: Pin("D", Pin.IN),
        10: Pin("QD", Pin.OUT),
        11: Pin("CLK", Pin.IN),
        13: Pin("~CLR", Pin.IN),
        14: Pin("QE", Pin.OUT),
        15: Pin("E", Pin.IN),
        16: Pin("QF", Pin.OUT),
        17: Pin("F", Pin.IN),
        18: Pin("QG", Pin.OUT),
        19: Pin("G", Pin.IN),
        20: Pin("QH", Pin.OUT),
        21: Pin("H", Pin.IN),
        22: Pin("SL SER", Pin.IN),
        23: Pin("S1", Pin.IN),
    }

    test_load = Test(
        name="Parallel load",
        inputs=[13,  23, 1,  11,  22, 2,  3, 5, 7, 9, 15, 17, 19, 21],
        outputs=[4, 6, 8, 10, 14, 16, 18, 20],
        ttype=Test.SEQ,
        body=[
            [[1,  1, 1,  '+',  0, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
            [[1,  1, 1,  '+',  0, 0,  1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
        ]
    )
    test_clear = Test(
        name="Clear",
        inputs=[13,  23, 1,  11,  22, 2,  3, 5, 7, 9, 15, 17, 19, 21],
        outputs=[4, 6, 8, 10, 14, 16, 18, 20],
        ttype=Test.SEQ,
        body=[
            # load 1s
            [[1,  1, 1,  '+',  0, 0,  1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
            # clear
            [['-',  1, 1,  0,  0, 0,  1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
        ]
    )
    test_rshift = Test(
        name="Shift right",
        inputs=[13,  23, 1,  11,  22, 2,  3, 5, 7, 9, 15, 17, 19, 21],
        outputs=[4, 6, 8, 10, 14, 16, 18, 20],
        ttype=Test.SEQ,
        body=[
            # clear
            [['0',  1, 1,  0,  0, 0,  1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
            # rshift
            [[1,  0, 1,  '+',  0, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
            [[1,  0, 1,  '+',  0, 1,  0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]],
            [[1,  0, 1,  '+',  0, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0]],
            [[1,  0, 1,  '+',  0, 1,  0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0]],
            [[1,  0, 1,  '+',  0, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0]],
            [[1,  0, 1,  '+',  0, 1,  0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0]],
            [[1,  0, 1,  '+',  0, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 0]],
            [[1,  0, 1,  '+',  0, 1,  0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0]],
            [[1,  0, 1,  '+',  0, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1]],
        ]
    )
    test_lshift = Test(
        name="Shift left",
        inputs=[13,  23, 1,  11,  22, 2,  3, 5, 7, 9, 15, 17, 19, 21],
        outputs=[4, 6, 8, 10, 14, 16, 18, 20],
        ttype=Test.SEQ,
        body=[
            # clear
            [['-',  1, 1,  0,  0, 0,  1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
            # lshift
            [[1,  1, 0,  '+',  0, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
            [[1,  1, 0,  '+',  1, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1]],
            [[1,  1, 0,  '+',  0, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0]],
            [[1,  1, 0,  '+',  1, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1]],
            [[1,  1, 0,  '+',  0, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0]],
            [[1,  1, 0,  '+',  1, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1]],
            [[1,  1, 0,  '+',  0, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0]],
            [[1,  1, 0,  '+',  1, 0,  0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1]],
            [[1,  1, 0,  '+',  0, 0,  0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0]],
        ]
    )
    test_clk_inhibit = Test(
        name="Clock inhibit",
        inputs=[13,  23, 1,  11,  22, 2,  3, 5, 7, 9, 15, 17, 19, 21],
        outputs=[4, 6, 8, 10, 14, 16, 18, 20],
        ttype=Test.SEQ,
        body=[
            # clear
            [['-',  1, 1,  0,  0, 0,  1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
            # clock inhibit
            [[1,  0, 0,  '+',  1, 1,  1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
            # load 1s
            [[1,  1, 1,  '+',  0, 0,  1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
            # clock inhibit
            [[1,  0, 0,  '+',  1, 1,  0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]],
        ]
    )

    tests = [test_load, test_clear, test_rshift, test_lshift, test_clk_inhibit]


# ------------------------------------------------------------------------
class Part74S405(PartDIP16):
    name = "74S405"
    desc = "1-from-8 binary decoder"
    pin_cfg = {
        1: Pin("A0", Pin.IN),
        2: Pin("A1", Pin.IN),
        3: Pin("A2", Pin.IN),
        4: Pin("~E1", Pin.IN),
        5: Pin("~E2", Pin.IN),
        6: Pin("E3", Pin.IN),
        7: Pin("O7", Pin.OUT),
        9: Pin("O6", Pin.OUT),
        10: Pin("O5", Pin.OUT),
        11: Pin("O4", Pin.OUT),
        12: Pin("O3", Pin.OUT),
        13: Pin("O2", Pin.OUT),
        14: Pin("O1", Pin.OUT),
        15: Pin("O0", Pin.OUT),
    }

    test_select = Test(
        name="Select",
        inputs=[4, 5, 6,  3, 2, 1],
        outputs=[15, 14, 13, 12, 11, 10, 9, 7],
        ttype=Test.SEQ,
        body=[
            [[0, 0, 1,  0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 0, 1,  0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1]],
            [[0, 0, 1,  0, 1, 0], [1, 1, 0, 1, 1, 1, 1, 1]],
            [[0, 0, 1,  0, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1]],
            [[0, 0, 1,  1, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1]],
            [[0, 0, 1,  1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1]],
            [[0, 0, 1,  1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 1]],
            [[0, 0, 1,  1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0]],
        ]
    )
    test_inhibit = Test(
        name="Inhibit",
        inputs=[4, 5, 6,  3, 2, 1],
        outputs=[15, 14, 13, 12, 11, 10, 9, 7],
        ttype=Test.SEQ,
        body=[
            [[0, 0, 0,  0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 1, 0,  0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]],
            [[0, 1, 1,  0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 0, 0,  0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 0, 1,  0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1, 0,  0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 1, 1,  0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]],
        ]
    )

    tests = [test_select, test_inhibit]


# ------------------------------------------------------------------------
class Part4164(PartDIP16_rotated):
    TEST_BIT_ALL_0 = 0
    TEST_BIT_ALL_1 = 1
    TEST_ROW_ALL_0 = 2
    TEST_ROW_ALL_1 = 3
    TEST_ROW_ALTERNATE_01 = 4
    TEST_ROW_ALTERNATE_10 = 5

    name = "4164"
    desc = "(also HM4864, ...) (REVERSE CHIP ORIENTATION!) 65536 x 1bit DRAM memory"
    pin_cfg = {
        1: Pin("NC", Pin.NC),
        2: Pin("Din", Pin.IN),
        3: Pin("~WE", Pin.IN),
        4: Pin("~RAS", Pin.IN),
        5: Pin("A0", Pin.IN),
        6: Pin("A2", Pin.IN),
        7: Pin("A1", Pin.IN),
        9: Pin("A7", Pin.IN),
        10: Pin("A5", Pin.IN),
        11: Pin("A4", Pin.IN),
        12: Pin("A3", Pin.IN),
        13: Pin("A6", Pin.IN),
        14: Pin("Dout", Pin.OUT),
        15: Pin("~CAS", Pin.IN),
    }
    test_bit_all_0 = Test(
        name="Single bit: all 0s",
        inputs=[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15],
        outputs=[14],
        ttype=Test.MEM,
        tsubtype=TEST_BIT_ALL_0,
        loops=1,
    )
    test_bit_all_1 = Test(
        name="Single bit: all 1s",
        inputs=[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15],
        outputs=[14],
        ttype=Test.MEM,
        tsubtype=TEST_BIT_ALL_1,
        loops=1,
    )
    test_row_all_0 = Test(
        name="Page mode: all 0s",
        inputs=[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15],
        outputs=[14],
        ttype=Test.MEM,
        tsubtype=TEST_ROW_ALL_0,
        loops=1,
    )
    test_row_all_1 = Test(
        name="Page mode: all 1s",
        inputs=[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15],
        outputs=[14],
        ttype=Test.MEM,
        tsubtype=TEST_ROW_ALL_1,
        loops=1,
    )
    test_row_alternate_01 = Test(
        name="Page mode: alternating 0/1",
        inputs=[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15],
        outputs=[14],
        ttype=Test.MEM,
        tsubtype=TEST_ROW_ALTERNATE_01,
        loops=1,
    )
    test_row_alternate_10 = Test(
        name="Page mode: alternating 1/0",
        inputs=[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15],
        outputs=[14],
        ttype=Test.MEM,
        tsubtype=TEST_ROW_ALTERNATE_10,
        loops=1,
    )

    tests = [
        test_bit_all_0, test_bit_all_1,
        test_row_all_0, test_row_all_1,
        test_row_alternate_01, test_row_alternate_10
    ]


# ------------------------------------------------------------------------
# build parts catalog
catalog = {}
for i in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(i[1]) and 'tests' in [i[0] for i in inspect.getmembers(i[1])]:
        catalog[i[1].name] = i[1]
