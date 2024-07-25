# main.py

import simpy
from config import TOTAL_SIMULATION_DURATION as DEFAULT_SIMULATION_DURATION
from container_terminal import ContainerTerminal
from vessel_generator import vessel_generator

def get_simulation_duration():
    """Prompt the user to enter the simulation duration and handle invalid inputs."""
    try:
        user_input = input("Enter the total simulation duration in minutes (or press Enter to use the default value of 1 day): ")
        if user_input.strip() == "":
            print(f"No input provided. Using default simulation duration of {DEFAULT_SIMULATION_DURATION} minutes.")
            return DEFAULT_SIMULATION_DURATION
        simulation_duration = int(user_input)
        if simulation_duration <= 0:
            raise ValueError("The duration must be a positive integer.")
        return simulation_duration
    except ValueError as e:
        print(f"Invalid input: {e}. Using default simulation duration of {DEFAULT_SIMULATION_DURATION} minutes.")
        return DEFAULT_SIMULATION_DURATION

# Get the simulation duration from the user
simulation_duration = get_simulation_duration()

# Initialize the simulation environment
env = simpy.Environment()
# Create an instance of the ContainerTerminal class
terminal = ContainerTerminal(env)
# Start the vessel generator process
env.process(vessel_generator(env, terminal))

# Run the simulation for the specified duration
env.run(until=simulation_duration)
