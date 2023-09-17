import inspect
from enum import Enum
from binvec import BV

# ------------------------------------------------------------------------
def partimport(part_name):
    '''
    Since module names cannot start with a number... Nasty hack time!
    '''
    part_module = __import__(f'parts.{part_name}', fromlist=[f'Part{part_name}'])
    class_list = inspect.getmembers(part_module, lambda x: inspect.isclass(x) and x.__name__ == f'Part{part_name}')
    assert len(class_list) == 1
    return class_list[0][1]


# ------------------------------------------------------------------------
PinType = Enum("PinType", ["IN", "OUT", "BIDI", "OC", "ST3", "OE", "C", "RC", "VCC", "GND", "NC"])
ZIFFunc = Enum("ZIFFunc", names=[
        ("OUT", 1),
        ("IN_HIZ", 2),
        ("IN_PU_STRONG", 3),
        ("IN_PU_WEAK", 4),
        ("OUT_SINK", 5),
        ("C", 6),
        ("OUT_SOURCE", 7),
        ("VCC", 128),
        ("GND", 129),
    ]
)
TestType = Enum("TestType", names=[
        ("LOGIC", 1),
        ("DRAM", 2),
        ("UNIVIB", 3),
    ]
)


# ------------------------------------------------------------------------
class Pin:

    _pin_zif_allowed_funcs = {
        PinType.IN: [ZIFFunc.OUT],
        PinType.OUT: [ZIFFunc.IN_PU_WEAK, ZIFFunc.IN_PU_STRONG, ZIFFunc.IN_HIZ],
        PinType.BIDI: [ZIFFunc.OUT, ZIFFunc.IN_PU_WEAK, ZIFFunc.IN_PU_STRONG, ZIFFunc.IN_HIZ],
        PinType.OC: [ZIFFunc.IN_PU_STRONG, ZIFFunc.IN_PU_WEAK, ZIFFunc.IN_HIZ],
        PinType.ST3: [ZIFFunc.IN_PU_WEAK, ZIFFunc.IN_HIZ, ZIFFunc.IN_PU_STRONG],
        PinType.OE: [ZIFFunc.OUT_SINK],
        PinType.C: [ZIFFunc.C],
        PinType.RC: [ZIFFunc.IN_PU_STRONG],
        PinType.VCC: [ZIFFunc.VCC],
        PinType.GND: [ZIFFunc.GND],
        PinType.NC: [ZIFFunc.IN_HIZ],
    }

    _pin_zif_default_funcs = {
        PinType.IN: [ZIFFunc.OUT],
        PinType.OUT: [ZIFFunc.IN_PU_WEAK],
        PinType.BIDI: None,
        PinType.OC: [ZIFFunc.IN_PU_STRONG],
        PinType.ST3: [ZIFFunc.IN_PU_WEAK],
        PinType.OE: [ZIFFunc.OUT_SINK],
        PinType.C: [ZIFFunc.C],
        PinType.RC: [ZIFFunc.IN_PU_STRONG],
        PinType.VCC: [ZIFFunc.VCC],
        PinType.GND: [ZIFFunc.GND],
        PinType.NC: [ZIFFunc.IN_HIZ],
    }


    def __init__(self, name, role, zif_func=None):
        assert role in self._pin_zif_allowed_funcs
        self.name = name
        self.role = role

        if zif_func:
            self.zif_func = zif_func
        else:
            self.zif_func = self._pin_zif_default_funcs[role]

        if not self.zif_func:
                raise ValueError(f"Pin {self.name} which is of type {self.role.name} requires zif_func to be defined")
        else:
            for f in self.zif_func:
                if f not in self._pin_zif_allowed_funcs[role]:
                    raise ValueError(f"ZIF function: {f.name} cannot be assigned to pin type: {self.role.name}")


