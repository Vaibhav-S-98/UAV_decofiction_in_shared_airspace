from typing import List, Tuple
from uav_deconfliction.drone_data import Mission, Waypoint
from uav_deconfliction.utils import euclidean_distance_3d 

def spatial_conflicts(
    mission_a: Mission, 
    mission_b: Mission, 
    safety_distance: float) -> List[Tuple[Waypoint, Waypoint]]:

    conflicts = []
    for wp_a in mission_a.waypoints:
        for wp_b in mission_b.waypoints:
            dist = euclidean_distance_3d(wp_a, wp_b)
            if dist < safety_distance:
                conflicts.append((wp_a, wp_b))
    return conflicts



# wp = waypoint
# Checks for spatial conflicts between two missions in 3D.
# Returns a list of conflicting waypoint pairs (point from A, point from B).
