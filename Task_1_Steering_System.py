def calculate_steering_assist(vehicle_speed, driver_torque):
    """
    Logic: Provides assist current based on torque, 
    but has a safety cutoff at 250 km/h.
    """
    SAFETY_LIMIT_SPEED = 250  # km/h
    
    if vehicle_speed > SAFETY_LIMIT_SPEED:
        return 0.0  # Safety Mechanism: Shut down assist
    
    # Condition: Driving torque is more than 20Nm, it means Sensor Failure
    if driver_torque > 20:
        return 0.0
    
    # Simple assist logic: Calculating 2 Amps per Nm of torque
    assist_current = driver_torque * 2.0
    return assist_current