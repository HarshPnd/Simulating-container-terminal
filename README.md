# Simulating-container-terminal

# About the Project -

### Project Overview
The Container Terminal Simulation models how a container terminal works. It uses SimPy to simulate vessels arriving, unloading containers, and moving them with terminal trucks.

### What It Does
- **Vessel Arrival and Berthing:** Shows vessels arriving and waiting for available berths.
- **Container Unloading:** Simulates cranes unloading containers from vessels.
- **Container Transport:** Models the movement of containers from cranes to storage or other locations using trucks.

### Key Functionalities
- **Vessel Generation:** Vessels arrive at random intervals, managed by a generator.
- **Resource Management:** Handles berths, cranes, and trucks using SimPy’s tools.
- **Unloading and Transport:** Manages unloading with cranes and transport with trucks, with detailed logs.
- **Flexible Duration:** Users can set the simulation length, defaulting to one day.
- **Detailed Logging:** Records events like vessel arrivals, unloading, and truck movements.



# What is Python ?

Python is a high-level, interpreted programming language valued for its simplicity and readability. It supports various programming styles, including procedural, object-oriented, and functional. Python’s clear syntax and extensive standard library make it ideal for diverse tasks, from web development and data analysis to AI and scientific computing. Its large, active community contributes many third-party packages and frameworks, boosting its flexibility and ease of use.

# What is SimPy ?

SimPy is a Python library used for discrete-event simulations. It helps model complex systems by managing processes, events, and resources. With SimPy, you can create and control processes, handle shared resources like cranes and trucks, and schedule events. This allows you to simulate and analyze systems like container terminals, manufacturing lines, or service operations.


---

# How to run

- __Python Installation:__ Install Python 3.x on your system.

## Step 1: Create and Activate a Virtual Environment

-       virtualenv venv
-       .\venv\Scripts\activate

## Step 2: Installl Dependencies

-       pip install -r requirements.txt

## Step 3: Run the Simulation

-       python main.py



___

# Code

## config.py

This file contains the configuration constants used in the simulation. Each constant is briefly described below:

- **AVERAGE_INTER_ARRIVAL_TIME**: The average time between vessel arrivals, set to 5 hours (300 minutes).
  
- **CONTAINER_TRANSFER_TIME**: The time taken by a quay crane to move one container, set to 3 minutes per container.

- **TRUCK_CYCLE_TIME**: The round trip time for a terminal truck, set to 6 minutes for one complete round trip.

- **CONTAINERS_PER_VESSEL**: The number of containers each vessel carries, set to 150 containers per vessel.

- **NUMBER_OF_BERTHS**: The number of berths available at the terminal, set to 2 berths.

- **NUMBER_OF_CRANES**: The number of quay cranes available, set to 2 quay cranes.

- **NUMBER_OF_TRUCKS**: The number of terminal trucks available, set to 3 terminal trucks.

- **TOTAL_SIMULATION_DURATION**: The default total duration of the simulation, set to 1 day (1440 minutes).

---

# vessel_generator.py

This file defines the `vessel_generator` function, which simulates the arrival of vessels at the container terminal. 

## Imports

- `random`: Used to generate random intervals for vessel arrivals.
- `config`: Imports the `AVERAGE_INTER_ARRIVAL_TIME` constant from the configuration file.

## Function: vessel_generator

```python
def vessel_generator(environment, terminal):
    """Generate vessels arriving at the terminal at random intervals."""
    vessel_id = 0
    while True:
        inter_arrival_time = random.expovariate(1 / AVERAGE_INTER_ARRIVAL_TIME)
        yield environment.timeout(inter_arrival_time)
        vessel_id += 1
        print(f"Time {int(environment.now)}: Vessel {vessel_id} arrives")
        environment.process(terminal.berth_vessel(vessel_id))
```
  - **Description**: 
    - This function simulates the arrival of vessels at random intervals based on an exponential distribution.
    - `vessel_id` starts at 0 and increments with each new vessel.
    - The `inter_arrival_time` is calculated using an exponential distribution with the average inter-arrival time.
    - The function yields a timeout for the calculated inter-arrival time, simulating the wait time between vessel arrivals.
    - When a vessel arrives, its arrival time and ID are printed, and the `berth_vessel` process is initiated for the vessel.
