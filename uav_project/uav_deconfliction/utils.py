import math
from uav_deconfliction.drone_data import Waypoint

def euclidean_distance_3d(p1: Waypoint, p2: Waypoint) -> float:  #Calculate Euclidean distance between two waypoints in 3D space.
    return math.sqrt(
        (p1.x - p2.x) ** 2 +
        (p1.y - p2.y) ** 2 +
        (p1.z - p2.z) ** 2)

def time_overlap(t1_start: float, t1_end: float, t2_start: float, t2_end: float) -> bool: #Check if two time intervals overlap.
    return max(t1_start, t2_start) <= min(t1_end, t2_end)
