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

from model_mkbitmanip import *
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

    # reset
    #dut.RST_N.value <= 0
    #yield Timer(10) 
    #dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    # driving the input transaction
    dut.rmode.value = 0 #round_nearest_even
    dut.fpu_op.value = 0 # ADD

    x=np.single('3.5')
    y=np.single('3.75')
    z=x+y
    dut.opa.value = x
    dut.opb.value = y
            
    yield Timer(8) 

    # obtaining the output
    dut_output = dut.out.value
    
    #cocotb.log.info(f' ***** ERROR AT DUT INSTR ={x}  : {hex(instructions[x])} ')
    cocotb.log.info(f'DUT OUTPUT=       {hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT=  {hex(z)}')
    cocotb.log.info(f'DUT INPUT 1=  {hex(x)}')
    cocotb.log.info(f'DUT INPUT 2   ={hex(y)}')
    
    cocotb.log.info(f'*********************************************')

        # comparison
        #error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        #assert dut_output == expected_mav_putvalue, error_message