---

# container_terminal.py

This file contains the main logic for simulating the operations of a container terminal, including berthing vessels, unloading containers, and transporting containers using trucks.

- **Imports**: 
  - `simpy`: The SimPy library for discrete-event simulation.
  - Constants from `config`: Various constants needed for the simulation.

- **Class: `ContainerTerminal`**
  - **Description**: Represents the container terminal simulation.
  
  - **Initialization (`__init__`)**:
    - **Parameters**: 
      - `environment`: The SimPy environment for the simulation.
    - **Attributes**:
      - `self.environment`: Stores the simulation environment.
      - `self.berths`: SimPy resource representing the number of berths.
      - `self.cranes`: SimPy resource representing the number of cranes.
      - `self.trucks`: SimPy resource representing the number of trucks.

  - **Method: `berth_vessel`**:
    - **Description**: Simulates the berthing process of a vessel.
    - **Parameters**: 
      - `vessel_id`: The ID of the vessel.
    - **Process**:
      - Requests a berth.
      - Once a berth is available, the vessel is berthed and the unloading process begins.
      - After unloading, the vessel departs.

  - **Method: `unload_vessel`**:
    - **Description**: Simulates the unloading process of a vessel.
    - **Parameters**: 
      - `vessel_id`: The ID of the vessel.
    - **Process**:
      - Iterates over the number of containers in the vessel.
      - For each container, initiates the process to move the container.

  - **Method: `move_container`**:
    - **Description**: Simulates the process of moving a container from the vessel to its destination.
    - **Parameters**: 
      - `vessel_id`: The ID of the vessel.
      - `container_number`: The number of the container.
    - **Process**:
      - Requests a crane.
      - Once a crane is available, the crane starts moving the container.
      - After moving the container, requests a truck.
      - Once a truck is available, the truck picks up the container and transports it.

---

# main.py

This file serves as the entry point for running the container terminal simulation. It includes the setup for the SimPy environment, the initialization of the container terminal, and the vessel generation process.

- **Imports**: 
  - `simpy`: The SimPy library for discrete-event simulation.
  - `TOTAL_SIMULATION_DURATION as DEFAULT_SIMULATION_DURATION` from `config`: The default duration of the simulation.
  - `ContainerTerminal` from `container_terminal`: The class representing the container terminal.
  - `vessel_generator` from `vessel_generator`: The function for generating vessels.

- **Function: `get_simulation_duration`**:
  - **Description**: Prompts the user to enter the simulation duration and handles invalid inputs.
  - **Process**:
    - Prompts the user to enter the simulation duration in minutes.
    - If the user does not provide input, uses the default simulation duration.
    - Checks if the entered duration is a positive integer. If not, it uses the default simulation duration.
    - Returns the simulation duration.

