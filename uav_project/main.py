from uav_deconfliction.drone_data import Waypoint, Mission
from uav_deconfliction.spatial_check import spatial_conflicts
from uav_deconfliction.temporal_check import temporal_conflicts
from uav_deconfliction.visualization import plot_3d_missions

primary = Mission(                        # Create missions in 3D
    drone_id="drone_A",
    waypoints=[
        Waypoint(0, 0, 20, time=0),
        Waypoint(60, 40, 30, time=10),
        Waypoint(75, 70, 45, time=20)],
    start_time=0,
    end_time=30)

other1 = Mission(
    drone_id="drone_B",
    waypoints=[
        Waypoint(80, 0, 20, time=0),
        Waypoint(60, 40, 40, time=10),
        Waypoint(20, 70, 45, time=20)],
    start_time=0,
    end_time=30)

other2 = Mission(
    drone_id="drone_C",
    waypoints=[
        Waypoint(100, 100, 80, time=0),
        Waypoint(70, 25, 62, time=10)],
    start_time=0,
    end_time=30)

all_conflicts = []                       # Check for conflicts
safety_distance = 5

for other in [other1, other2]:
    spatial_hits = spatial_conflicts(primary, other, safety_distance)
    if spatial_hits:
        temporal_hits = temporal_conflicts(primary, other)
        for wp_a, wp_b in spatial_hits:
            if (wp_a, wp_b) in temporal_hits:
                all_conflicts.append({
                    "other_drone": other.drone_id,
                    "primary_point": (wp_a.x, wp_a.y, wp_a.z, wp_a.time),
                    "other_point": (wp_b.x, wp_b.y, wp_b.z, wp_b.time)})


if all_conflicts:                        # Output results
    print("Conflict detected:")
    for c in all_conflicts:
        print(f"Conflict with {c['other_drone']}")
        print(f"Primary:{c['primary_point']}")
        print(f"Other:{c['other_point']}")
else:
    print("No conflicts detected.")


plot_3d_missions(primary, [other1, other2], all_conflicts)