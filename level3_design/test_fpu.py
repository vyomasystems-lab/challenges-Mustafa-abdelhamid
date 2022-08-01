# See LICENSE.iitm for details
# See LICENSE.vyoma for details
import numpy as np
import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

#input		clk;
#input	[1:0]	rmode;
#input	[2:0]	fpu_op;
#input	[31:0]	opa, opb;

#output	[31:0]	out;
#output		inf, snan, qnan;
#output		ine;
#output		overflow, underflow;
#output		zero;
#output		div_by_zero;

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk))

    
    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    # driving the input transaction
    dut.opcode.value = 0 # ADD

    x=random.randint(0,(2**32)-1)
    y=random.randint(0,(2**32)-1)
    
    
    dut.A.value =x
    print(bin(x))
    dut.B.value =y
    print(bin(y))

    # obtaining the output
    yield Timer(12) 

    dut_output = dut.O.value
    print(dut_output)
   
