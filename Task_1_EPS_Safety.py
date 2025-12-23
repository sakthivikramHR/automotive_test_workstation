import pytest
from steering_system import calculate_steering_assist

# Test Data: (Speed, Torque, Expected_Assist)
test_cases = [
    (100, 5, 10.0),   # Normal operation
    (249, 25, 0.0),   # Boundary: Just below limit
    (250, 5, 10.0),
    (255, 25, 0.0),   # Boundary: At limit
    (251, 5, 0.0),    # SAFETY TRIGGER: Just above limit
    (300, 2, 0.0),     # Extreme overspeed
    (275, 25, 0.0)
]

@pytest.mark.parametrize("speed, torque, expected", test_cases)

def test_eps_speed_cutoff(speed, torque, expected):
    """
    Verifies that steering assist follows safety requirements
    based on vehicle speed.
    """
    result = calculate_steering_assist(speed, torque)
    
    # In FuSa, we check for exact matches on safety cutoffs
    assert result == expected, f"Failed at {speed}km/h! Expected {expected}, got {result}"

def test_negative_speed_robustness():
    """Robustness test: ECU should handle invalid sensor data (negative speed)"""
    # Typical safety logic would treat negative speed as 0 or an error
    result = calculate_steering_assist(-10, 5)
    assert result >= 0