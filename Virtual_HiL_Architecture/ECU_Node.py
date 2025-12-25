import can
import cantools
from BMS_ECU_Logic import BatteryManagementSystem

# Load DBC and Initialize BMS Logic
db = cantools.database.load_file('battery.dbc')
bms_logic = BatteryManagementSystem()

def start_ecu():
    
    bus = can.interface.Bus('v-hil-bus', bustype='virtual')
    print("ECU Node: Online. Waiting for CAN data...")

    while True:
        message = bus.recv()
        if message is not None and message.arbitration_id == 500:
            
            decoded = db.decode_message('BMS_Status', message.data)
            temp = decoded['BatteryTemp']
            volt = decoded['BatteryVoltage']
            
            bms_logic.process_telemetry(temp, volt)
            status = bms_logic.get_status()
            
            print(f"ECU RX: Temp={temp}, Volt={volt} | State: {status['state']}")
        
            if status['state'] != "NORMAL":
                print("SAFETY ACTION TAKEN: OPENING CONTACTORS")

if __name__ == "__main__":
    start_ecu()