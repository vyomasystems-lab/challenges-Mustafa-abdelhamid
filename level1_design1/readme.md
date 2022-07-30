# Level 1 design 1 Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![](https://i.imgur.com/miWGA1o.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs *a* and *b* and gives 5-bit output *sum*

The values are assigned to the input port using random generated data to all 32 mux 
 ``` 
  random_data.append(random.randint(0, 3))
```
then a for loop to change select line from 0 to 31 
```
for i in range(30): ## TESTING ALL POSSIPLE SELECTIONS
        dut.sel.value=i
        await Timer(1, units="ns")
```

The assert statement is used for comparing the  outut to the expected value.

The following error is seen:
![image](https://user-images.githubusercontent.com/90484856/181624483-f56c4219-1f5c-4a1d-a5ae-b871188b035f.png)

## Test Scenario **(Important)**
- Test Inputs: SEL = 12 
- Expected Output: out=2
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
The design has the following bugs 
* SEL=12 isn't included so whenever selection line is 12 the output is the default value = 0 
* SEL=13 is repeated for both selection line values = 12 and 13 so the output when the selection line is 13 is ambiguious and the simulator choosed the input 12  

## Design Fix
Updating the design and re-running the test makes the test pass.

## Verification Strategy
 The input data is randomised 
 all selection lines were tested 
## Is the verification complete ?
 Yes
