import matplotlib.pyplot as plt
from uav_deconfliction.drone_data import Mission

def plot_3d_missions(primary: Mission, others: list, conflicts: list):    # Plots the primary mission and other missions in 3D space.

    fig = plt.figure()                                                    # Conflicts are highlighted as red markers.
    ax = fig.add_subplot(111, projection='3d')

    # Plot primary mission
    xs = [wp.x for wp in primary.waypoints]
    ys = [wp.y for wp in primary.waypoints]
    zs = [wp.z for wp in primary.waypoints]
    ax.plot(xs, ys, zs, marker='o', color='green', label=primary.drone_id)

    # Plot other missions
    colors = ['blue', 'orange', 'purple', 'white']
    for idx, mission in enumerate(others):
        xs = [wp.x for wp in mission.waypoints]
        ys = [wp.y for wp in mission.waypoints]
        zs = [wp.z for wp in mission.waypoints]
        ax.plot(xs, ys, zs, marker='o', color=colors[idx % len(colors)], label=mission.drone_id)

    # Highlight conflicts
    for c in conflicts:
        px, py, pz, _ = c["primary_point"]
        ox, oy, oz, _ = c["other_point"]
        ax.scatter([px, ox], [py, oy], [pz, oz], color='red', s=60, label='Conflict')

    ax.set_xlabel('X Position (m)')
    ax.set_ylabel('Y Position (m)')
    ax.set_zlabel('Altitude (m)')
    ax.set_title('3D UAV Mission simulation')
    ax.legend()
    plt.show()
