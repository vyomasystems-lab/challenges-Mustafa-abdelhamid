# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    dut.inp0.value=random.randint(0, 3)
    dut.inp1.value=random.randint(0, 3)
    dut.inp2.value=random.randint(0, 3)
    dut.inp3.value=random.randint(0, 3)
    dut.inp4.value=random.randint(0, 3)
    dut.inp5.value=random.randint(0, 3)
    dut.inp6.value=random.randint(0, 3)
    dut.inp7.value=random.randint(0, 3)
    dut.inp8.value=random.randint(0, 3)
    dut.inp9.value=random.randint(0, 3)
    dut.inp10.value=random.randint(0, 3)

    dut.inp11.value=random.randint(0, 3)
    dut.inp12.value=random.randint(0, 3)
    dut.inp13.value=random.randint(0, 3)
    dut.inp14.value=random.randint(0, 3)
    dut.inp15.value=random.randint(0, 3)
    dut.inp16.value=random.randint(0, 3)
    dut.inp17.value=random.randint(0, 3)
    dut.inp18.value=random.randint(0, 3)
    dut.inp19.value=random.randint(0, 3)

    dut.inp20.value=random.randint(0, 3)
    dut.inp21.value=random.randint(0, 3)
    dut.inp22.value=random.randint(0, 3)
    dut.inp23.value=random.randint(0, 3)
    dut.inp24.value=random.randint(0, 3)
    dut.inp25.value=random.randint(0, 3)
    dut.inp26.value=random.randint(0, 3)
    dut.inp27.value=random.randint(0, 3)
    dut.inp28.value=random.randint(0, 3)
    dut.inp29.value=random.randint(0, 3)
    
    dut.inp30.value=random.randint(0, 3)
    dut.inp31.value=random.randint(0, 3)
    for i in range(31): ## TESTING ALL POSSIPLE SELECTIONS
        dut.sel.value=i
            assert dut.out.value == dut."inp"+str(i).value,"FAIL" 