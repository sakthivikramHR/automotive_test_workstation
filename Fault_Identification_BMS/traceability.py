import pytest
import json
from BMS_ECU import BatteryManagementSystem

# Load requirements for reporting
with open("Requirements.json") as f:
    REQS = json.load(f)

@pytest.fixture

def bms():
    """Provides a fresh BMS instance for every test."""
    return BatteryManagementSystem()

def test_thermal_shutdown_requirement(bms):
    """Verify REQ_BMS_001: Shutdown on high temp."""
    # Test Step: Inject 65 degrees
    bms.process_telemetry(temp=65, voltage=3.7)
    
    status = bms.get_status()
    
    assert status["state"] == "SHUTDOWN"
    assert status["contactors"] is False
    print(f"\nVerified {REQS['REQ_BMS_001']}")

def test_overvoltage_fault_requirement(bms):
    """Verify REQ_BMS_002: Fault on high voltage."""
    # Test Step: Inject 4.5V
    bms.process_telemetry(temp=25, voltage=4.5)
    
    status = bms.get_status()
    
    assert status["state"] == "OVERVOLTAGE_FAULT"
    assert status["contactors"] is False
    print(f"\nVerified {REQS['REQ_BMS_002']}")

def test_undervoltage_fault_requirement(bms):
    """Verify REQ_BMS_003: Fault on low voltage."""
    # Test Step: Inject 1.8V
    bms.process_telemetry(temp=30, voltage=1.8)
    
    status = bms.get_status()
    
    assert status["state"] == "UNDERVOLTAGE_FAULT"
    assert status["contactors"] is False
    print(f"\nVerified {REQS['REQ_BMS_003']}")


def test_low_temperature_fault_requirement(bms):
    """Verify REQ_BMS_004: Fault on low temperature."""
    # Test Step: Inject 18 degrees
    bms.process_telemetry(temp=18, voltage=3)
    
    status = bms.get_status()
    
    assert status["state"] == "LOW_TEMPERATURE_FAULT"
    assert status["contactors"] is False
    print(f"\nVerified {REQS['REQ_BMS_004']}")

def test_normal_requirement(bms):
    """Verify REQ_BMS_005: Normal Behaviour of BMS."""
    # Test Step: Temperature to stay between 20 and 60 degree Celsius
    # Test Step: Voltage to stay between 2.5 and 4.2 Volts
    bms.process_telemetry(temp=35, voltage=3.3)
    
    status = bms.get_status()
    
    assert status["state"] == "NORMAL"
    assert status["contactors"] is True
    print(f"\nVerified {REQS['REQ_BMS_005']}")