from typing import List
from dataclasses import dataclass

@dataclass
class Waypoint:               # Represents drone corordinates in the space.
    x: float
    y: float
    z: float
    time: float

@dataclass
class Mission:                # Represents a mission consisting of waypoints,(unique id, ordered list and mission time).
    drone_id: str
    waypoints: List[Waypoint]
    start_time: float
    end_time: float



