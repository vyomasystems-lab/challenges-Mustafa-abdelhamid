# See LICENSE.vyoma for details
import random
import array as arr

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    random_data= arr.array('i')
    for i in range (32):
        random_data.append(random.randint(0, 3))
    dut.inp0.value=random_data[0]
    dut.inp1.value=random_data[1]
    dut.inp2.value=random_data[2]
    dut.inp3.value=random_data[3]
    dut.inp4.value=random_data[4]
    dut.inp5.value=random_data[5]
    dut.inp6.value=random_data[6]
    dut.inp7.value=random_data[7]
    dut.inp8.value=random_data[8]
    dut.inp9.value=random_data[9]
    dut.inp10.value=random_data[10]

    dut.inp11.value=random_data[11]
    dut.inp12.value=random_data[12]
    dut.inp13.value=random_data[13]
    dut.inp14.value=random_data[14]
    dut.inp15.value=random_data[15]
    dut.inp16.value=random_data[16]
    dut.inp17.value=random_data[17]
    dut.inp18.value=random_data[18]
    dut.inp19.value=random_data[19]

    dut.inp20.value=random_data[20]
    dut.inp21.value=random_data[21]
    dut.inp22.value=random_data[22]
    dut.inp23.value=random_data[23]
    dut.inp24.value=random_data[24]
    dut.inp25.value=random_data[25]
    dut.inp26.value=random_data[26]
    dut.inp27.value=random_data[27]
    dut.inp28.value=random_data[28]
    dut.inp29.value=random_data[29]
    
    dut.inp30.value=random_data[30]
    for i in range(30): ## TESTING ALL POSSIPLE SELECTIONS
        dut.sel.value=i
        await Timer(1, units="ns")
        print("DUT VALUE :",dut.out.value)
        print("EXPECTED VALUE: ",random_data[i])
         
        assert dut.out.value == random_data[i],"FAIL"
        await Timer(2, units="ns") 