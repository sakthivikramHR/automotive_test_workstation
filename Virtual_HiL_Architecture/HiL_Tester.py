import can
import cantools
import time

db = cantools.database.load_file('battery.dbc')
bus = can.interface.Bus('v-hil-bus', bustype='virtual')

def inject_fault(test_name, temp, voltage):
    print(f"\nRunning Test: {test_name}")
    
    # 1. Pack the data based on DBC
    data = db.encode_message('BMS_Status', {'BatteryTemp': temp, 'BatteryVoltage': voltage})
    
    # 2. Send the CAN message
    msg = can.Message(arbitration_id=500, data=data, is_extended_id=False)
    bus.send(msg)
    print(f"Tester TX: Sent {temp}degC, {voltage}V")
    
    # Give the "ECU" a moment to process
    time.sleep(0.5)

if __name__ == "__main__":
    # Test Case 1: Normal Operation
    inject_fault("TC_01_Normal", temp=30, voltage=3.7)
    
    # Test Case 2: Over-temperature Fault
    inject_fault("TC_02_OverTemp_Fault", temp=75, voltage=3.7)