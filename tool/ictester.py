#!/usr/bin/env python3

import sys
import argparse
import math
import re
import time

from tester import Tester
from parts import catalog


# ------------------------------------------------------------------------
def list_parts(list_tests=False):
    families = {}
    for i in catalog.items():
        family = i[0][0:2]
        if family not in families:
            families[family] = []
        families[family].append(i)

    for family, parts in sorted(families.items()):
        for name, part in sorted(parts, key=lambda x: int(re.sub("74[HS]", "74", x[0]))):
            print(f"{name:7s} {part.full_package_name:15s} {part.desc}")
            if (list_tests):
                for t in part.tests:
                    # NOTE: hack to work around sequentialize()
                    l = 2*len(t.body) if (t.type == t.SEQ) else len(t.body)
                    print(f"  * ({l} vectors) {t.name}")

# ------------------------------------------------------------------------
def print_part_info(part):
    print(f"Part: {part.name}, {part.full_package_name} - {part.desc}")
    if part.missing_tests:
        print(f"{WARN}WARNING: missing tests: {part.missing_tests}{ENDC}")
    if part.unusual_power:
        print(f"{WARN}WARNING: unusual pins used for power. Make sure to use the correct socket and orientation.{ENDC}")


# ------------------------------------------------------------------------
# --- Main ---------------------------------------------------------------
# ------------------------------------------------------------------------

FAIL = '\033[91m\033[1m'
OK = '\033[92m\033[1m'
WARN = '\033[95m\033[1m'
ENDC = '\033[0m'

if '--list' in sys.argv:
    list_parts("--tests" in sys.argv)
    sys.exit(0)

parser = argparse.ArgumentParser(description='IC tester controller')
parser.add_argument('--device', default="/dev/ttyUSB1", help='Serial port where the IC tester is connected')
parser.add_argument('--loops', type=int, help='Loop count (<65536, will be rounded to the nearest power of 2)')
parser.add_argument('--list', action="store_true", help='List all supported parts')
parser.add_argument('--tests', action="store_true", help='When listing parts, list also tests for each part')
parser.add_argument('--debug', action="store_true", help='Enable debug output')
parser.add_argument('--serial_debug', action="store_true", help='Enable serial debug output')
parser.add_argument('part', help='Part symbol')
args = parser.parse_args()

try:
    part = catalog[args.part.upper()]
except KeyError:
    print(f"Part not found: {args.part}")
    print("Use --list to list all supported parts")
    sys.exit(100)

print_part_info(part)

tester = Tester(part, args.device, 500000, debug=args.debug, serial_debug=args.serial_debug)
all_tests = tester.tests_available()
test_count = len(all_tests)
longest_desc = len(max(all_tests, key=len))
tests_passed = 0

total_time = 0
print()
for test_name in all_tests:
    test = tester.part.get_test(test_name)
    loops_pow = round((math.log2(args.loops if args.loops else test.loops)))
    loops = 2 ** loops_pow

    plural = "s" if loops != 1 else ""
    endc = "\n" if args.debug else ""
    print(f" * Testing: {test_name:{longest_desc}s}   {loops} loop{plural}  ... ", end=endc, flush=True)

    start = time.time()
    res = tester.exec_test(test, loops_pow)
    elapsed = time.time() - start
    total_time += elapsed

    if res == Tester.RES_PASS:
        tests_passed += 1
        print(f"\b\b\b\b{OK}PASS{ENDC}  ({elapsed:.2f} sec.)")
    else:
        print(f"\b\b\b\b{FAIL}FAIL{ENDC}  ({elapsed:.2f} sec.)")

if tests_passed != test_count:
    color = FAIL
    result = "PART DEFECTIVE"
    ret = 1
else:
    color = OK
    result = "PART OK"
    ret = 0

print(f"\n{color}{result}: {tests_passed} of {test_count} tests passed{ENDC}  ({total_time:.2f} sec. total)")

sys.exit(ret)
