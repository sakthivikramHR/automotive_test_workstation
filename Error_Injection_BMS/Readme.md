# Error Injection

## Description
This project stimulates/injects an Error into the BMS System and check if the BMS ECU reacts to the error induced.

## Functional Safety Goals

1. The ECU should be aware that one of the important variables, such as temperature, jumps to an impossible value and react accordingly.
2. If at all the variables are anything other than the required datatype (In this case, int), the system should react accordingly.

## How to run the file?

Use the command "pytest -v -s error_injection.py" to run this project.

## Information about the project

1. The Temperature shoots up to an impossible value of 150 degrees within few milliseconds and the ECU must be moved into a specific state. Therefore, the ECU logic is updated for an impossible value.
2. The Communication Error is induced into the variables by assigning them the value of None to see how it reacts when the datatype of int is expected in the logic. Therefore, the ECU logic is also upgraded according to communication failures.