# ------------------------------------------------------------------------
class Part:

    DIP = 1

    _type_names = {
        DIP: "DIP",
    }

    pincount = 0
    package_type = None
    package_pins = {}
    name = None
    tests = None
    missing_tests = None

    def __init__(self):
        self.pins = {}
        self.pins.update(self.package_pins)
        self.pins.update(self.pin_cfg)
        self.debug = False

    def get_test(self, name):
        return next(t for t in self.tests if t.name == name)

    @property
    def package_name(self):
        return f"{self._type_names[self.package_type]}{self.pincount}"

    @property
    def vcc(self):
        return list(k for k, v in self.pins.items() if v.role == PinType.VCC)

    @property
    def gnd(self):
        return list(k for k, v in self.pins.items() if v.role == PinType.GND)

    def __bytes__(self):
        data = []
        cfg_count = 0
        for pin in self.pins.values():
            if len(pin.zif_func) > cfg_count:
                cfg_count = len(pin.zif_func)
        assert 5 > cfg_count > 0
        data.extend([self.package_type, self.pincount, cfg_count])

        if self.debug:
            print(f"DUT pin definitions, {cfg_count} configuration(-s) available:")

        for cfgnum in range(0, cfg_count):
            if self.debug:
                print(f"Configuration {cfgnum}:")
            for num, pin in sorted(self.pins.items()):
                try:
                    pin_func = pin.zif_func[cfgnum]
                except IndexError:
                    pin_func = pin.zif_func[0]
                if self.debug:
                    print(f'{num:-3} {pin.name:6} {pin.role.name:5} ZIF {pin_func.name}')
                data.append(pin_func.value)

        return bytes(data)


# ------------------------------------------------------------------------
class PackageDIP14(Part):
    pincount = 14
    package_type = Part.DIP
    package_pins = {
        7: Pin("GND", PinType.GND),
        14: Pin("VCC", PinType.VCC),
    }


# ------------------------------------------------------------------------
class PackageDIP14_vcc5(Part):
    pincount = 14
    package_type = Part.DIP
    package_pins = {
        5: Pin("VCC", PinType.VCC),
        10: Pin("GND", PinType.GND),
    }


# ------------------------------------------------------------------------
class PackageDIP14_vcc4(Part):
    pincount = 14
    package_type = Part.DIP
    package_pins = {
        4: Pin("VCC", PinType.VCC),
        11: Pin("GND", PinType.GND),
    }


# ------------------------------------------------------------------------
class PackageDIP16(Part):
    pincount = 16
    package_type = Part.DIP
    package_pins = {
        8: Pin("GND", PinType.GND),
        16: Pin("VCC", PinType.VCC),
    }


# ------------------------------------------------------------------------
class PackageDIP16_rotated(Part):
    pincount = 16
    package_type = Part.DIP
    package_pins = {
        8: Pin("VCC", PinType.VCC),
        16: Pin("GND", PinType.GND),
    }


# ------------------------------------------------------------------------
class PackageDIP16_vcc5(Part):
    pincount = 16
    package_type = Part.DIP
    package_pins = {
        5: Pin("VCC", PinType.VCC),
        12: Pin("GND", PinType.GND),
    }


# ------------------------------------------------------------------------
class PackageDIP16_vcc5_gnd13(Part):
    pincount = 16
    package_type = Part.DIP
    package_pins = {
        5: Pin("VCC", PinType.VCC),
        13: Pin("GND", PinType.GND),
    }


# ------------------------------------------------------------------------
class PackageDIP20(Part):
    pincount = 20
    package_type = Part.DIP
    package_pins = {
        10: Pin("GND", PinType.GND),
        20: Pin("VCC", PinType.VCC),
    }


# ------------------------------------------------------------------------
class PackageDIP24(Part):
    pincount = 24
    package_type = Part.DIP
    package_pins = {
        12: Pin("GND", PinType.GND),
        24: Pin("VCC", PinType.VCC),
    }


# ------------------------------------------------------------------------
class TestVector():
    def __init__(self, vector, test):
        self.input = vector[0]
        self.output = vector[1] if vector[1] else []
        self.test = test

    def pin(self, pin):
        try:
            return [*self.input, *self.output][self.test.pins.index(pin)]
        except (IndexError, ValueError):
            return False

    def by_pins(self, pins):
        return [self.pin(i) for i in pins]

    def __str__(self):
        return f"{list(map(int, self.input))} -> {list(map(int, self.output))}"

    def __bytes__(self):
        pin_data = self.by_pins(sorted(self.test.part.pins))
        # If output is empty, that means DUT outputs shouldn't be checked
        # Protocol marks such case with "1" on VCC position
        if not self.output:
            for vcc in self.test.part.vcc:
                pin_data[vcc-1] = 1

        pin_data = list(reversed(pin_data))

        if self.test.debug:
            check = " NC" if not v.output else ""
            print(f" {list(map(int, pin_data))}{check}")

        return bytes(BV(pin_data))


