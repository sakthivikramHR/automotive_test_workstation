import pytest
import os
from datetime import datetime

def run_safety_suite():
    # Define the report name with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = f"Safety_Report_{timestamp}.xml"
    
    print(f"--- Starting Functional Safety Test Suite: {timestamp} ---")
    
    # Run pytest programmatically
    exit_code = pytest.main([
        "-v", 
        f"--junitxml=reports/{report_name}", 
        "Aufgabe2_Traceability.py"
    ])
    
    if exit_code == 0:
        print("\nALL SAFETY REQUIREMENTS VERIFIED.")
    else:
        print("\n SAFETY VIOLATION DETECTED OR TEST FAILED.")

if __name__ == "__main__":
    # Create a reports folder
    if not os.path.exists("reports"):
        os.makedirs("reports")
    run_safety_suite()