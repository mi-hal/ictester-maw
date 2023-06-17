from prototypes import (PackageDIP16_rotated, Pin, Test)

class Part41256(PackageDIP16_rotated):
    SIZE_256 = 1 << 7
    MEM_TEST_MARCH_C_MINUS_RMW = SIZE_256 |0
    MEM_TEST_MARCH_C_MINUS_RW = SIZE_256 |1
    MEM_TEST_MARCH_C_MINUS_PAGE = SIZE_256 |2

    name = "41256"
    desc = "262144 x 1bit DRAM memory"
    pin_cfg = {
        1: Pin("A8", Pin.IN),
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

    default_inputs = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15]
    default_outputs = [14]

    tests = [
        Test("MARCH C- Read-Modify-Write mode", Test.MEM, default_inputs, default_outputs,
            tsubtype=MEM_TEST_MARCH_C_MINUS_RMW,
            loops=1,
        ),
        Test("MARCH C- Read+Write mode", Test.MEM, default_inputs, default_outputs,
            tsubtype=MEM_TEST_MARCH_C_MINUS_RW,
            loops=1,
        ),
        Test("MARCH C- Page access mode", Test.MEM, default_inputs, default_outputs,
            tsubtype=MEM_TEST_MARCH_C_MINUS_PAGE,
            loops=1,
        ),
    ]