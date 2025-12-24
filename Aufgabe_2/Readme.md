# Automotive BMS Functional Safety Validator (SiL)

## Description
This project simulates a Battery Management System (BMS) to verify safety-critical requirements (ASIL-B/C).

## Functional Safety Goals

You can find the safety mechanisms defined in `requirements.json`:
* **REQ_BMS_001:** Thermal shutdown if Temp > 60°C.
* **REQ_BMS_002:** Overvoltage protection if Voltage > 4.2V.
* **REQ_BMS_003:** Perfectly normal condition if Temp < 60°C.
* **REQ_BMS_004:** Undervoltage detection if Voltage < 2.5V.

## How to run the file?

First, the user can update the testing requirements in the file "Traceability.py".
Second, the user can update the conditions in "BMS_ECU.py" file.

Finally, Run the file "Automated_Reporting"
