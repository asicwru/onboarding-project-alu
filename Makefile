# Makefile

SIM ?= verilator
TOPLEVEL_LANG = verilog

VERILOG_SOURCES = $(PWD)/alu.sv

COCOTB_TOPLEVEL = alu
COCOTB_TEST_MODULES = tb_alu

include $(shell cocotb-config --makefiles)/Makefile.sim
