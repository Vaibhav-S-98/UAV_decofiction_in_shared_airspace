# UAV Strategic Deconfliction System (3D + Time Check)

## Overview
This project is a simulation tool to check if a drone’s planned flight path is safe to execute in shared airspace.  
It compares the primary drone's mission against other drones' missions to detect any conflicts in space and time.

The system:
- Takes waypoints (x, y, z, time) for all drones.
- Checks for spatial conflicts (distance check).
- Checks for temporal conflicts (time overlap).
- Reports detailed conflicts.
- Shows a 3D plot of all drone paths with conflicts marked in red.


# Requirements
- Python 3.8+
- matplotlib

# Install dependencies:
- pip install matplotlib

# Project Structure
uav_deconfliction/
    __init__.py
    drone_data.py
    utils.py
    spatial_check.py
    temporal_check.py
    visualization.py
main.py
README.md

# How to Run
- Place your mission data in main.py or load from a file.

- Run: `python main.py`

- The console will show detected conflicts.
- A 3D plot will display all missions and conflict points.
