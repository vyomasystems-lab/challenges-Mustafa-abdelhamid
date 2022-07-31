# Level 1 design 1 Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs *a* and *b* and gives 5-bit output *sum*

The values are assigned to the input port using random generated data to sources inputs 1, 2, and 3 
 ``` 
        mav_putvalue_src1 = random.randint(0, (2**32)-1)
        mav_putvalue_src2 = random.randint(0, (2**32)-1)
        mav_putvalue_src3 = random.randint(0, (2**32)-1)
```
then a for loop to verify all instructions. A python dictionary stores all instructions keys are instruction and value is its corresponding binary representation
![image](https://user-images.githubusercontent.com/90484856/182022003-80268165-67a7-4b6f-99b5-b37737335c23.png)
  
```
for x in instructions:
        mav_putvalue_instr = instructions[x]
```

The assert statement is used for comparing the  outut to the expected value.

## The following error is seen:
![image](https://user-images.githubusercontent.com/90484856/182021965-173e5f94-9753-4436-95b2-b7f365e55fe6.png)

## Test Scenario **(Important)**
- Test Inputs: DUT instruction = ANDN ( 0x40007033 ) 
- Expected Output:              0x1002c010d
- Observed Output in the DUT:   0x023820021

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
The design has the following bugs 
* ANDN instruction output doesn't match ANDN model output  

## Design Fix
Updating the design and re-running the test makes the test pass.

## Verification Strategy
 The input data is randomised 
 all instructions  were tested 
## Is the verification complete ?
  More direct test for the corner cases of sources operands need to be done
