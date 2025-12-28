import pytest
from BMS_ECU_EI import BatteryManagementSystem

@pytest.fixture
def bms():
    return BatteryManagementSystem()


def test_forced_shutdown(bms):
    # Normal Temperature    
    bms.process_telemetry(25, 3.7)
    assert bms.state == "NORMAL"
    # Inject a Impossible jump
    # A real sensor jumps from 25 to 160
    bms.process_telemetry(160, 3.7)    
    assert bms.state == "FORCED_SHUTDOWN"
    print(f"--> ECU entered {bms.state} state on extreme temperature jump")

def test_sensor_timeout(bms):
    # 'None' can simulate a lost signal or sensor timeout which means a Communication Failure (CRC/ALIV/TIMEOUT)
    try:
        bms.process_telemetry(None, None)
        assert bms.state == "SENSOR_COMMUNICATION_ERROR"
        print(f"--> ECU entered {bms.state} state on communication error")
    except Exception as e:
        pytest.fail(f"ECU Crashed on missing data! Error: {e}")

def test_frozen_sensor(bms):    
    # Sensor to get frozen for a threshold of 6. 
    for i in range(6):
        bms.process_telemetry(30, 3.7)
    
    status = bms.get_status()
    assert status["state"] == "SENSOR_FROZEN_FAULT"
    print(f"--> ECU entered {bms.state} state because the sensor entered Frozen state")


def test_cyclic_redudancy_check(bms):
    bms.process_telemetry_crc(30, 5, 87)
    status = bms.get_status()
    assert status["state"] == "CRC_COMMUNICATION_ERROR"
    print(f"--> ECU entered {bms.state} state because of Cyclic Redudancy Check Failure")