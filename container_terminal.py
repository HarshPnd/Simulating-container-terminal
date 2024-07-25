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
        self.container_queue = simpy.Store(environment)

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
            yield self.environment.process(self.unload_container(vessel_id, container_number))

    def unload_container(self, vessel_id, container_number):
        """Simulate the process of unloading a container."""
        with self.cranes.request() as crane_request:
            yield crane_request
            print(f"Time {int(self.environment.now)}: Crane starts moving container {container_number} from vessel {vessel_id}")
            yield self.environment.timeout(CONTAINER_TRANSFER_TIME)
            print(f"Time {int(self.environment.now)}: Crane finished moving container {container_number} from vessel {vessel_id}")
            # Add the unloaded container to the container queue
            yield self.container_queue.put((vessel_id, container_number))
            # Start the transport process for this container
            self.environment.process(self.transport_container())

    def transport_container(self):
        """Simulate the transport of a container by a truck."""
        while True:
            # Wait for a container to be available in the queue
            vessel_id, container_number = yield self.container_queue.get()
            with self.trucks.request() as truck_request:
                yield truck_request
                print(f"Time {int(self.environment.now)}: Truck picks up container {container_number} from vessel {vessel_id}")
                yield self.environment.timeout(TRUCK_CYCLE_TIME)
                print(f"Time {int(self.environment.now)}: Truck drops off container {container_number} from vessel {vessel_id}")
