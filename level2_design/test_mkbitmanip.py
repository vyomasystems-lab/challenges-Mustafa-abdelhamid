# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

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
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    instructions={
        # R type
        ######################################################
        #"AND"   :0b0000000_00000_00000_111_00000_0110011,
        #"OR"    :0b0000000_00000_00000_110_00000_0110011,
        #"XOR"   :0b0000000_00000_00000_100_00000_0110011,
        "ANDN"  :0b0100000_00000_00000_111_00000_0110011,
        "ORN"   :0b0100000_00000_00000_110_00000_0110011,
        "XORN"  :0b0100000_00000_00000_100_00000_0110011,
        ######################################################
        #"SLL"   :0b0000000_00000_00000_001_00000_0110011,
        #"SRL"   :0b0000000_00000_00000_101_00000_0110011,
        #"SRA"   :0b0100000_00000_00000_101_00000_0110011,
        "SLO"   :0b0010000_00000_00000_001_00000_0110011,
        "SRO"   :0b0010000_00000_00000_101_00000_0110011,
        "ROL"   :0b0110000_00000_00000_001_00000_0110011,
        "ROR"   :0b0110000_00000_00000_101_00000_0110011,
        #######################################################
        "SBCLR" :0b0100100_00000_00000_001_00000_0110011,
        "SBSET" :0b0010100_00000_00000_001_00000_0110011,
        "SBINV" :0b0110100_00000_00000_001_00000_0110011,
        "SBEXT" :0b0100100_00000_00000_101_00000_0110011,
        "GORC"  :0b0010100_00000_00000_101_00000_0110011,
        "GREV"  :0b0110100_00000_00000_101_00000_0110011,
        #######################################################
        # I type
        ######################################################
        #"SLLI"  :0b00000_0000000_00000_001_00000_0010011,
        #"SRLI"  :0b00000_0000000_00000_101_00000_0010011,
        #"SRAI"  :0b01000_0000000_00000_101_00000_0010011,
        "SLOI"  :0b00100_0000000_00000_001_00000_0010011,
        "SROI"  :0b00100_0000000_00000_101_00000_0010011,
        "RORI"  :0b01100_0000000_00000_101_00000_0010011,
        #######################################################
        "SBCLRI" :0b01001_0000000_00000_001_00000_0010011,
        "SBSETI" :0b00101_0000000_00000_001_00000_0010011,
        "SBINVI" :0b01101_0000000_00000_001_00000_0010011,
        "SBEXTI" :0b01001_0000000_00000_101_00000_0010011,
        "GORCI"  :0b00101_0000000_00000_101_00000_0010011,
        "GREVI"  :0b01101_0000000_00000_101_00000_0010011,
        #######################################################
        # R4 type
        "SBCLRI" :0b00000_11_00000_00000_001_00000_0110011,
        "SBSETI" :0b00000_11_00000_00000_101_00000_0110011,
        "SBINVI" :0b00000_10_00000_00000_001_00000_0110011,
        "SBEXTI" :0b00000_10_00000_00000_101_00000_0110011,
        "GORCI"  :0b00000_1_000000_00000_101_00000_0110011
    }

    for x in instructions:
        mav_putvalue_src1 = random.randint(0, (2**32)-1)
        mav_putvalue_src2 = random.randint(0, (2**32)-1)
        mav_putvalue_src3 = random.randint(0, (2**32)-1)
        mav_putvalue_instr = instructions[x]

        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
    
        yield Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value
        if(dut_output != expected_mav_putvalue):
            cocotb.log.info(f' ***** ERROR AT DUT INSTR ={x}  : {hex(instructions[x])} ')
            cocotb.log.info(f'DUT OUTPUT=       {hex(dut_output)}')
            cocotb.log.info(f'EXPECTED OUTPUT=  {hex(expected_mav_putvalue)}')
            cocotb.log.info(f'DUT INPUT 1=  {hex(mav_putvalue_src1)}')
            cocotb.log.info(f'DUT INPUT 2   ={hex(mav_putvalue_src2)}')
            cocotb.log.info(f'DUT INPUT 3   ={hex(mav_putvalue_src3)}')
            cocotb.log.info(f'*********************************************')

        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message
