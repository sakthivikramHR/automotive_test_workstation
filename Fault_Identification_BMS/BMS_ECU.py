class BatteryManagementSystem:
    def __init__(self):
        self.state = "NORMAL"
        self.contactors_closed = True

    def process_telemetry(self, temp, voltage):
        """Processes sensor data and updates system state."""
        # Safety Logic for Temperature
        if temp > 60:
            self.state = "SHUTDOWN"
            self.contactors_closed = False
            return
        
        # Safety Logic for Temperature
        if temp < 20:
            self.state = "LOW_TEMPERATURE_FAULT"
            self.contactors_closed = False
            return
            
        # Safety Logic for Voltage
        if voltage > 4.2:
            self.state = "OVERVOLTAGE_FAULT"
            self.contactors_closed = False
            return
        
        # Safety Logic for Voltage 
        if voltage < 2.5:
            self.state = "UNDERVOLTAGE_FAULT"
            self.contactors_closed = False
            return

        if 20 < temp < 60 and 2.5 < voltage < 4.2:
            self.state = "NORMAL"
            self.contactors_closed = True
            return

    def get_status(self):
        return {"state": self.state, "contactors": self.contactors_closed}