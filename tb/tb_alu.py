
import random
import cocotb
from cocotb.triggers import Timer


"""
Sections marked with TODO is for you to fill in. You will also need to make sure to number the opcode constants accordingly with your alu.sv

Design verification ensures that our designs behaves as expected by meeting our design's original architectural specifications.

There will be resources available in the Discord / GitHub for you to get help on cocotb. 

"""

# The opcode constants must match alu.sv

ADD = 0x0   # OPCODE FOR ADD
SUB = None  # OPCODE FOR SUB
AND = None  # OPCODE FOR AND
OR  = None  # OPCODE FOR OR
XOR = None  # OPCODE FOR XOR
NOT = None  # OPCODE FOR NOT
SLL = None  # OPCODE FOR SLL
SRL = None  # OPCODE FOR SRL
SLT = None  # OPCODE FOR SLT
EQ  = None  # OPCODE FOR EQ

VALID_OPCODES = [ADD, SUB, AND, OR, XOR, NOT, SLL, SRL, SLT, EQ]

MASK32 = 0xFFFFFFFF

def expected_result(a, b, opcode):

    # Keep the inputs within 32 bits
    a = a & MASK32
    b = b & MASK32

    if opcode == ADD:
        # TODO: Return a + b, limited to 32 bits
        pass

    elif opcode == SUB:
        # TODO: Return a - b, limited to 32 bits
        pass

    elif opcode == AND:
        # TODO: Return a AND b
        pass

    elif opcode == OR:
        # TODO: Return a OR b
        pass

    elif opcode == XOR:
        # TODO: Return a XOR b
        pass

    elif opcode == NOT:
        # TODO: Return the 32-bit inverse of a
        pass

    elif opcode == SLL:
        # TODO: Return a logically shifted left by b
        # A shift of 32 or greater should produce zero
        pass

    elif opcode == SRL:
        # TODO: Return a logically shifted right by b
        # A shift of 32 or greater should produce zero
        pass

    elif opcode == SLT:
        # TODO: Return 1 when unsigned a < b; otherwise return 0
        pass

    elif opcode == EQ:
        # TODO: Return 1 when a == b; otherwise return 0
        pass

    else:
        # TODO: Unsupported opcodes should return zero
        pass

async def check_alu(dut, a, b, opcode):

    """
    Apply one set of inputs and check the ALU output.
    """

    # Keep the inputs within 32 bits
    a = a & MASK32
    b = b & MASK32

    # TODO: Drive a into the DUT

    # TODO: Drive b into the DUT

    # TODO: Drive opcode into the DUT

    # TODO: Wait 1 ns for the combinational output to update

    # TODO: Calculate the expected result
    expected = None

    # TODO: Read dut.result and convert it to a Python integer
    actual = None

    # TODO: Assert that actual equals expected
    # Include a useful error message

# Test every operation

@cocotb.test()
async def test_all_operations(dut):
    """
    Test every supported opcode at least once.
    """

    # Example:
    # await check_alu(dut, a=5, b=3, opcode=ADD)

    # TODO: Test ADD

    # TODO: Test SUB

    # TODO: Test AND

    # TODO: Test OR

    # TODO: Test XOR

    # TODO: Test NOT

    # TODO: Test SLL

    # TODO: Test SRL

    # TODO: Test SLT when true

    # TODO: Test SLT when false

    # TODO: Test EQ when true

    # TODO: Test EQ when false

# Edge-case tests

@cocotb.test()
async def test_edge_cases(dut):
    """
    Test important 32-bit boundary conditions.
    """

    # TODO: Test addition overflow:
    # 0xFFFFFFFF + 1

    # TODO: Test subtraction underflow:
    # 0 - 1

    # TODO: Test zero operands

    # TODO: Test maximum-value operands

    # TODO: Test shifting by zero

    # TODO: Test shifting by 31

    # TODO: Test shifting by 32 or greater

# Randomized tests

@cocotb.test()
async def test_random_operations(dut):
    """
    Run randomized inputs for every supported operation.
    """

    # Fixed seed makes test failures repeatable
    rng = random.Random(12345)

    # TODO:
    # Loop through every opcode in VALID_OPCODES.
    #
    # For every opcode:
    #     1. Generate at least 100 random 32-bit values for a and b.
    #     2. Call check_alu(dut, a, b, opcode).

# Invalid-opcode tests

@cocotb.test()
async def test_invalid_opcodes(dut):
    """
    Confirm that unsupported opcodes produce zero.
    """

    # TODO:
    # Test invalid opcodes from 0b1010 through 0b1111.
