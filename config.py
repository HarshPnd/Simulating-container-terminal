# config.py

# Average time (in minutes) between vessel arrivals
AVERAGE_INTER_ARRIVAL_TIME = 5 * 60  # 5 hours converted to minutes

# Time taken by a quay crane to move one container (in minutes)
CONTAINER_TRANSFER_TIME = 3  # 3 minutes per container

# Round trip time for a terminal truck (in minutes)
TRUCK_CYCLE_TIME = 6  # 6 minutes for one complete round trip

# Number of containers each vessel carries
CONTAINERS_PER_VESSEL = 150  # 150 containers per vessel

# Number of berths available at the terminal
NUMBER_OF_BERTHS = 2  # 2 berths

# Number of quay cranes available
NUMBER_OF_CRANES = 2  # 2 quay cranes

# Number of terminal trucks available
NUMBER_OF_TRUCKS = 3  # 3 terminal trucks

# Default total duration of the simulation (in minutes)
TOTAL_SIMULATION_DURATION = 24 * 60  # 1 day converted to minutes
