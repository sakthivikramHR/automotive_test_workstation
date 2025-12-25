import pytest
from BMS_ECU_EI import BatteryManagementSystem

@pytest.fixture
def bms():
    return BatteryManagementSystem()


def test_erroneous_signal_jump(bms):
    # Normal Temperature    
    bms.process_telemetry(temp=25, voltage=3.7)
    assert bms.state == "NORMAL"
    
    # Inject a Impossible jump
    # A real sensor jumps from 25 to 150
    bms.process_telemetry(temp=150, voltage=3.7)    
    assert bms.state == "EXTREME_SHUTDOWN"
    print(f"\n[PASSED] ECU entered {bms.state} state on extreme temperature jump.")

def test_sensor_timeout_simulation(bms):
    # 'None' can simulate a lost signal or sensor timeout which means a Communication Failure (CRC/ALIV/TIMEOUT)
    try:
        bms.process_telemetry(None, None)
        assert bms.state == "SENSOR_ERROR"
        print(f"\n[PASSED] ECU entered {bms.state} state on communication error.")
    except Exception as e:
        pytest.fail(f"ECU Crashed on missing data! Error: {e}")