# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog
GUI = 1 
PWD=$(shell pwd)
VERILOG_SOURCES = $(PWD)/fpu.v  
#VERILOG_SOURCES = $(PWD)/verilog/fpu.v  \
				  $(PWD)/verilog/*v   \
				  $(PWD)/test_bench/test_top.v          # provide your design path

TOPLEVEL :=fpu         # design file
MODULE   :=test_fpu     # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 