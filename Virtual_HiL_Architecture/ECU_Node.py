import can
import cantools
from BMS_ECU_Logic import BatteryManagementSystem

# Load DBC and Initialize BMS Logic
db = cantools.database.load_file('battery.dbc')
bms_logic = BatteryManagementSystem()

def start_ecu():
    # Connect to the virtual bus
    bus = can.interface.Bus('v-hil-bus', bustype='virtual')
    print("ECU Node: Online. Waiting for CAN data...")

    while True:
        message = bus.recv() # Wait for a message
        if message is not None and message.arbitration_id == 500:
            # Decode the message
            decoded = db.decode_message('BMS_Status', message.data)
            temp = decoded['BatteryTemp']
            volt = decoded['BatteryVoltage']
            
            # Run the Safety Logic
            bms_logic.process_telemetry(temp, volt)
            status = bms_logic.get_status()
            
            print(f"ECU RX: Temp={temp}, Volt={volt} | State: {status['state']}")
            
            # If in fault, we could send a "Fault Frame" back here
            if status['state'] != "NORMAL":
                print("SAFETY ACTION TAKEN: OPENING CONTACTORS")

if __name__ == "__main__":
    start_ecu()