class BatteryManagementSystem:
    def __init__(self):
        self.state = "NORMAL"
        self.contactors_closed = True
        self.last_temperature = None
        self.freeze_counter = 0
        self.freeze_threshold = 5

    def process_telemetry(self, temperature, voltage):
        """Processes sensor data and updates system state."""

        if temperature == self.last_temperature:
            self.freeze_counter += 1
        else:
            self.freeze_counter = 0
            
        self.last_temperature = temperature
        if self.freeze_counter >= self.freeze_threshold:
            self.state = "SENSOR_FROZEN_FAULT"
            self.contactors_closed = False
            return

        # Logic for Communication Problems --> (ALIV/CRC/CHL Failures) 
        if temperature is None or voltage is None: 
            self.state = "SENSOR_COMMUNICATION_ERROR"
            self.contactors_closed = False
            return
        
        # Safety Logic for Temperature
        if temperature > 60 and temperature < 150:
            self.state = "SHUTDOWN"
            self.contactors_closed = False
            return
        
        # Safety Logic for Temperature
        if temperature >= 150:
            self.state = "FORCED_SHUTDOWN"
            self.contactors_closed = False
            return
        
        # Safety Logic for Temperature
        if temperature < 20:
            self.state = "LOW_TEMPERATURE_FAULT"
            self.contactors_closed = False
            return
            
        # Safety Logic for Voltage --> Overvoltage State
        if voltage > 4.2:
            self.state = "OVERVOLTAGE_FAULT"
            self.contactors_closed = False
            return
        
        # Safety Logic for Voltage --> Undervoltage State
        if voltage < 2.5:
            self.state = "UNDERVOLTAGE_FAULT"
            self.contactors_closed = False
            return

        # Default logic for i.O. State
        self.state = "NORMAL"
        self.contactors_closed = True
        return

    def get_status(self):
        return {"state": self.state, "contactors": self.contactors_closed}

    def process_telemetry_crc(self, temperature, voltage, checksum):

        expected_checksum = int(temperature + voltage) if temperature and voltage else 0
        
        if checksum != expected_checksum:
            self.state = "CRC_COMMUNICATION_ERROR"
            self.contactors_closed = False
            return