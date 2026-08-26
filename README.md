# Onboarding Project: ALU

ASICWRU's Level 1 Onboarding Project: a 32-bit Arithmetic Logic Unit (ALU) written in SystemVerilog, verified with a Python ([cocotb](https://www.cocotb.org/)) testbench.

For the full project write-up (what an ALU does, the spec, and why we're building one), see [`L1_ALU_README.md`](https://github.com/asicwru/asicwru-onboarding/blob/main/L1_ALU_README.md) in the [asicwru-onboarding](https://github.com/asicwru/asicwru-onboarding) repo. This README just covers how to work in *this* repo.

---

## Repo Structure

```
.
├── Makefile        # Runs the Verilator + cocotb simulation
├── rtl/
│   └── alu.sv       # The ALU design
└── tb/
    └── tb_alu.py    # The cocotb testbench
```

## Prerequisites

- [Verilator](https://verilator.org/guide/latest/install.html)
- Python 3 with [cocotb](https://www.cocotb.org/) installed:

  ```bash
  pip install cocotb
  ```

## What to Do

1. **`rtl/alu.sv`** — Implement the ALU. The `ADD` opcode (`4'h0`) and its logic are done for you as an example. Fill in the remaining `localparam` opcodes and their `case` branches for `SUB`, `AND`, `OR`, `XOR`, `NOT`, `SLL`, `SRL`, `SLT`, and `EQ`. Any opcode you don't define should fall through to the `default: result = 32'b0;` branch.

2. **`tb/tb_alu.py`** — Implement the testbench. This includes:
   - The opcode constants (must match the values you chose in `alu.sv`)
   - `expected_result` — a plain-Python reference model for each operation
   - `check_alu` — drives inputs into the DUT and asserts the output matches `expected_result`
   - The test cases in `test_all_operations`, `test_edge_cases`, `test_random_operations`, and `test_invalid_opcodes`

## Running the Tests

```bash
make
```

This compiles `rtl/alu.sv` with Verilator, runs it against `tb/tb_alu.py`, and prints a pass/fail summary for every cocotb test. To re-run from a clean state:

```bash
make clean
make
```

## Done When

All four test groups pass with no failures:

- `test_all_operations` — every opcode produces the correct result at least once
- `test_edge_cases` — 32-bit boundaries (overflow, underflow, shift ≥ 32, etc.) are handled correctly
- `test_random_operations` — 100+ randomized inputs per opcode all check out against the reference model
- `test_invalid_opcodes` — undefined opcodes (`0b1010`–`0b1111`) all produce `0`

Stuck? Ask in the `#onboarding-channel` on Discord.
