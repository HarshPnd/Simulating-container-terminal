import simpy
from config import CONTAINER_TRANSFER_TIME, TRUCK_CYCLE_TIME, CONTAINERS_PER_VESSEL, NUMBER_OF_BERTHS, NUMBER_OF_CRANES, NUMBER_OF_TRUCKS

class ContainerTerminal:
    """Class representing a container terminal simulation."""

    def __init__(self, environment):
        """Initialize the terminal with resources."""
        self.environment = environment
        self.berths = simpy.Resource(environment, NUMBER_OF_BERTHS)
        self.cranes = simpy.Resource(environment, NUMBER_OF_CRANES)
        self.trucks = simpy.Resource(environment, NUMBER_OF_TRUCKS)

    def berth_vessel(self, vessel_id):
        """Simulate the berthing process of a vessel."""
        with self.berths.request() as request:
            yield request
            print(f"Time {int(self.environment.now)}: Vessel {vessel_id} berths")
            yield self.environment.process(self.unload_vessel(vessel_id))
            print(f"Time {int(self.environment.now)}: Vessel {vessel_id} has finished unloading and departs")

    def unload_vessel(self, vessel_id):
        """Simulate the unloading process of a vessel."""
        for container_number in range(1, CONTAINERS_PER_VESSEL + 1):
            yield self.environment.process(self.move_container(vessel_id, container_number))

    def move_container(self, vessel_id, container_number):
        """Simulate the process of moving a container."""
        # Request a crane
        with self.cranes.request() as crane_request:
            yield crane_request
            print(f"Time {int(self.environment.now)}: Crane starts moving container {container_number} from vessel {vessel_id}")
            yield self.environment.timeout(CONTAINER_TRANSFER_TIME)

        # Request a truck
        with self.trucks.request() as truck_request:
            yield truck_request
            print(f"Time {int(self.environment.now)}: Truck picks up container {container_number} from vessel {vessel_id}")
            yield self.environment.timeout(TRUCK_CYCLE_TIME)
            print(f"Time {int(self.environment.now)}: Truck drops off container {container_number} from vessel {vessel_id}")