- **Simulation Setup and Execution**:
  - Calls `get_simulation_duration` to get the simulation duration from the user.
  - Initializes the SimPy environment.
  - Creates an instance of the `ContainerTerminal` class with the SimPy environment.
  - Starts the vessel generator process.
  - Runs the simulation for the specified duration.

  ----


  # Demo Run

  ## Output:

      Enter the total simulation duration in minutes (or press Enter to use the default value of 1 day): 151  
      Time 57: Vessel 1 arrives  
      Time 57: Vessel 1 berths  
      Time 57: Crane starts moving container 1 from vessel 1  
      Time 60: Vessel 2 arrives  
      Time 60: Vessel 2 berths   
      Time 60: Crane starts moving container 1 from vessel 2   
      Time 60: Crane finished moving container 1 from vessel 1   
      Time 60: Crane starts moving container 2 from vessel 1   
      Time 60: Truck picks up container 1 from vessel 1   
      Time 63: Crane finished moving container 1 from vessel 2   
      Time 63: Crane starts moving container 2 from vessel 2   
      Time 63: Truck picks up container 1 from vessel 2   
      Time 63: Crane finished moving container 2 from vessel 1   
      Time 63: Crane starts moving container 3 from vessel 1   
      Time 63: Truck picks up container 2 from vessel 1   
      Time 66: Crane finished moving container 2 from vessel 2   
      Time 66: Crane starts moving container 3 from vessel 2   
      Time 66: Truck drops off container 1 from vessel 1   
      Time 66: Crane finished moving container 3 from vessel 1   
      Time 66: Truck picks up container 2 from vessel 2   
      Time 66: Crane starts moving container 4 from vessel 1   
      Time 69: Truck drops off container 1 from vessel 2   
      Time 69: Crane finished moving container 3 from vessel 2   
      Time 69: Truck picks up container 3 from vessel 1   
      Time 69: Crane starts moving container 4 from vessel 2   
      Time 69: Truck drops off container 2 from vessel 1   
      Time 69: Crane finished moving container 4 from vessel 1   
      Time 69: Truck picks up container 3 from vessel 2   
      Time 69: Crane starts moving container 5 from vessel 1   
      Time 72: Crane finished moving container 4 from vessel 2   
      Time 72: Crane starts moving container 5 from vessel 2   
      Time 72: Truck drops off container 2 from vessel 2   
      Time 72: Crane finished moving container 5 from vessel 1   
      Time 72: Truck picks up container 4 from vessel 1   
      Time 72: Crane starts moving container 6 from vessel 1   
      Time 75: Truck drops off container 3 from vessel 1   
      Time 75: Crane finished moving container 5 from vessel 2   
      Time 75: Truck picks up container 4 from vessel 2   
      Time 75: Crane starts moving container 6 from vessel 2   
      Time 75: Truck drops off container 3 from vessel 2   
      Time 75: Crane finished moving container 6 from vessel 1   
      Time 75: Truck picks up container 5 from vessel 1   
      Time 75: Crane starts moving container 7 from vessel 1   
      Time 78: Crane finished moving container 6 from vessel 2   
      Time 78: Crane starts moving container 7 from vessel 2   
      Time 78: Truck drops off container 4 from vessel 1   
      Time 78: Crane finished moving container 7 from vessel 1   
      Time 78: Truck picks up container 5 from vessel 2   
      Time 78: Crane starts moving container 8 from vessel 1   
      Time 81: Truck drops off container 4 from vessel 2   
      Time 81: Crane finished moving container 7 from vessel 2   
      Time 81: Truck picks up container 6 from vessel 1   
      Time 81: Crane starts moving container 8 from vessel 2     
      Time 81: Truck drops off container 5 from vessel 1    
      Time 81: Crane finished moving container 8 from vessel 1    
      Time 81: Truck picks up container 6 from vessel 2    
      Time 81: Crane starts moving container 9 from vessel 1    
      Time 84: Crane finished moving container 8 from vessel 2    
      Time 84: Crane starts moving container 9 from vessel 2    
      Time 84: Truck drops off container 5 from vessel 2    
      Time 84: Crane finished moving container 9 from vessel 1    
      Time 84: Truck picks up container 7 from vessel 1    
      Time 84: Crane starts moving container 10 from vessel 1    
      Time 87: Truck drops off container 6 from vessel 1    
      Time 87: Crane finished moving container 9 from vessel 2    
      Time 87: Truck picks up container 7 from vessel 2    
      Time 87: Crane starts moving container 10 from vessel 2    
      Time 87: Truck drops off container 6 from vessel 2    
      Time 87: Crane finished moving container 10 from vessel 1    
      Time 87: Truck picks up container 8 from vessel 1   
      Time 87: Crane starts moving container 11 from vessel 1   
      Time 90: Crane finished moving container 10 from vessel 2   
      Time 90: Crane starts moving container 11 from vessel 2   
      Time 90: Truck drops off container 7 from vessel 1   
      Time 90: Crane finished moving container 11 from vessel 1   
      Time 90: Truck picks up container 8 from vessel 2   
      Time 90: Crane starts moving container 12 from vessel 1   
      Time 93: Truck drops off container 7 from vessel 2   
      Time 93: Crane finished moving container 11 from vessel 2   
      Time 93: Truck picks up container 9 from vessel 1   
      Time 93: Crane starts moving container 12 from vessel 2   
      Time 93: Truck drops off container 8 from vessel 1   
      Time 93: Crane finished moving container 12 from vessel 1   
      Time 93: Truck picks up container 9 from vessel 2   
      Time 93: Crane starts moving container 13 from vessel 1   
      Time 96: Crane finished moving container 12 from vessel 2   
      Time 96: Crane starts moving container 13 from vessel 2   
      Time 96: Truck drops off container 8 from vessel 2   
      Time 96: Crane finished moving container 13 from vessel 1   
      Time 96: Truck picks up container 10 from vessel 1   
      Time 96: Crane starts moving container 14 from vessel 1   
      Time 99: Truck drops off container 9 from vessel 1   
      Time 99: Crane finished moving container 13 from vessel 2   
      Time 99: Truck picks up container 10 from vessel 2   
      Time 99: Crane starts moving container 14 from vessel 2   
      Time 99: Truck drops off container 9 from vessel 2   
      Time 99: Crane finished moving container 14 from vessel 1    
      Time 99: Truck picks up container 11 from vessel 1    
      Time 99: Crane starts moving container 15 from vessel 1    
      Time 102: Crane finished moving container 14 from vessel 2    
      Time 102: Crane starts moving container 15 from vessel 2    
      Time 102: Truck drops off container 10 from vessel 1    
      Time 102: Crane finished moving container 15 from vessel 1    
      Time 102: Truck picks up container 11 from vessel 2    
      Time 102: Crane starts moving container 16 from vessel 1    
      Time 105: Truck drops off container 10 from vessel 2    
      Time 105: Crane finished moving container 15 from vessel 2    
      Time 105: Truck picks up container 12 from vessel 1    
      Time 105: Crane starts moving container 16 from vessel 2    
      Time 105: Truck drops off container 11 from vessel 1    
      Time 105: Crane finished moving container 16 from vessel 1    
      Time 105: Truck picks up container 12 from vessel 2    
      Time 105: Crane starts moving container 17 from vessel 1    
      Time 108: Crane finished moving container 16 from vessel 2    
      Time 108: Crane starts moving container 17 from vessel 2    
      Time 108: Truck drops off container 11 from vessel 2    
      Time 108: Crane finished moving container 17 from vessel 1    
      Time 108: Truck picks up container 13 from vessel 1    
      Time 108: Crane starts moving container 18 from vessel 1    
      Time 111: Truck drops off container 12 from vessel 1    
      Time 111: Crane finished moving container 17 from vessel 2    
      Time 111: Truck picks up container 13 from vessel 2    
      Time 111: Crane starts moving container 18 from vessel 2    
      Time 111: Truck drops off container 12 from vessel 2    
      Time 111: Crane finished moving container 18 from vessel 1    
      Time 111: Truck picks up container 14 from vessel 1    
      Time 111: Crane starts moving container 19 from vessel 1    
      Time 114: Crane finished moving container 18 from vessel 2    
      Time 114: Crane starts moving container 19 from vessel 2    
      Time 114: Truck drops off container 13 from vessel 1    
      Time 114: Crane finished moving container 19 from vessel 1    
      Time 114: Truck picks up container 14 from vessel 2    
      Time 114: Crane starts moving container 20 from vessel 1    
      Time 117: Truck drops off container 13 from vessel 2    
      Time 117: Crane finished moving container 19 from vessel 2    
      Time 117: Truck picks up container 15 from vessel 1    
      Time 117: Crane starts moving container 20 from vessel 2    
      Time 117: Truck drops off container 14 from vessel 1    
      Time 117: Crane finished moving container 20 from vessel 1    
      Time 117: Truck picks up container 15 from vessel 2    
      Time 117: Crane starts moving container 21 from vessel 1    
      Time 120: Crane finished moving container 20 from vessel 2    
      Time 120: Crane starts moving container 21 from vessel 2    
      Time 120: Truck drops off container 14 from vessel 2    
      Time 120: Crane finished moving container 21 from vessel 1    
      Time 120: Truck picks up container 16 from vessel 1    
      Time 120: Crane starts moving container 22 from vessel 1    
      Time 123: Truck drops off container 15 from vessel 1    
      Time 123: Crane finished moving container 21 from vessel 2    
      Time 123: Truck picks up container 16 from vessel 2    
      Time 123: Crane starts moving container 22 from vessel 2    
      Time 123: Truck drops off container 15 from vessel 2    
      Time 123: Crane finished moving container 22 from vessel 1    
      Time 123: Truck picks up container 17 from vessel 1    
      Time 123: Crane starts moving container 23 from vessel 1    
      Time 126: Crane finished moving container 22 from vessel 2    
      Time 126: Crane starts moving container 23 from vessel 2    
      Time 126: Truck drops off container 16 from vessel 1    
      Time 126: Crane finished moving container 23 from vessel 1    
      Time 126: Truck picks up container 17 from vessel 2    
      Time 126: Crane starts moving container 24 from vessel 1    
      Time 129: Truck drops off container 16 from vessel 2    
      Time 129: Crane finished moving container 23 from vessel 2    
      Time 129: Truck picks up container 18 from vessel 1    
      Time 129: Crane starts moving container 24 from vessel 2    
      Time 129: Truck drops off container 17 from vessel 1    
      Time 129: Crane finished moving container 24 from vessel 1    
      Time 129: Truck picks up container 18 from vessel 2    
      Time 129: Crane starts moving container 25 from vessel 1    
      Time 132: Crane finished moving container 24 from vessel 2    
      Time 132: Crane starts moving container 25 from vessel 2    
      Time 132: Truck drops off container 17 from vessel 2    
      Time 132: Crane finished moving container 25 from vessel 1    
      Time 132: Truck picks up container 19 from vessel 1    
      Time 132: Crane starts moving container 26 from vessel 1    
      Time 135: Truck drops off container 18 from vessel 1    
      Time 135: Crane finished moving container 25 from vessel 2    
      Time 135: Truck picks up container 19 from vessel 2    
      Time 135: Crane starts moving container 26 from vessel 2    
      Time 135: Truck drops off container 18 from vessel 2    
      Time 135: Crane finished moving container 26 from vessel 1    
      Time 135: Truck picks up container 20 from vessel 1    
      Time 135: Crane starts moving container 27 from vessel 1    
      Time 138: Crane finished moving container 26 from vessel 2    
      Time 138: Crane starts moving container 27 from vessel 2    
      Time 138: Truck drops off container 19 from vessel 1    
      Time 138: Crane finished moving container 27 from vessel 1    
      Time 138: Truck picks up container 20 from vessel 2    
      Time 138: Crane starts moving container 28 from vessel 1    
      Time 141: Truck drops off container 19 from vessel 2    
      Time 141: Crane finished moving container 27 from vessel 2    
      Time 141: Truck picks up container 21 from vessel 1    
      Time 141: Crane starts moving container 28 from vessel 2    
      Time 141: Truck drops off container 20 from vessel 1    
      Time 141: Crane finished moving container 28 from vessel 1    
      Time 141: Truck picks up container 21 from vessel 2    
      Time 141: Crane starts moving container 29 from vessel 1    
      Time 144: Crane finished moving container 28 from vessel 2    
      Time 144: Crane starts moving container 29 from vessel 2    
      Time 144: Truck drops off container 20 from vessel 2    
      Time 144: Crane finished moving container 29 from vessel 1    
      Time 144: Truck picks up container 22 from vessel 1    
      Time 144: Crane starts moving container 30 from vessel 1    
      Time 147: Truck drops off container 21 from vessel 1    
      Time 147: Crane finished moving container 29 from vessel 2    
      Time 147: Truck picks up container 22 from vessel 2    
      Time 147: Crane starts moving container 30 from vessel 2    
      Time 147: Truck drops off container 21 from vessel 2    
      Time 147: Crane finished moving container 30 from vessel 1    
      Time 147: Truck picks up container 23 from vessel 1    
      Time 147: Crane starts moving container 31 from vessel 1    
      Time 150: Crane finished moving container 30 from vessel 2    
      Time 150: Crane starts moving container 31 from vessel 2    
      Time 150: Truck drops off container 22 from vessel 1    
      Time 150: Crane finished moving container 31 from vessel 1    
      Time 150: Truck picks up container 23 from vessel 2    
      Time 150: Crane starts moving container 32 from vessel 1    
      





 
 P.S. - Any suggestions and improvements are warmly welcome.