# ------------------------------------------------------------------------
class Test:
    def __init__(self, ttype, name, loops, cfgnum):
        self.type = ttype
        self.name = name
        self.loops = loops
        self.cfgnum = cfgnum
        self.part = None

    def attach_part(self, part):
        self.part = part

    def __bytes__(self):
        data = bytes([self.cfgnum, self.type.value])

        if self.debug:
            print(f"Test type: {self.type.name}")
            print(f"Configuration used: {self.cfgnum}")

        return data

# ------------------------------------------------------------------------
class TestDRAM(Test):
    def __init__(self, name, mem_test_type, mem_size, loops=1, cfgnum=0):
        super(TestDRAM, self).__init__(TestType.DRAM, name, loops, cfgnum)
        self.mem_test_type = mem_test_type
        self.mem_size = mem_size
        self.vectors = []
        # TODO: not really necessary?
        self.inputs = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15]
        self.outputs = [14]

    @property
    def pins(self):
        return self.inputs + self.outputs

    def __bytes__(self):
        data = super().__bytes__()
        data += bytes([self.mem_size, self.mem_test_type, 0, 0])

        if self.debug:
            print(f"DRAM size: {self.mem_size}, test: {self.mem_test_type}")

        # TODO: not really necessary?
        pin_data = [
            1 if i in self.pins else 0
            for i in reversed(sorted(self.part.pins))
        ]
        data += bytes(BV(pin_data))

        return data


# ------------------------------------------------------------------------
class TestUnivib(Test):
    def __init__(self, name, univib_type, univib_test_type, inputs, outputs, loops=1024, cfgnum=0):
        super(TestUnivib, self).__init__(TestType.UNIVIB, name, loops, cfgnum)
        self.univib_type = univib_type
        self.univib_test_type = univib_test_type
        self.vectors = []
        # TODO: not really necessary?
        self.inputs = inputs
        self.outputs = outputs

    @property
    def pins(self):
        return self.inputs + self.outputs

    def __bytes__(self):
        data = super().__bytes__()
        data += bytes([self.univib_type, self.univib_test_type, 0, 0])

        if self.debug:
            print(f"Univibrator type: {self.univib_type}, test: {self.univib_test_type}")

        # TODO: not really necessary?
        pin_data = [
            1 if i in self.pins else 0
            for i in reversed(sorted(self.part.pins))
        ]
        data += bytes(BV(pin_data))

        return data


# ------------------------------------------------------------------------
class TestLogic(Test):

    MAX_TEST_PARAMS = 4

    def __init__(self, name, inputs, outputs, params=[], body=[], loops=1024, cfgnum=0, read_delay_us=0):
        super(TestLogic, self).__init__(TestType.LOGIC, name, loops, cfgnum)
        self.params = params + [0] * (self.MAX_TEST_PARAMS - len(params))
        self.inputs = inputs
        self.outputs = outputs
        self._body = body
        self._vectors = None
        self.read_delay_us = read_delay_us

    def set_delay(self, read_delay_us):
        self.read_delay_us = read_delay_us

    @property
    def pins(self):
        return self.inputs + self.outputs

    @property
    def _body_data(self):
        if callable(self._body):
            return self._body()
        else:
            return self._body

    @property
    def body(self):
        for v in self._body_data:
            i = v[0]
            o = v[1]
            if set(['+', '-']).intersection(i):
                yield [[0 if x == '+' else 1 if x == '-' else x for x in i], None]
                yield [[1 if x == '+' else 0 if x == '-' else x for x in i], None]
                yield [[0 if x == '+' else 1 if x == '-' else x for x in i], o]
            elif set(['/', '\\']).intersection(i):
                yield [[0 if x == '/' else 1 if x == '\\' else x for x in i], None]
                yield [[1 if x == '/' else 0 if x == '\\' else x for x in i], o]
            else:
                yield v

    @property
    def vectors(self):
        if not self._vectors:
            self._vectors = [TestVector(v, self) for v in self.body]
        return self._vectors

    def __bytes__(self):
        data = super().__bytes__()
        data += round(self.read_delay_us/0.2).to_bytes(2, 'little')
        data += bytes([0, 0])

        pin_data = [
            1 if i in self.pins else 0
            for i in reversed(sorted(self.part.pins))
        ]
        if self.debug:
            print(f"Additional read delay: {self.read_delay_us} us")
            print(f"DUT inputs: {self.inputs}")
            print(f"DUT outputs: {self.outputs}")

        data += bytes(BV(pin_data))

        return data

