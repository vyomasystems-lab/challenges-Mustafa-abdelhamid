

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for FPU"""

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    
    
    await FallingEdge(dut.clk)  
    dut.opcode.value = 0 # ADD
    x=random.randint(0,(2**32)-1)
    x_length=len(bin(x))-2
    if(x_length < 32):
        m=32-x_length
        x_sign=0
        x_exponent=int(bin(x)[3:11],2)
        x_exponent=(x_exponent>>m)-127
        print(x_exponent)
        x_mantissa=int(bin(x)[12::],2) >>m
        x_mantissa=x_mantissa* (2**-23)
        print(x_mantissa)

        if (x_exponent==-127): # denormal
            if(x_sign==0):
                x_value= (x_mantissa)*(2**x_exponent)
            else:
                x_value= -1*(x_mantissa)*(2**x_exponent)

        else:
            if(x_sign==0):
                x_value= (1+x_mantissa)*(2**x_exponent)
            else:
                x_value= -1*(1+x_mantissa)*(2**x_exponent)
    
    else:
        x_sign=int(bin(x)[2],2)
        x_exponent=int(bin(x)[3:11],2)-127
        print(x_exponent)
        x_mantissa=int(bin(x)[12::],2) * (2**-23)
        print(x_mantissa)

        if (x_exponent==-127): # denormal
            if(x_sign==0):
                x_value= (x_mantissa)*(2**x_exponent)
            else:
                x_value= -1*(x_mantissa)*(2**x_exponent)

        else:
            if(x_sign==0):
                x_value= (1+x_mantissa)*(2**x_exponent)
            else:
                x_value= -1*(1+x_mantissa)*(2**x_exponent)

    print(x_value)
    dut.A.value=x
    y=random.randint(0,(2**32)-1)
    print(bin(x))
    dut.B.value =y
    print(bin(y))
    await FallingEdge(dut.clk)
    dut_output = dut.O.value
    print(dut_output)
    print(bin(x))
    print(bin(y))

    cocotb.log.info('#### CTB: Develop your test here! ######')
    

    
    
    
     
     
# See LICENSE.iitm for details
# See LICENSE.vyoma for details
#import numpy as np
#import random
#import sys
#import cocotb
#from cocotb.decorators import coroutine
#from cocotb.triggers import Timer, RisingEdge
#from cocotb.result import TestFailure
#from cocotb.clock import Clock
   
