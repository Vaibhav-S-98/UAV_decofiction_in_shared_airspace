from typing import List, Tuple
from uav_deconfliction.drone_data import Mission, Waypoint
from uav_deconfliction.utils import time_overlap

def temporal_conflicts(                                      # Checks for temporal conflicts between two missions.
    mission_a: Mission,                                      # Returns a list of waypoint pairs where the time intervals overlap.
    mission_b: Mission) -> List[Tuple[Waypoint, Waypoint]]:
    
    conflicts = []
    for wp_a in mission_a.waypoints:
        for wp_b in mission_b.waypoints:                     # Convert waypoint times to absolute mission times
            abs_time_a = mission_a.start_time + wp_a.time
            abs_time_b = mission_b.start_time + wp_b.time
            if abs(abs_time_a - abs_time_b) <= 1:            # consider them same time if they happen within 1 second
                conflicts.append((wp_a, wp_b))  
    return conflicts

