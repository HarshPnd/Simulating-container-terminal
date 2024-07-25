# vessel_generator.py

import random
from config import AVERAGE_INTER_ARRIVAL_TIME

def vessel_generator(environment, terminal, vessel_arrival_flag):
    """Generate vessels arriving at the terminal at random intervals."""
    vessel_id = 0
    while True:
        inter_arrival_time = random.expovariate(1 / AVERAGE_INTER_ARRIVAL_TIME)
        yield environment.timeout(inter_arrival_time)
        vessel_id += 1
        vessel_arrival_flag[0] = True  # Set the flag to True when the first vessel arrives
        print(f"Time {int(environment.now)}: Vessel {vessel_id} arrives")
        environment.process(terminal.berth_vessel(vessel_id))
